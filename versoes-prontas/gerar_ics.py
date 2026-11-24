"""Gera prazos-mei.ics (calendário de prazos do MEI).

Uso: python gerar_ics.py   (escreve prazos-mei.ics na mesma pasta)
Só usa a biblioteca padrão. Datas conferidas em 24/11/2026 (ver referencias/00 e 06).
"""

from pathlib import Path

PASTA = Path(__file__).resolve().parent
CARIMBO = "20261124T120000Z"
LINK = "https://github.com/Clarki7/contador-mei-br"

# (uid, data AAAAMMDD, título, descrição, regra de repetição ou None, aviso antes)
EVENTOS = [
    ("das-mensal", "20261220", "Pagar o DAS do MEI",
     "Vence todo dia 20 (o do mês anterior). Gere a guia só no PGMEI ou no App MEI: "
     "https://www8.receita.fazenda.gov.br/SimplesNacional/Aplicacoes/ATSPO/pgmei.app . "
     "Se cair em fim de semana ou feriado, vale o próximo dia útil. "
     "Atraso: multa de 0,33% ao dia até 20% + juros, e o mês não conta para o INSS.",
     "FREQ=MONTHLY;BYMONTHDAY=20", "-P3D"),
    ("dasn-anual", "20270531", "Entregar a DASN-SIMEI (declaração anual do MEI)",
     "Prazo: 31/05, mesmo sem faturamento. Informe a receita bruta do ano anterior, separada em "
     "comércio/indústria e serviços: "
     "https://www8.receita.fazenda.gov.br/SimplesNacional/Aplicacoes/ATSPO/DASNSIMEI.app/Default.aspx . "
     "Multa mínima de R$ 50 se atrasar.",
     "FREQ=YEARLY;BYMONTH=5;BYMONTHDAY=31", "-P15D"),
    ("desenquadramento-2026", "20261231", "Último dia para pedir para sair do MEI e ser ME em 2027",
     "Quem quer ser microempresa (ME) já em 01/01/2027 deve pedir o desenquadramento por opção "
     "até hoje, no Portal do Simples Nacional. Pela regra nova, pedido em 2027 só vale em 2028 "
     "(ponto parcial: conferir no portal). Recomendado falar com um contador antes.",
     None, "-P10D"),
    ("mudancas-2027", "20270101", "MEI: começam as regras de 2027",
     "Teto de R$ 110 mil; até 2 empregados; nota fiscal passa a ser obrigatória (para pessoa física "
     "sem CNPJ, vale a DASN ou 1 nota consolidada por mês); perdão automático da parte do INSS do "
     "DAS vencido até 13/10/2026 (Portaria Conjunta RFB/PGFN 740/2026).",
     None, None),
    ("edital-pgfn-6-2026", "20270129", "Fim da adesão ao Edital PGFN 6/2026 (dívida ativa do MEI)",
     "Prazo até 19h de hoje, no Regularize (https://www.regularize.pgfn.gov.br/), entrando com o CNPJ. "
     "Até 133 parcelas, mínimo R$ 25 para o MEI, desconto em juros e multas. "
     "Confira as condições no próprio Regularize.",
     None, "-P7D"),
    ("perdao-condicao-fim", "20270720", "Último DAS da condição do perdão (competência junho/2027)",
     "O perdão da LC 238 só fica valendo se o DAS de janeiro a junho de 2027 for pago em dia "
     "(vencimentos de fevereiro a julho de 2027). Este é o último.",
     None, "-P3D"),
]


def dobrar(linha: str) -> str:
    """Quebra linhas longas a cada 73 caracteres (RFC 5545)."""
    partes = []
    while len(linha.encode("utf-8")) > 73:
        corte = 73
        while len(linha[:corte].encode("utf-8")) > 73:
            corte -= 1
        partes.append(linha[:corte])
        linha = " " + linha[corte:]
    partes.append(linha)
    return "\r\n".join(partes)


def escapar(t: str) -> str:
    return t.replace("\\", "\\\\").replace(";", "\\;").replace(",", "\\,").replace("\n", "\\n")


def dia_seguinte(d: str) -> str:
    from datetime import date, timedelta
    x = date(int(d[:4]), int(d[4:6]), int(d[6:])) + timedelta(days=1)
    return x.strftime("%Y%m%d")


def main() -> None:
    linhas = [
        "BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//contador-mei-br//prazos//PT-BR",
        "CALSCALE:GREGORIAN", "METHOD:PUBLISH", "X-WR-CALNAME:Prazos do MEI",
        "X-WR-TIMEZONE:America/Sao_Paulo",
    ]
    for uid, data, titulo, desc, regra, aviso in EVENTOS:
        linhas += [
            "BEGIN:VEVENT",
            f"UID:{uid}@contador-mei-br",
            f"DTSTAMP:{CARIMBO}",
            f"DTSTART;VALUE=DATE:{data}",
            f"DTEND;VALUE=DATE:{dia_seguinte(data)}",
            f"SUMMARY:{escapar(titulo)}",
            f"DESCRIPTION:{escapar(desc + ' Fonte e mais detalhes: ' + LINK)}",
            "TRANSP:TRANSPARENT",
        ]
        if regra:
            linhas.append(f"RRULE:{regra}")
        if aviso:
            linhas += ["BEGIN:VALARM", "ACTION:DISPLAY", f"DESCRIPTION:{escapar(titulo)}",
                       f"TRIGGER:{aviso}", "END:VALARM"]
        linhas.append("END:VEVENT")
    linhas.append("END:VCALENDAR")
    texto = "\r\n".join(dobrar(l) for l in linhas) + "\r\n"
    (PASTA / "prazos-mei.ics").write_bytes(texto.encode("utf-8"))
    print(f"prazos-mei.ics gerado com {len(EVENTOS)} eventos.")


if __name__ == "__main__":
    main()
