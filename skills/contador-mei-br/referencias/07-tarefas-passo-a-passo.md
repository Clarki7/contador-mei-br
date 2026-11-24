# Tarefas do MEI: passo a passo oficial

Conferido em 24/11/2026. Marca: **C** = lido em página ou documento oficial; **P** = parcial (fonte oficial antiga, só parte da regra, ou divergência entre páginas oficiais); **N** = não achei em fonte oficial.

Siglas das fontes mais usadas (todas oficiais):
- **FAQ-PE**: Perguntas Frequentes do Portal do Empreendedor, modificada em 16/09/2025. https://www.gov.br/empresas-e-negocios/pt-br/empreendedor/perguntas-frequentes
- **Perguntão**: "Perguntas e Respostas MEI e Simei", CGSN, atualizado em 29/04/2025. https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/PerguntaoMEI.pdf
- **Manual PGMEI**: versão de 19/11/2025. https://www8.receita.fazenda.gov.br/simplesnacional/arquivos/manual/manual_pgmei_2018.pdf
- **Manual DASN**: atualizado em setembro de 2024. https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/Manual_DASN-SIMEI.pdf
- **Manual Débito Automático**: versão de março de 2024. https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/MANUAL_DEBITO_AUTO_MEI.pdf
- **P&R IRPF 2026**: Receita Federal, versão 1.00 de 23/04/2026. https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/perguntas-e-respostas/dirpf/p-r-irpf-2026-v1-00-2026-04-23.pdf
- **Guia Emissor NFS-e**: "Guia do Emissor Público Nacional Web", v1.2 de 27/07/2026. https://www.gov.br/nfse/pt-br/biblioteca/documentacao-tecnica/producao-restrita/guia_emissor_publico_nacional_web_snnfse-ern_versao_1-2-1.pdf

> **Perdão de dívidas (LC 238):** muda as tarefas 2, 3 e 8. A parte do INSS do DAS vencido até 13/10/2026 é perdoada de ofício em 01/01/2027, com a condição de pagar em dia jan–jun/2027 (Portaria Conjunta RFB/PGFN 740/2026). Ver `00-resumo-por-ano.md` e `06-conferencia-oficial-nov-2026.md`, ponto 5. **C**

---

## 1. Gerar e pagar o DAS (PGMEI, Pix, débito automático, App MEI)

**URL do serviço:** https://www.gov.br/pt-br/servicos/emitir-das-para-pagamento-de-tributos-do-mei (C)
- PGMEI simples (só o CNPJ): https://www8.receita.fazenda.gov.br/SimplesNacional/Aplicacoes/ATSPO/pgmei.app (C)
- PGMEI versão completa (mostra pendências e extrato): pelo Portal do Simples Nacional com código de acesso, ou pelo e-CAC com gov.br. https://cav.receita.fazenda.gov.br/autenticacao/login/index/10004 (C)
- App MEI: Google Play `br.gov.fazenda.receita.mei` e App Store `id1040521803` (C, links na mesma página de serviço)

**O que precisa para entrar** (Manual PGMEI, itens 1.1, 2.1 e 2.2) — C
- PGMEI simples: só o número do CNPJ, sem código de acesso.
- Versão completa pelo Portal do Simples: CNPJ, CPF do responsável e código de acesso. O código se gera em https://www8.receita.fazenda.gov.br/SimplesNacional/controleAcesso/GeraCodigo.aspx
- Versão completa pelo e-CAC: conta gov.br prata ou ouro, ou certificado digital. Com a conta gov.br da pessoa física, é preciso trocar o perfil para o CNPJ e abrir a aba "Simples Nacional".

