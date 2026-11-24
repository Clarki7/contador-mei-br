"""Busca ocupações permitidas ao MEI (Anexo XI da Res. CGSN 140/2018).

Uso:
    python buscar_ocupacao.py "computador"      # busca por palavra (ignora acentos)
    python buscar_ocupacao.py 9511-8/00         # busca por CNAE (com ou sem pontuação)
    python buscar_ocupacao.py "comerciante" --max 50

Só usa a biblioteca padrão do Python.
"""

import argparse
import itertools
import csv
import re
import sys
import unicodedata
from pathlib import Path

CSV = Path(__file__).resolve().parent.parent / "dados" / "ocupacoes-mei.csv"


def normalizar(texto: str) -> str:
    sem_acento = unicodedata.normalize("NFKD", texto)
    sem_acento = "".join(c for c in sem_acento if not unicodedata.combining(c))
    return sem_acento.lower()


# Palavras do dia a dia -> termos usados no Anexo XI. Se a busca original
# não achar nada, o script tenta de novo trocando a palavra pelo sinônimo.
SINONIMOS = {
    "celular": ["telefonia"],
    "celulares": ["telefonia"],
    "smartphone": ["telefonia"],
    "conserto": ["manutencao", "reparacao"],
    "consertar": ["manutencao", "reparacao"],
    "concerto": ["manutencao", "reparacao"],
    "reparo": ["reparacao", "manutencao"],
    "notebook": ["computador", "informatica"],
    "pc": ["computador"],
    "unha": ["manicure"],
    "unhas": ["manicure"],
    "cabelo": ["cabeleireiro"],
    "salao": ["cabeleireiro"],
    "bolo": ["bolos", "doceiro"],
    "doce": ["doceiro"],
    "doces": ["doceiro"],
    "marmita": ["alimentos", "refeicoes"],
    "comida": ["alimentos", "refeicoes"],
    "roupa": ["vestuario", "artigos do vestuario"],
    "roupas": ["vestuario"],
    "moto": ["motocicletas", "motociclistas"],
    "motoboy": ["motoboy", "entrega"],
    "entregador": ["entrega", "motoboy"],
    "uber": ["passageiros"],
    "faxina": ["diarista", "limpeza"],
    "faxineira": ["diarista", "limpeza"],
    "pedreiro": ["pedreiro", "obras"],
    "pintor": ["pintor"],
    "eletricista": ["eletricista", "instalacao eletrica"],
    "encanador": ["encanador", "hidraulica"],
    "carro": ["veiculos", "automotores"],
    "mecanico": ["mecanico", "veiculos"],
    "foto": ["fotografo", "fotografia"],
    "fotos": ["fotografo", "fotografia"],
}


VAZIAS = {"de", "da", "do", "das", "dos", "e", "em", "para", "pra", "com", "a", "o", "as", "os", "no", "na"}


def so_digitos(texto: str) -> str:
    return re.sub(r"\D", "", texto)


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description="Busca ocupações do MEI")
    parser.add_argument("termo", help="palavra da ocupação/descrição ou código CNAE")
    parser.add_argument("--max", type=int, default=30, help="máximo de resultados (padrão 30)")
    args = parser.parse_args()

    termo = args.termo.strip()
    digitos = so_digitos(termo)
    busca_cnae = len(digitos) >= 4 and len(digitos) == len(re.sub(r"[\s./-]", "", termo))
    palavras = normalizar(termo).split()

    with CSV.open(encoding="utf-8", newline="") as f:
        linhas = list(csv.DictReader(f, delimiter=";"))

    def buscar(lista_palavras):
        res = []
        for linha in linhas:
            if busca_cnae:
                if so_digitos(linha["cnae"]).startswith(digitos):
                    res.append(linha)
            else:
                alvo = normalizar(linha["ocupacao"] + " " + linha["descricao_cnae"])
                if all(re.search(r"(?<![a-z0-9])" + re.escape(p), alvo) for p in lista_palavras):
                    res.append(linha)
        return res

    achados = buscar(palavras)
    trocas = []
    if not achados and not busca_cnae:
        # Tira palavras vazias e tenta todas as combinações com sinônimos oficiais.
        uteis = [p for p in palavras if p not in VAZIAS] or palavras
        opcoes = [[p] + SINONIMOS.get(p, []) for p in uteis]
        vistos = set()
        for combo in itertools.islice(itertools.product(*opcoes), 50):
            nova = [w for parte in combo for w in parte.split()]
            achou = buscar(nova)
            if achou and list(combo) != uteis:
                trocas.append(" + ".join(combo))
            for linha in achou:
                chave = (linha["ocupacao"], linha["cnae"])
                if chave not in vistos:
                    vistos.add(chave)
                    achados.append(linha)

    if not achados:
        print(f'Nenhuma ocupação do MEI encontrada para "{termo}".')
        print("Isso NÃO prova que a atividade é proibida: tente outras palavras "
              "(o nome oficial costuma ser diferente do popular) e confira o mapa "
              "referencias/05-ocupacoes-mapa.md.")
        print("Só se nenhuma busca achar a atividade é que ela não pode ser MEI.")
        print("Fonte: Anexo XI da Res. CGSN 140/2018 - "
              "https://www8.receita.fazenda.gov.br/simplesnacional/arquivos/manual/anexo_xi.pdf")
        return 1

    if trocas:
        print(f'Busca exata não achou nada; tentei: {", ".join(trocas)}. Confira se bate com a atividade.\n')

    print(f"{len(achados)} resultado(s) para \"{termo}\" (ISS/ICMS: S = contribuinte):\n")
    for linha in achados[: args.max]:
        print(f"- {linha['ocupacao']}")
        print(f"  CNAE {linha['cnae']} | {linha['descricao_cnae']} | ISS {linha['iss']} | ICMS {linha['icms']}")
    if len(achados) > args.max:
        print(f"\n... mais {len(achados) - args.max}. Use --max para ver todos ou refine a busca.")
    print("\nFonte: Anexo XI da Res. CGSN 140/2018 (PDF da Receita, conferido em 23/11/2026).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
