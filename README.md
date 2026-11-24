# contador-mei-br

**Uma skill gratuita que faz o Claude orientar MEI com a regra oficial e o link de cada resposta.**

Milhões de brasileiros são MEI, e a maioria não tem contador. Quem trava numa tela do Portal do Empreendedor, recebe um boleto estranho ou quer saber se pode sair do MEI costuma achar respostas desencontradas, desatualizadas ou erradas. Esta skill junta as regras que mais se perguntam. Cada uma foi conferida em fonte oficial e leva o link, e as regras de 2026, 2027 e 2028 ficam separadas.

> **Aviso.** Isto é orientação, não é serviço de contabilidade. A skill não substitui um contador com registro no CRC. Quando o caso pede um profissional, ela diz isso.

## O que ela responde

- **Check-up do MEI:** você responde 5 perguntas e recebe as suas pendências em ordem de urgência, com onde resolver e até quando.
- **Passo a passo de tarefas:** gerar o DAS, débito automático, parcelar, dívida ativa no Regularize, entregar a DASN, emitir nota no Emissor Nacional, alterar dados, dar baixa.
- **Perdão de dívidas (LC 238):** quem tem direito, o que entra (só o INSS) e a condição de pagar em dia de janeiro a junho de 2027.
- **Ocupação e CNAE:** qual ocupação marcar, se a sua atividade cabe no MEI, e a lista oficial das 471 ocupações com busca.
- **Alterar dados:** onde trocar ocupação e endereço (Portal do Empreendedor, sem Junta Comercial).
- **DAS:** valores de 2026, vencimento, parcelamento e o que acontece se atrasar.
- **DASN-SIMEI:** prazo, o que informar e multa.
- **Nota fiscal:** quando é obrigatória, o que muda em 2027 (pessoa física, nota mensal consolidada) e IBS/CBS.
- **Imposto de renda, benefícios e sócio:** a conta da parte isenta do lucro, Bolsa Família, BPC, seguro-desemprego, sócio e se precisa de contador.
- **Teto e funcionários:** R$ 81 mil em 2026, R$ 110 mil em 2027, R$ 140 mil em 2028; 1 empregado em 2026 e até 2 a partir de 2027 (LC 238/2026).
- **Sair do MEI:** desenquadramento, virar ME, o que muda depois, e a mudança de prazo em 2027.
- **Baixa** do MEI e o que acontece com as dívidas.
- **INSS:** aposentadoria, auxílio, salário-maternidade e carência.
- **Golpes:** boletos de "associação" e mensagens falsas de cancelamento do CNPJ.

## Exemplo

> **Você:** Sou MEI motoboy, mas hoje faço sistemas e bots para empresas. Que ocupação eu coloco?
>
> **Claude (com a skill):** Não existe ocupação de software no MEI. O Anexo XI da Resolução CGSN 140 não traz nenhum CNAE de 6201 a 6209 ([lista oficial](https://www8.receita.fazenda.gov.br/simplesnacional/arquivos/manual/anexo_xi.pdf)). Enquanto for MEI, registre só o que você de fato faz e que está na lista. Para formalizar o software, o caminho é sair do MEI e virar ME. Atenção ao prazo: pela regra que entra em vigor em 01/01/2027, um pedido feito em janeiro só valeria em 2028. Por isso, quem quer ser ME já em 2027 precisa pedir até 31/12/2026, no Portal do Simples Nacional. (A regra nova foi lida numa cópia não oficial: confira no portal antes de pedir.)...

## Sem instalar nada: ChatGPT, Gemini e Claude.ai

Crie o seu assistente em 5 minutos colando as instruções e enviando os arquivos oficiais: veja [versoes-prontas/COMO-USAR.md](versoes-prontas/COMO-USAR.md).

**Calendário de prazos:** importe [versoes-prontas/prazos-mei.ics](versoes-prontas/prazos-mei.ics) no Google Agenda ou no celular (DAS todo dia 20, DASN até 31/05 e as datas de 2027).

## Como instalar

### Claude Code (recomendado)

```bash
claude plugin marketplace add Clarki7/contador-mei-br
claude plugin install contador-mei-br@contador-mei-br
```

Abra uma sessão nova e pergunte qualquer coisa sobre MEI. A skill entra sozinha.

### Cópia manual (Claude Code)

```bash
git clone https://github.com/Clarki7/contador-mei-br
cp -r contador-mei-br/skills/contador-mei-br ~/.claude/skills/
```

### Claude.ai ou app do Claude

1. Baixe a pasta `skills/contador-mei-br` e compacte em `.zip`.
2. Em **Configurações → Capacidades → Skills**, envie o arquivo.

### Outros agentes (Codex, Cursor, Gemini CLI e outros que leem SKILL.md)

```bash
npx skills add Clarki7/contador-mei-br
```

## Como ela evita erro

1. **Só afirma o que está nas referências.** Cada regra em `skills/contador-mei-br/referencias/` tem fonte oficial, data de acesso e nível de confiança (confirmado, parcial ou não confirmado).
2. **Separa MEI de ME.** Exemplo: no MEI se altera tudo pelo gov.br. Depois de sair do MEI, as alterações passam para a Junta Comercial.
3. **Separa por ano.** As regras de 2026, 2027 e 2028 ficam em `referencias/00-resumo-por-ano.md`.
4. **Avisa no caso cinza.** Para influenciador, infoproduto, afiliado ou dropshipping, ela diz que não há enquadramento oficial claro, em vez de inventar um CNAE.
5. **Tem casos de teste.** Veja `testes/casos.md`.

## Fontes

Todas foram conferidas em **23/11/2026**:
- Lei Complementar 123/2006
- Lei Complementar 238/2026, que mudou o teto e o número de empregados
- Resolução CGSN 140/2018 e seu Anexo XI, com as alterações das Resoluções CGSN 190, 195 e 196/2026
- Lei Complementar 214/2025 (reforma tributária) e Portaria Conjunta RFB/PGFN 740/2026 (perdão de dívidas)
- Portal do Empreendedor (gov.br)
- Portal do Simples Nacional
- Perguntas e Respostas do MEI (Receita Federal)
- INSS e Lei 8.213/1991
- Portal da NFS-e nacional

Quando o texto oficial não abriu e foi usada uma cópia, a referência diz isso.

## Ajude a manter atualizado

As regras do MEI mudam todo ano. Se achou algo desatualizado ou errado:

1. Abra uma [issue](https://github.com/Clarki7/contador-mei-br/issues) com o **link oficial** que mostra a regra certa.
2. Ou envie um pull request mudando a referência, com a fonte e a data de acesso.

Contadores que quiserem revisar o conteúdo são muito bem-vindos. O nome de quem revisar entra aqui.

## Próximos passos

- Conferir os pontos que ainda estão como "parcial" (regras do CGSIM, nota de produto por estado).
- Regras de prefeitura das maiores capitais.
- Atualização quando sair o salário mínimo de 2027 e a regulamentação da LC 238.

## Autoria

Projeto pessoal e independente de [Clarki7](https://github.com/Clarki7), feito para ajudar quem é MEI. Não é serviço de contabilidade e não tem ligação com nenhuma empresa. Licença MIT: use, copie e melhore.