**Passos** (Manual PGMEI, itens 2.1 e 4) — C
1. Abra o Portal do Simples Nacional, menu no canto superior esquerdo > Serviços Públicos > "PGMEI – Programa Gerador do DAS para o MEI".
2. Informe o CNPJ e clique em Continuar.
3. Clique em "Emitir Guia de Pagamento (DAS)".
4. Escolha o ano-calendário e clique em OK.
5. Marque o mês (período de apuração). Se esteve em benefício do INSS o mês inteiro, marque "Benefício INSS" e clique em "Atualizar Valores".
6. Clique em "Apurar/Gerar DAS" e depois em "Imprimir/Visualizar PDF".
7. Pague o boleto em banco, lotérica ou app do banco. A guia já sai com QR Code Pix ([Como pagar o DAS](https://www.gov.br/empresas-e-negocios/pt-br/empreendedor/servicos-para-mei/pagamento-de-contribuicao-mensal/como-pagar-o-das), C). Também dá para clicar em "Pagar Online": débito em conta só no Banco do Brasil, ou cartão de crédito com taxa (Manual PGMEI 4.6, C).

**Débito automático** (Manual Débito Automático; https://www.gov.br/pt-br/servicos/autorizar-debito-automatico-de-impostos-federais) — C
1. No Portal do Simples, entre nos serviços do MEI com código de acesso e clique em "Débito Automático". Também dá pelo e-CAC, em "Meus Débitos Automáticos".
2. Em "Inclusão", informe banco, agência, conta com dígito e se a conta é do CNPJ ou do CPF. Clique em "Incluir".
3. Anote o primeiro mês que será debitado: o sistema mostra essa informação na hora.
- A conta precisa estar num banco da rede arrecadadora. O manual lista 14 bancos.
- Pedir ou cancelar até 10 dias antes do vencimento vale no mesmo mês; depois disso, só no mês seguinte (manual). A página "Como pagar o DAS" diz "até o dia 10 do mês". **P (as duas páginas divergem)**
- Quem recebe benefício do INSS precisa marcar isso no PGMEI antes do débito, ou desativar o débito automático.

**Prazo:** dia 20 do mês seguinte; se não houver expediente bancário no dia 20, vale o próximo dia útil (Manual PGMEI 1.4). O DAS é devido mesmo sem faturamento e mesmo com o MEI parado (Perguntão 3.5; Manual PGMEI 4). — C

**Erros mais comuns** — C
- Pagar boleto ou Pix que chegou por mensagem ou ligação. A Receita só aceita guia gerada nos canais oficiais e não pede pagamento por telefone, e-mail ou mensagem ([alerta de out/2025](https://www.gov.br/receitafederal/pt-br/assuntos/noticias/2025/outubro/receita-federal-alerta-para-novo-golpe-envolvendo-transacoes-financeiras)).
- Pop-up bloqueado no "Pagar Online": a página do banco não abre e é preciso gerar outro DAS (Manual PGMEI 4.6).
- Marcar "Benefício INSS" num mês em que o benefício não cobriu o mês inteiro (Manual PGMEI 4.7).
- Tentar pagar no PGMEI um débito que já foi para a dívida ativa: o PGMEI não gera essa guia (Manual PGMEI 4.10).
- Página do Portal (2021): o DAS em atraso só é gerado depois de entregar as DASN pendentes ([O que você precisa saber sobre o DAS](https://www.gov.br/empresas-e-negocios/pt-br/empreendedor/servicos-para-mei/pagamento-de-contribuicao-mensal/o-que-voce-precisa-saber-sobre-o-das-1)). **P (página antiga)**

---

## 2. Ver DAS em atraso e parcelar na Receita (antes da dívida ativa)

**Onde ver os atrasos:** PGMEI versão completa > "Consulta Extrato/Pendências" > "Consulta Pendências no Simei" (FAQ-PE; Manual PGMEI 5.1). Ali também se gera o DAS. — C

**URL do parcelamento:** https://www.gov.br/pt-br/servicos/parcelar-imposto-mei (página modificada em 08/09/2026) — C
- e-CAC, "Meus Parcelamentos do MEI": https://cav.receita.fazenda.gov.br/autenticacao/login/index/134
- Portal do Simples: serviço "Parcelamento – Microempreendedor Individual" em https://www8.receita.fazenda.gov.br/SimplesNacional/Servicos/Grupo.aspx?grp=t&area=2

**O que precisa para entrar:** código de acesso do Portal do Simples ou certificado digital. O código do Simples não vale no e-CAC, e o do e-CAC não vale no Simples (Perguntão 4.2). — C

**Regras** — C, salvo onde indicado
- Até 60 parcelas, com parcela mínima de R$ 50 ([gov.br](https://www.gov.br/pt-br/servicos/parcelar-imposto-mei); Perguntão 4.4).
- Número de parcelas: a página gov.br de 2026 diz que **você escolhe**; o Perguntão de 2025 diz que **não escolhe** (o sistema calcula o máximo possível). **P (divergem; a página mais nova diz que escolhe)**
- **Exige a DASN entregue**: "Somente serão parcelados débitos já vencidos e declarados por meio da DASN Simei" (Perguntão 4.1, nota 1). A página "Como pagar o DAS" diz o mesmo.
- Entram no parcelamento todos os débitos em cobrança na Receita. A multa de mora entra no máximo de 20% (Perguntão 4.3).
- Só 1 parcelamento por ano-calendário. O pedido é confissão de dívida e só vale depois que a 1ª parcela é paga.
- Rescisão: 3 parcelas sem pagar, seguidas ou não, ou falta de pagamento da última parcela (gov.br). O Perguntão fala em "saldo devedor após o vencimento da última". Parcela paga em parte conta como não paga.
- Só vale para débitos ainda não enviados à dívida ativa. Depois do envio, o parcelamento é na PGFN (tarefa 3).

**Passos** (gov.br; Perguntão 4.2 e 4.5)
1. Entre em "Parcelamento – Microempreendedor Individual" pelo Portal do Simples ou pelo e-CAC. — C
2. Escolha a opção de pedir parcelamento e selecione os débitos. — C (a página não dá o nome exato do botão)
3. Preencha os dados pedidos e emita o DAS da 1ª parcela. — C
4. Pague a 1ª parcela até o vencimento. — C
5. A partir do dia 10 de cada mês, emita a parcela do mês no mesmo serviço e pague até o último dia útil do mês. O débito automático pode ser ligado no próprio serviço (Perguntão 4.5 e 4.6). — C

**Erros mais comuns:** não pagar a 1ª parcela, e o pedido fica sem efeito; tentar parcelar sem ter entregue a DASN; usar o código de acesso errado (Simples × e-CAC). — C

---

## 3. Dívida ativa: como saber, consultar e parcelar no Regularize (PGFN)

**Como saber se o débito foi para a dívida ativa** — C
- No PGMEI, ao escolher o ano, aparece uma mensagem com o mês, o tributo, o valor e o órgão que recebeu o débito. A mensagem continua aparecendo mesmo depois de regularizar (Manual PGMEI 4.10).
- No Regularize: "Consultar Dívida Ativa" ([serviço gov.br](https://www.gov.br/pt-br/servicos/consultar-debitos-inscritos-em-divida-ativa-da-uniao)).
- Quem cobra cada parte: o INSS vai para a PGFN, com 20% de encargos; o ICMS vai para o Estado e o ISS para o Município, cada um com guia própria (FAQ-PE; Manual PGMEI 4.10).

**URL:** https://www.regularize.pgfn.gov.br/ — C

**O que precisa para entrar:** o MEI deve entrar no Regularize **com o CNPJ, não com o CPF** ([página Regularize do Portal, 21/11/2024](https://www.gov.br/empresas-e-negocios/pt-br/empreendedor/servicos-para-mei/regularize)). — C. O nível da conta gov.br exigido: **N** (não achei em página oficial).

**Consultar** ([serviço gov.br](https://www.gov.br/pt-br/servicos/consultar-debitos-inscritos-em-divida-ativa-da-uniao)) — C
1. No Regularize, clique em "Consultar Dívida Ativa".
2. Abra a aba "Simples Nacional". Ela só aparece se houver inscrição dessa natureza.
3. Clique no número da inscrição para ver o relatório resumido ou o completo, que dá para exportar em PDF.

**Parcelar** ([serviço gov.br](https://www.gov.br/pt-br/servicos/parcelar-debitos-do-simples-nacional-inscritos-em-divida-ativa-da-uniao); FAQ-PE) — C
1. No Regularize: Negociar Dívida > Acesso ao Sistema de Negociações (SISPAR) > Simular/Negociar.
2. Escolha a natureza da dívida e selecione os débitos. A FAQ-PE indica a modalidade "Parcelamento Convencional" e "Parcelamento sem garantia – Simples Nacional".
3. Clique em Simular, escolha a opção e clique em "Adicionar à Carteira".
4. Vá em "Ir para a Carteira" > Negociar e confirme.
5. Para emitir a 1ª parcela: SISPAR > "Emissão de Documento". Pague até o vencimento.
6. Acompanhe em SISPAR > Consulta. O deferimento aparece em até 5 dias úteis depois do pagamento.

**Regras:** até 60 parcelas, parcela mínima de **R$ 300**, juros Selic e +1% no mês do pagamento. Rescinde com 3 parcelas sem pagar, ou até 2 se as demais estiverem pagas ou a última já tiver vencido. No reparcelamento, a entrada é de 10% ou 20%. — C para o Simples Nacional em geral. Se o mínimo de R$ 300 vale igual para o MEI: **P** (a página não trata o MEI separado).
- Transação com desconto hoje: a página gov.br/empresas-e-negocios (verificar-debitos-do-mei) informa o **Edital PGFN nº 6/2026**, adesão até 29/01/2027, até 133 parcelas, mínimo R$ 25 para o MEI, desconto de até 100% em juros, multas e encargo. **C na página; edital não lido** (ver `06`, ponto 5).

**Prazo:** a 1ª parcela até o vencimento do DAS de parcela. — C

**Erros mais comuns:** entrar com o CPF em vez do CNPJ; pagar a parcela de outro jeito que não seja o código de barras ("deve ser feito somente por meio da leitura ou digitação do código de barras", [serviço gov.br](https://www.gov.br/pt-br/servicos/parcelar-debitos-do-simples-nacional-inscritos-em-divida-ativa-da-uniao)); procurar no Regularize o ISS ou ICMS, que ficam com o Município ou o Estado. — C

---

## 4. Entregar a DASN-SIMEI e retificar

**URL:** https://www.gov.br/pt-br/servicos/declarar-receita-bruta-anual-para-o-mei — C
- Programa: https://www8.receita.fazenda.gov.br/SimplesNacional/Aplicacoes/ATSPO/DASNSIMEI.app/Default.aspx
- Também pelo App MEI, menu "Fazer a declaração" (Manual DASN, item 3).

**O que precisa para entrar:** só o CNPJ (Manual DASN, item 3). Para ver o recibo depois, pelo serviço "Consulta Declaração Transmitida", precisa do código de acesso (Manual DASN 4.6). — C

**Passos** (Manual DASN, itens 3 a 4.6) — C
1. Portal do Simples > menu > Serviços Públicos > "DASN SIMEI – Declaração Anual para o MEI". Ou, no app: "Fazer a declaração".
2. Informe o CNPJ e clique em Continuar.
3. Escolha o ano-calendário. É preciso declarar em ordem: o sistema não aceita um ano se o anterior estiver faltando.
4. Preencha os campos:
   - a) **Receita de comércio e indústria**: inclui transporte intermunicipal e interestadual e fornecimento de refeições;
   - b) **Receita de prestação de serviços**: inclui locação e demais receitas sem ICMS nem ISS;
   - c) **Receita bruta total**: o sistema soma sozinho;
   - d) **Possuiu empregado** no período: sim ou não.
   Se não teve receita num campo, informe zero.
5. Confira o resumo e clique em "Transmitir".
6. Imprima o recibo na hora. Se houver multa por atraso (MAED), a guia (DARF) sai junto.

**Retificar** (Manual DASN 4.2; FAQ-PE) — C
1. Mesmo programa; escolha o ano com a opção "AAAA – Retificar".
2. Digite **todos** os valores de novo: a retificadora não mostra o que foi declarado antes.
3. Transmita e imprima o recibo.
- Se o MEI corrigir o PGMEI depois de entregar a DASN, o sistema entrega sozinho uma "Retificadora Automática" (Manual PGMEI 4.8).

**Prazo** — C, com divergência
- Normal: até 31 de maio do ano seguinte, mesmo sem faturamento. O prazo não muda se cair em fim de semana ou feriado (Perguntão 3.9; serviço gov.br).
- Extinção (baixa): o Perguntão 3.9 e a FAQ-PE dizem até 30 de junho se a baixa for de janeiro a abril, e até o último dia do mês seguinte nos outros casos. A página de serviço gov.br diz "primeiros 3 meses" para o caso de junho. Outra resposta da FAQ-PE diz "até o último dia do mês de encerramento". **P (três versões oficiais)**
- Multa: 2% ao mês sobre os tributos declarados, limitada a 20%, com mínimo de R$ 50. Cai pela metade se entregar antes de intimação (Perguntão 3.10).

**Erros mais comuns:** pular um ano; deixar de imprimir o recibo na hora; somar comércio e serviço no mesmo campo; achar que, sem movimento, não precisa entregar. — C

---

## 5. Emitir NFS-e no Emissor Nacional (web e app)

**URLs:** https://www.gov.br/pt-br/servicos/emitir-nota-fiscal-de-servico-eletronica (C) e o emissor web https://www.nfse.gov.br/EmissorNacional (C). App: "NFS-e Mobile", na App Store e no Google Play (Nota Técnica 2023.001, C).

**Obrigação:** desde 01/09/2023, o MEI emite NFS-e só pelo Emissor Nacional (web, app ou API), não mais no sistema da prefeitura ([NT 2023.001](https://www.gov.br/nfse/pt-br/nt-2023-001-obrigatoriedade-da-nfs-e-nacional-para-o-mei.pdf)). — C

**O que precisa para entrar** (NT 2023.001, item 4) — C
- Conta gov.br do CPF do titular, **só prata ou ouro**. É o caminho recomendado.
- Ou usuário e senha criados em "Fazer primeiro acesso".
- Ou e-CNPJ, que é opcional. O certificado só é obrigatório para emitir por API.

**Primeiro acesso com usuário e senha** (Guia Emissor 1.1.1) — C
1. Em nfse.gov.br/EmissorNacional, clique em "Fazer primeiro acesso" e marque Pessoa Jurídica.
2. Informe o CNPJ, o CPF do responsável e a data de nascimento.
3. Informe o título de eleitor. Se declarou IRPF, informe também os números dos recibos dos 2 últimos anos.
4. Cadastre e-mail e senha e digite o código de segurança que chega por e-mail.

**Emitir (emissão simplificada do MEI)** (Guia Emissor 4.2; serviço gov.br) — C
1. Antes da primeira nota: menu "Configurações", informe e-mail e telefone e marque a exibição dos tributos aproximados.
2. Menu "Serviços Favoritos": crie o serviço com apelido, Código de Tributação Nacional, item da NBS e descrição.
3. Clique no ícone "+" > "Emissão Simplificada".
4. Preencha o identificador do cliente (CPF ou CNPJ do tomador), escolha o serviço favorito e informe o valor. Obra ou evento pedem dados a mais.
5. Clique em "Emitir NFS-e". Os tributos são calculados pelo sistema.
- No app: login com gov.br, escolha simplificada ou completa, CPF/CNPJ do cliente, serviço, valor, "Emitir" (serviço gov.br). Os menus do app não estão detalhados no material oficial: siga as telas. — P

**Cadastrar cliente:** o guia oficial não mostra uma tela de "cadastro de clientes". Na emissão simplificada, o cliente é informado em cada nota. **N**

**Cancelar** (Guia Emissor 5.3) — C
1. Abra a consulta de NFS-e emitidas e escolha a nota.
2. Clique em cancelar e informe o **motivo** (lista) e a **justificativa** (texto).
3. Se a regra do município não permitir o cancelamento direto, o sistema oferece transformar o pedido em "Solicitação de Cancelamento por Análise Fiscal".
- Prazo para cancelar: depende da regra do município; o guia não dá um número. **N**

**Erros mais comuns:** conta gov.br bronze, que não é aceita; tentar a emissão simplificada sem ter configurado os favoritos; emitir no site da prefeitura. — C

---

## 6. Nota de produto (NF-e) para MEI

**Fontes:** FAQ-PE; Perguntão 3.6 a 3.8; https://www.gov.br/empresas-e-negocios/pt-br/empreendedor/servicos-para-mei/nota-fiscal

- **Precisa emitir?** É obrigatório dar nota quando o cliente é empresa (CNPJ), salvo se ele emitir nota de entrada. Para pessoa física, só se ela pedir (FAQ-PE, com base no art. 106 da Res. CGSN 140). — C. **Vale até 31/12/2026**: a partir de 2027 a nota passa a ser obrigatória (ver `00` e `06`, ponto 1).
- **NF-e eletrônica:** "O MEI não tem a obrigação de emitir a Nota Fiscal Eletrônica – NF-e, mesmo se realizar vendas interestaduais, exceto se desejar" (FAQ-PE). O Perguntão (3.6, nota 1) também dispensa o MEI da emissão de NF-e. — C. Exceção estadual: a referência `03-tributos-obrigacoes.md` cita o art. 106 da Res. 140 (o Estado pode exigir se der sistema gratuito), mas essa leitura foi feita num espelho, não na fonte oficial. **P**
- **Inscrição estadual:** só serviço ou transporte municipal não precisa. Comércio, indústria e transporte intermunicipal ou interestadual, em regra, precisam de inscrição na Secretaria da Fazenda (SEFAZ) do Estado (FAQ-PE). — C
- **Certificado digital:** a FAQ-PE diz que, para nota em modelo eletrônico, o MEI não é obrigado a ter certificado (resposta sobre o MEI caminhoneiro). — P (o contexto é só o caminhoneiro)
- **Onde emitir:** procure a SEFAZ do seu Estado (FAQ-PE, resposta sobre o caminhoneiro). Emissor gratuito de NF-e por Estado: **N**
- Nota avulsa: pode, se a lei estadual ou municipal previr (Perguntão 3.8). — C

---

## 7. Alterar dados (ocupação, endereço, nome fantasia) e emitir o CCMEI

**URL:** https://www.gov.br/pt-br/servicos/solicitar-alteracao-cadastral-do-microempreendedor-individual e a página do Portal https://www.gov.br/empresas-e-negocios/pt-br/empreendedor/servicos-para-mei/atualizacao-cadastral-de-mei — C

**O que precisa:** conta gov.br **prata ou ouro** para brasileiro; estrangeiro com conta bronze informa os documentos da Polícia Federal. — C

**O que dá para mudar:** documento de identidade, telefones, e-mail, capital social, ocupações, forma de atuação, endereço comercial ou residencial. — C
- **Nome fantasia:** foi descontinuado no CNPJ do MEI em 15/11/2023; para marca, procure o INPI (FAQ-PE). — C
- **Nome empresarial:** não muda. É formado pelos 8 primeiros dígitos do CNPJ mais o nome do titular (FAQ-PE). — C

**Passos** (serviço gov.br; página do Portal) — C
1. Portal do Empreendedor > tema "Já sou MEI".
2. Card "Atualização Cadastral de MEI" > "Solicitar".
3. Entre com a conta gov.br.
4. Altere os dados, confira e marque as declarações.
5. Clique em "Continuar" ou "Finalizar".
6. Emita o CCMEI atualizado.

**CCMEI** ([Emissão de Comprovante (CCMEI)](https://www.gov.br/empresas-e-negocios/pt-br/empreendedor/servicos-para-mei/emissao-de-comprovante-ccmei), modificada em 26/10/2026) — C
- CCMEI completo: no Portal do Empreendedor, botão "Emissão de Comprovante (CCMEI)", ou no App MEI.
- "CCMEI Digital Simplificado", com QR Code: só no aplicativo da Receita Federal, opção "Emissão de CCMEI Digital Simplificado".

**Prazo:** não há prazo fixo; é gratuito; no máximo 2 alterações por dia, com até 8 campos por pedido (FAQ-PE). — C

**Erros mais comuns** — C
- Não avisar a prefeitura: os cadastros não são integrados, e ao mudar atividade ou endereço é preciso ver as exigências do município (FAQ-PE; página do Portal).
- Esperar que o DAS mude no mesmo ano: imposto e destino são definidos no primeiro DAS do ano, e a mudança só vale no DAS do ano seguinte (Manual PGMEI 1.3.1).
- Antes de mudar de cidade ou Estado, fazer a consulta prévia de endereço (FAQ-PE).

---

## 8. Baixar (encerrar) o MEI e o que acontece com as dívidas

**URL:** https://www.gov.br/pt-br/servicos/portal-do-empreendedor-quero-deixar-de-ser-mei e https://www.gov.br/empresas-e-negocios/pt-br/empreendedor/servicos-para-mei/baixa-de-mei — C

**O que precisa:** conta gov.br prata ou ouro. Quem se formalizou até 15/03/2022 pode usar conta bronze (página Baixa da Empresa). — C

**Passos** (serviço gov.br; página do Portal) — C
1. Portal do Empreendedor > "Já sou MEI" > card "Baixa de MEI" > "Solicitar baixa".
2. Entre com o gov.br, informe os dados e revise.
3. Marque a declaração de baixa e finalize.
4. Emita e guarde o comprovante de baixa. Mais tarde, a "Certidão de Baixa de Inscrição no CNPJ" sai no site de Comprovante de Inscrição e Situação Cadastral, opção "Deseja Emitir Certidão de Baixa" (FAQ-PE).
5. Pague os DAS em aberto pelo PGMEI.
6. Entregue a DASN-SIMEI de "Situação especial – Extinção" (prazo na tarefa 4).

**Dívidas** — C
- Pode dar baixa mesmo devendo; a dívida continua e pode ser cobrada do titular depois (FAQ-PE).
- A baixa não cancela o valor fixo devido no tempo em que foi MEI (Perguntão 3.5, nota 3).
- O DAS é devido até o mês da baixa, mesmo que ela seja no dia 1º (Manual PGMEI 1.4; FAQ-PE).
- Depois da baixa, não dá para reabrir o mesmo CNPJ; só abrir outro (FAQ-PE).
- Inscrições estadual e municipal: a página de serviço diz que a baixa do CNPJ **gera** a baixa delas e o cancelamento dos alvarás; a FAQ-PE diz que **não gera**. **P (divergência oficial)**

**Erros mais comuns:** achar que a baixa apaga as dívidas; esquecer a DASN de extinção, o que gera multa (MAED) na hora da entrega (FAQ-PE). — C

---

## 9. Imposto de renda da pessoa física do MEI

**Fonte principal:** P&R IRPF 2026, pergunta 184 (MEI) e pergunta 003. — C

**Lucro isento** (pergunta 184) — C
- É isento o lucro do titular, limitado a **receita bruta anual × percentual de presunção do art. 15 da Lei 9.249/1995**. Base citada: LC 123, art. 14; **Res. CGSN 140, art. 145**; IN RFB 1.500, art. 8º, I.
- O limite não vale se o MEI tiver escrituração contábil que mostre lucro maior.
- Não são isentos os valores de pró-labore, aluguéis ou serviços prestados.
- Exemplo oficial (comércio): receita de R$ 80.000 × 8% = **R$ 6.400 isentos**. O cálculo usa a receita bruta, não o lucro.
- Onde lançar: ficha "Rendimentos Isentos e Não Tributáveis", código **13**. A parte não isenta vai em "Rendimentos Tributáveis Recebidos de PJ pelo Titular".
- Novidade: a partir de janeiro de 2026, a resposta manda observar os arts. 6º-A e 16-A da Lei 9.250/1995. O efeito disso para o MEI **não está explicado** no documento. **P**

**Percentuais** ([P&R Pessoa Jurídica 2021, cap. XIII, pergunta 015](https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/declaracoes-e-demonstrativos/ecf/perguntas-e-respostas-pessoa-juridica-2021-arquivos/capitulo-xiii-irpj-lucro-presumido-2021.pdf)) — C, mas a versão é de 2021
- 8%: atividades em geral, incluindo comércio e indústria; também transporte de cargas.
- 16%: transporte, exceto o de carga (passageiros).
- 32%: prestação de serviços em geral.
- 1,6%: revenda de combustíveis (raro para MEI).
- O texto da Lei 9.249 não foi relido no planalto.gov.br, que não respondeu. **P quanto à lei; C quanto ao documento da Receita**

**Precisa declarar IRPF?** — C
- Ser MEI ou titular de empresa, por si só, não obriga (pergunta 003; Perguntão 3.6, nota 6).
- Exercício 2026 (ano-base 2025), alguns critérios da pergunta 001: rendimentos tributáveis acima de R$ 35.584; isentos acima de R$ 200.000; bens acima de R$ 800.000 em 31/12; receita rural acima de R$ 177.920; ganho de capital; bolsa acima de R$ 40.000. Há outros critérios na pergunta 001.

**Erro mais comum:** declarar todo o lucro como isento sem escrituração contábil, ou aplicar o percentual sobre o lucro em vez da receita bruta. — C

---

## 10. Benefícios do INSS e outros benefícios

**Fontes:** FAQ-PE (Previdência Social; seguro-desemprego; pontos de atenção); [notícia do INSS, atualizada em 28/10/2026](https://www.gov.br/inss/pt-br/noticias/o-que-voce-precisa-saber-sobre-a-aposentadoria-do-mei); [Solicitar salário-maternidade urbano](https://www.gov.br/pt-br/servicos/solicitar-salario-maternidade-urbano) (modificada em 19/08/2026).

**INSS** — C
- **Aposentadoria por idade:** 62 anos (mulher) e 65 (homem), com 180 meses de contribuição (mulher) e 240 (homem). Quem contribuía antes de 13/11/2019 tem regra de transição. O valor é de **1 salário mínimo** (notícia do INSS; FAQ-PE). Se a pessoa tiver outras contribuições além das do MEI, pode passar de 1 salário mínimo (FAQ-PE).
- **Aposentadoria por tempo de contribuição:** extinta pela EC 103/2019; só valem as regras de transição (FAQ-PE). Pela FAQ-PE não se confirma que o MEI fica fora delas pela alíquota de 5%. **P**
- **Auxílio por incapacidade temporária e aposentadoria por incapacidade permanente:** 12 meses de carência, em regra. Acidente ou doença da lista legal não exigem carência (FAQ-PE).
- **Salário-maternidade:** 120 dias. Carência de **10 meses** para contribuinte individual (serviço gov.br, 19/08/2026). Ver nota abaixo. **C**
- **Pensão por morte:** sem carência, a partir do primeiro pagamento em dia (FAQ-PE).
- **Auxílio-reclusão:** 24 contribuições (FAQ-PE).
- A carência só conta a partir do primeiro DAS **pago em dia**. A qualidade de segurado dura, em regra, até 12 meses depois da última contribuição (FAQ-PE).
- Quem recebe benefício por incapacidade ou salário-maternidade o mês inteiro não paga a parte do INSS no DAS desse mês, mas paga o ICMS e o ISS (FAQ-PE; Manual PGMEI 4.7).

> **Nota sobre a carência do salário-maternidade:** houve discussão no STF sobre essa carência. Não conferi em fonte oficial; a página do serviço ainda mostra 10 meses. **N**

**Outros benefícios** (FAQ-PE) — C
- **Bolsa Família:** ser MEI não cancela o benefício, a não ser que a renda familiar passe do limite do programa. Mesmo assim, o corte não é imediato: só no ano de atualização cadastral. Valores e duração da regra de proteção em página do MDS: **N**
- **BPC/LOAS:** não perde de imediato, mas o Serviço Social pode reavaliar se a renda familiar aumentar.
- **Seguro-desemprego:** quem já recebe e se formaliza "poderá ter a suspensão" numa resposta e "Não [perde]" em outra. Quem é MEI e é demitido sem justa causa da carteira assinada: uma resposta diz que tem direito se cumprir a Lei 7.998/1990; outra diz que não terá direito; e uma terceira diz que perde o direito se a DASN mostrar renda própria suficiente, com análise caso a caso. **P (a FAQ-PE se contradiz)**
- **Aposentadoria por invalidez e pensão de dependente inválido:** ao virar MEI, a pessoa é considerada recuperada e perde o benefício.
- **Auxílio-doença:** perde a partir do mês da formalização.
- **Carteira assinada e MEI ao mesmo tempo: pode** ("Não há impedimento", FAQ-PE). Mas o MEI não pode substituir um emprego com carteira: não pode ter pessoalidade, subordinação e habitualidade com o cliente (FAQ-PE; Perguntão 1.2).

---

## 11. Sócio, mais de um MEI, sócio de outra empresa

- **Pode ter sócio? Não.** "O MEI não pode ter sócios e também não pode ser sócio, titular ou administrador de outra empresa" (FAQ-PE). — C
- **Pode ser sócio de outra empresa? Não.** Requisito: "não participar de outra empresa como titular, sócio ou administrador" (Perguntão 1.2; Manual PGMEI 1.5). Isso gera desenquadramento (Perguntão 6.3). — C
- **Mais de um MEI? Não.** O requisito acima impede ser titular de outra empresa, e o MEI só pode ter um estabelecimento (Perguntão 1.2). Não achei uma frase oficial que diga literalmente "uma pessoa só pode ter um MEI". **P**
- LC 123, art. 18-A, § 4º: não relido nesta rodada (planalto.gov.br fora do ar daqui); a referência `02-ciclo-de-vida.md` já o resume. **P**

---

## 12. Precisa de contador?

- **Não.** "O MEI não é obrigado contratar um contador ou manter a contabilidade formal. Também não é preciso ter livro caixa." Mas deve preencher todo mês o Relatório Mensal das Receitas Brutas (FAQ-PE, pergunta "Preciso ter contabilidade?"). — C
- Também não precisa de contador para contratar o empregado (FAQ-PE). — C
- O MEI é dispensado de escrituração fiscal e contábil (Perguntão 3.6, nota 1). — C

---

## Lista do que ficou N
1. Regularize: nível da conta gov.br exigido para entrar.
2. ~~Transação PGFN em vigor~~: resolvido em `06` (Edital PGFN 6/2026).
3. NFS-e: tela de "cadastro de clientes" no Emissor Nacional (o guia não mostra).
4. NFS-e: prazo para cancelar (depende do município; o guia não dá número).
5. NF-e: emissor gratuito por Estado e onde emitir em cada SEFAZ.
6. Salário-maternidade: efeito da discussão no STF sobre a carência de 10 meses.
7. Bolsa Família: faixa e duração da regra de proteção em página do MDS.

## Divergências entre páginas oficiais (marcadas P)
- Parcelamento: escolher ou não o número de parcelas (gov.br 2026 × Perguntão 2025).
- Débito automático: "10 dias antes do vencimento" (manual) × "até o dia 10" (Portal).
- DASN de extinção: "jan–abr → junho" × "primeiros 3 meses" × "até o fim do mês do encerramento".
- Baixa: "gera" × "não gera" a baixa das inscrições estadual e municipal.
- Seguro-desemprego de quem é MEI e tem carteira assinada: a FAQ-PE se contradiz.

## Fontes que não abriram daqui
- planalto.gov.br (Lei 9.249, LC 123, Leis 8.212, 8.213, 8.742 e 14.601): conexão recusada. Sem a releitura literal dos artigos de lei.
- gov.br/nfse "links com passo a passo" (404) e a FAQ NFS-e v1.4 em PDF (o servidor devolveu uma página HTML).
