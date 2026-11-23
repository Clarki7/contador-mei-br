# MEI: ocupações permitidas, vedações e CNAE (regras com fonte)

Pesquisa feita em 23/11/2026. Marcação: **[OFICIAL]** = lido em fonte oficial; **[ESPELHO]** = texto consolidado de site secundário que reproduz a norma (usado só para conferir); **[NÃO CONFIRMADO]** = não achei fonte oficial.

## 1. Versão vigente do Anexo XI

- Texto vigente: Anexo XI da Res. CGSN 140/2018, na redação da Res. CGSN 165/2022, publicado pela Receita em PDF. **[OFICIAL]**
  - PDF: https://www8.receita.fazenda.gov.br/simplesnacional/arquivos/manual/anexo_xi.pdf
  - Norma: https://normas.receita.fazenda.gov.br/sijut2consulta/link.action?idAto=92278
- Conteúdo: Tabela A (ocupações em geral) + Tabela B (transportador autônomo de carga). Extraí **471 linhas ocupação x CNAE, 470 ocupações, 351 CNAEs distintos** para `../dados/ocupacoes-mei.csv`.
- Conferência cruzada: o texto consolidado do LegisWeb (https://www.legisweb.com.br/legislacao/?id=360430) **[ESPELHO]** tem as mesmas 471 linhas, com os mesmos CNAE, ISS e ICMS.
- Alteração recente do Anexo XI: a única anotada depois de 2022 é a linha **MOTORISTA (POR APLICATIVO OU NÃO) INDEPENDENTE, CNAE 4923-0/02**, com "redação dada pela Res. CGSN 182, de 26/09/2025" **[ESPELHO]**. O PDF da Receita já traz essa linha. Não li o texto da Res. 182 em si.
- Não houve inclusão nem exclusão de ocupações em 2026 nas fontes que achei. Resoluções de 2025 e 2026 mexem em outros pontos:
  - Res. CGSN 183/2025 (DOU 13/10/2025): trata de IBS/CBS, DASN-Simei e outros artigos; no art. 100 mudou só o § 9º. Nada no Anexo XI. https://www.normasbrasil.com.br/norma/resolucao-183-2025_484849.html **[ESPELHO]**
  - Res. CGSN 190, de 04/08/2026, com efeitos a partir de **01/01/2027**: revoga os incisos II e III do art. 101 (ICMS R$ 1,00 e ISS R$ 5,00 fixos) e cria os incisos IV e V (IBS e CBS, e ICMS e ISS, nos valores do novo Anexo XIII). **[ESPELHO]** Isso muda o significado das colunas `iss` e `icms` do CSV a partir de 2027: elas dizem se a ocupação é contribuinte de ISS e/ou ICMS, e o valor fixo passa a vir do Anexo XIII. Passar para a frente de tributos.
- Boato a ignorar: "13 atividades excluídas do MEI em 2026 pela Res. 183/2025" (blog Treeunfe). Não achei isso no texto da Res. 183 nem no Anexo XI. **[NÃO CONFIRMADO]**
- Boato de fev/2025 de que o INSS tirou atividades da lista: a Fenacon registra que é falso e que o órgão competente é o CGSN. https://fenacon.org.br/noticias/inss-nao-exclui-atividades-de-lista-do-mei/ **[ESPELHO]**
- A página oficial "Quais as ocupações que podem ser MEI" tem última modificação em 09/10/2026. https://www.gov.br/empresas-e-negocios/pt-br/empreendedor/quero-ser-mei/quais-as-ocupacoes-que-podem-ser-mei **[OFICIAL]**
- A lista alfabética oficial por letra fica em https://www.gov.br/empresas-e-negocios/pt-br/empreendedor/quero-ser-mei/atividades-permitidas (páginas por letra, últimas modificações de 2021; usar o PDF da Receita como referência).

## 2. Regras

| Regra | Conteúdo | Fonte |
|---|---|---|
| Quantas ocupações | 1 principal + até **15 secundárias** (total de 16). | Portal do Empreendedor: "é possível escolher 1 ocupação como principal e outras 15 ocupações secundárias". https://www.gov.br/empresas-e-negocios/pt-br/empreendedor/quero-ser-mei/quais-as-ocupacoes-que-podem-ser-mei **[OFICIAL]**. Não está no texto da Res. 140 (busquei "secundária": zero ocorrências). |
| Só o que exerce | A ocupação é a atividade "exercida pelo MEI na prática"; o portal manda conferir se a descrição é exatamente o que você faz ou fará, pois ela define impostos e exigências municipais. Não registre CNAE "de reserva". | Mesma página do portal **[OFICIAL]**. Base normativa: Res. CGSN 140, art. 100, caput ("exerça ... apenas as ocupações constantes do Anexo XI") e § 1º-C, I. |
| Só ocupação do Anexo XI | É vedado ao MEI exercer ocupação não prevista no Anexo XI. Outras vedações do § 1º-C: mais de um estabelecimento; participar de outra empresa como titular, sócio ou administrador; startup; mais de um empregado (art. 105); cessão ou locação de mão de obra. | Res. CGSN 140, art. 100, § 1º-C, I a VI (redação da Res. 165/2022; inciso IV pela 171/2022). Norma: https://normas.receita.fazenda.gov.br/sijut2consulta/link.action?idAto=92278 ; conferido no espelho LegisWeb. |
| Independência | "Independente" = sem pessoalidade, subordinação e habitualidade cumulativas com o contratante; se houver, exclusão do Simples. | Res. CGSN 140, art. 100, §§ 4º e 8º. |
| Critérios para entrar na lista | Para uma atividade ser incluída no Anexo XI ela não pode estar tributada pelo Anexo V (art. 25, § 1º, V), deve caber em até 2 pessoas, em um único estabelecimento, sem fragilizar relações de trabalho. | Res. CGSN 140, art. 100-A (incisos II a VIII; I não aparece no espelho). |
| Atividades intelectuais e serviços "Anexo V" | A lista do Anexo V inclui, entre outras: tradução e interpretação; arquitetura; engenharia, suporte e análises técnicas e tecnológicas, pesquisa e **design**; representação comercial e intermediação de negócios e serviços de terceiros; **consultoria**, gestão, organização, administração; **jornalismo e publicidade**; **agenciamento**; e a cláusula geral de atividade intelectual, técnica, científica, desportiva, artística ou cultural, regulamentada ou não. Como a ocupação do MEI precisa estar no Anexo XI e os critérios do art. 100-A afastam o Anexo V, essas atividades não cabem no MEI. | Res. CGSN 140, art. 25, § 1º, V, alíneas "p" a "x" (lista lida no espelho LegisWeb) e art. 100-A, VI. Base de lei: LC 123/2006, art. 18, § 5º-I (https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp123.htm — não consegui abrir o site do Planalto; citado via Res. 140). |
| Profissões regulamentadas | Não há uma regra geral "regulamentada = proibida". O que vale é a lista fechada do Anexo XI. Profissões de saúde (medicina, odontologia, psicologia, fisioterapia, nutrição etc.), jurídicas, engenharia, arquitetura, contábeis estão na lista do Anexo V e não constam no Anexo XI. Exceção que existe no Anexo XI: cuidador de idosos e enfermos (8712-3/00), por exemplo. | Res. CGSN 140, art. 25 § 1º V; Anexo XI. |
| Software | **Desenvolvimento de software, programas sob encomenda, licenciamento e SaaS (CNAE 6201-5, 6202-3, 6203-1, 6204-0, 6209-1) não constam no Anexo XI.** Verifiquei por CNAE e por palavra no CSV. Nenhuma ocupação do Anexo XI cobre programar, consultar em TI ou hospedar sistema. | Anexo XI (PDF da Receita). |
| Startup | Constituir-se sob a forma de startup é vedado ao MEI, mesmo sob o rito do art. 65-A da LC 123. | Res. CGSN 140, art. 100, § 1º-C, IV. |
| Limite de receita | R$ 81.000,00 por ano (R$ 6.750,00 por mês de atividade no 1º ano); transportador autônomo de cargas: R$ 251.600,00. | Res. CGSN 140, art. 100, caput e §§ 1º e 1º-A. (A frente de tributos detalha.) |

## 3. Ocupações de informática e tecnologia que existem no Anexo XI

Todas em `../dados/ocupacoes-mei.csv`. Em ISS/ICMS, S = contribuinte, N = não.

| Ocupação | CNAE | ISS | ICMS |
|---|---|---|---|
| Técnico(a) de manutenção de computador | 9511-8/00 | S | N |
| Técnico(a) de manutenção de telefonia | 9512-6/00 | S | N |
| Instalador(a) de rede de computadores | 6190-6/99 | S | N |
| Instrutor(a) de informática | 8599-6/03 | S | N |
| Digitador(a) | 8219-9/99 | S | N |
| Comerciante de equipamentos e suprimentos de informática | 4751-2/01 | N | S |
| Recarregador(a) de cartuchos para equipamentos de informática | 4751-2/02 | S | S |
| Comerciante de equipamentos de telefonia e comunicação | 4752-1/00 | N | S |
| Proprietário(a) de sala de acesso à internet (lan house) | 8299-7/07 | S | N |
| Locador(a) de vídeo games | 7722-5/00 | N | N |
| Locador(a) de aparelhos de jogos eletrônicos | 7729-2/01 | N | N |
| Editor(a) de lista de dados e de outras informações | 5819-1/00 | S | N |
| Editor(a) de vídeo | 5912-0/99 | S | N |

Não existem no Anexo XI: programador, desenvolvedor, analista de sistemas, web designer, designer gráfico, gestor de redes sociais, consultor de TI, suporte remoto de software, hospedagem, agência de marketing.

## 4. Ocupações retiradas (histórico)

- **Nada foi retirado do Anexo XI em 2026** nas fontes consultadas.
- **Dez/2019:** a Res. CGSN 150, de 03/12/2019, excluiu 14 ocupações do MEI (entre elas astrólogo, cantor/músico, DJ/VJ, esteticista, e três CNAEs de desenvolvimento de software do Anexo VII). A Res. CGSN 151, de dezembro/2019, **revogou** a 150 poucos dias depois. Por isso **cantor(a)/músico(a) (9001-9/02) e DJ/VJ (9001-9/06) continuam no Anexo XI**; conferi no PDF atual. Fonte: Contábeis, 12/12/2019 https://www.contabeis.com.br/noticias/41620/resolucao-que-excluia-14-atividades-do-mei-e-revogada/ **[ESPELHO / notícia]**. Não li as Res. 150 e 151 no site oficial.
- **Personal trainer** (CNAE 9313-1/00): foi incluído em 2014 e saiu do MEI com efeitos desde 01/01/2018. Não consta no Anexo XI atual (conferi no CSV). A resolução que o tirou é citada de forma divergente nas fontes (137/2017 em uma). **[NÃO CONFIRMADO em fonte oficial]**. Fonte secundária: https://tactus.com.br/personal-trainer-pode-ser-mei/amp/
- Portanto, "retiradas recentemente" (personal trainer, DJ, cantor) não procede: personal trainer saiu em 2018; DJ e cantor continuam permitidos.

## 5. Pendências

- Texto oficial da Res. CGSN 182/2025 (linha do motorista) e das Res. 150/151 de 2019 não lido.
- Site do Planalto (LC 123/2006) não abriu para mim; os artigos da lei foram citados a partir das remissões da Res. 140.
- Se o portal tiver FAQ oficial específico sobre "vender pela internet" ou sobre infoprodutos, não achei; ver o mapa em `05-ocupacoes-mapa.md`.
