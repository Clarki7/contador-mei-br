# Check-up do MEI

Use quando a pessoa pedir "meu MEI está em dia?", "o que eu tenho que fazer?", "check-up", ou quando ela parecer perdida e não souber nem o que perguntar. O objetivo é sair com uma **lista curta de pendências da pessoa**, em ordem de risco, cada uma com o que fazer, onde e até quando.

Antes de começar, confira a data de hoje: as regras de 2026 e 2027 são diferentes (`00-resumo-por-ano.md`).

## As 5 perguntas

Faça todas numa mensagem só, numeradas, para a pessoa responder de uma vez. Pule as que já estiverem respondidas na conversa. Aceite "não sei" como resposta: ela vira pendência ("conferir no PGMEI").

1. **DAS:** você está pagando o DAS todo mês? Sabe se tem algum atrasado?
2. **Declaração anual (DASN-SIMEI):** você entregou a declaração deste ano (até 31/05)? E dos anos anteriores?
3. **Faturamento:** quanto você faturou, mais ou menos, este ano até agora? Em que mês e ano abriu o MEI?
4. **O que você faz e para quem:** qual a atividade na prática? Vende para pessoa física, para empresa (CNPJ) ou para os dois? Emite nota?
5. **Planos:** tem ou vai contratar funcionário? Pensa em sair do MEI ou virar microempresa?

## Como transformar respostas em pendências

Avalie nesta ordem (da mais grave para a mais leve). Inclua só o que se aplica.

| Se… | Pendência | Onde | Prazo | Fonte |
|---|---|---|---|---|
| Tem DAS atrasado ou "não sei" | Ver débitos e pagar ou parcelar. Explique a multa (0,33% ao dia, até 20%) e que mês atrasado não conta para o INSS | PGMEI; se já na dívida ativa, Regularize | o quanto antes | `06` ponto 4, `07` |
| Tem DAS atrasado vencido até 13/10/2026 | Avisar do perdão automático da parte do INSS em 01/01/2027, com a condição de pagar em dia jan–jun/2027. ICMS e ISS não entram | — | pagar fev–jul/2027 em dia | `00`, `06` ponto 5 |
| Está há muitos meses sem pagar nem declarar | Risco de cancelamento automático do CNPJ após 12 meses seguidos sem pagar nem declarar | PGMEI e DASN | já | `06` ponto 4 |
| DASN não entregue (este ano ou anteriores) | Entregar a DASN atrasada (multa mínima R$ 50). Sem DASN entregue não dá para parcelar | DASN-SIMEI | já | `03`, `07` |
| Faturamento acima do teto proporcional | Calcular: teto do ano ÷ 12 × meses de atividade no ano de abertura. Até 20% acima: comunicar desenquadramento e pagar DAS de excesso. Acima de 20%: efeito retroativo, **recomendar contador** | Portal do Simples Nacional | último dia útil do mês seguinte ao excesso | `00`, `02` seção 3 |
| Faturamento perto do teto (mais de 80%) | Alerta para acompanhar mês a mês | — | — | `00` |
| Atividade fora do Anexo XI | Rodar o script. Se não achar, explicar que não pode ser MEI e o caminho de sair. Em 2026: pedir até 31/12/2026 para valer em 2027 | Portal do Simples Nacional | 31/12/2026 | `04`, `05`, `00` |
| Vende para CNPJ e não emite nota | Emitir NFS-e no Emissor Nacional (serviço) ou nota de produto conforme o estado | gov.br/nfse | a cada venda | `06` ponto 2, `07` |
| Vende para pessoa física (hoje 2026) | Em 2026 a nota para pessoa física é dispensada. Avisar que **muda em 01/01/2027**: nota obrigatória, mas para PF sem CNPJ vale a DASN ou 1 nota consolidada por mês | — | 01/01/2027 | `00`, `06` ponto 1 |
| Quer 2º funcionário | Em 2026, 2 empregados desenquadram. A partir de 01/01/2027 pode ter até 2 | — | esperar 2027 | `00` |
| Quer virar ME | Passo a passo de sair do MEI; recomendar contador para a ME | Portal do Simples Nacional | 31/12/2026 para valer em 2027 | `02`, `00` |
| Tudo em dia | Dizer isso claramente e listar os próximos prazos: DAS dia 20, DASN 31/05 | — | — | `00` |

## Formato da resposta

```
Seu check-up (data de hoje)

🔴 Urgente
1. <pendência> — onde: <portal> — até: <data>

🟡 Logo
2. ...

🟢 Fique de olho
3. ...

Próximos prazos fixos: DAS todo dia 20; DASN até 31/05.
```

- No máximo 5 itens. Se houver mais, mostre os 5 mais graves e diga quantos faltam.
- Cada item tem uma frase de "por quê" com o link oficial que está na referência citada.
- Termine com **uma** ação para fazer agora (a primeira da lista), com o link.
- Se algum item depender de contador (regra 7 da skill), diga isso no próprio item.
- Não peça CPF, CNPJ, senha nem código de acesso. A pessoa consulta os portais sozinha e te conta o que viu.
