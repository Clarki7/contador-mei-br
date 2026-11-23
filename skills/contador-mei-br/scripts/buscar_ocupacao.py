"""Busca ocupações permitidas ao MEI (Anexo XI da Res. CGSN 140/2018).

Uso:
    python buscar_ocupacao.py "computador"      # busca por palavra (ignora acentos)
    python buscar_ocupacao.py 9511-8/00         # busca por CNAE (com ou sem pontuação)
    python buscar_ocupacao.py "comerciante" --max 50

Só usa a biblioteca padrão do Python.
"""

import argparse
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

    achados = []
    for linha in linhas:
        if busca_cnae:
            if so_digitos(linha["cnae"]).startswith(digitos):
                achados.append(linha)
        else:
            alvo = normalizar(linha["ocupacao"] + " " + linha["descricao_cnae"])
            if all(re.search(r"(?<![a-z0-9])" + re.escape(p), alvo) for p in palavras):
                achados.append(linha)

    if not achados:
        print(f'Nenhuma ocupação do MEI encontrada para "{termo}".')
        print("Se a atividade não está na lista, ela NÃO pode ser exercida como MEI.")
        print("Fonte: Anexo XI da Res. CGSN 140/2018 - "
              "https://www8.receita.fazenda.gov.br/simplesnacional/arquivos/manual/anexo_xi.pdf")
        return 1

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
