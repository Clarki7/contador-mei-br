# Use o Contador MEI BR no ChatGPT, no Gemini ou no Claude.ai

Não precisa instalar nada. Você cria um assistente seu, com as instruções e os arquivos oficiais deste projeto, em uns 5 minutos.

## Antes: baixe os arquivos (1 minuto)

1. Abra https://github.com/Clarki7/contador-mei-br
2. Clique em **Code** > **Download ZIP** e descompacte.
3. Você vai usar:
   - o texto de [`instrucoes.md`](instrucoes.md) (copiar e colar);
   - os arquivos de conhecimento: tudo da pasta `skills/contador-mei-br/referencias/` (9 arquivos `.md`) e `skills/contador-mei-br/dados/ocupacoes-mei.csv`. São 10 arquivos.

## ChatGPT (GPT personalizado)

Precisa de uma conta que possa criar GPTs.

1. Entre em https://chatgpt.com/gpts/editor (ou **Explorar GPTs** > **Criar**).
2. Abra a aba **Configurar**.
3. **Nome:** Contador MEI BR. **Descrição:** Orientação para MEI com a regra oficial e o link.
4. **Instruções:** cole todo o texto de `instrucoes.md`.
5. **Conhecimento:** envie os 10 arquivos.
6. Em **Recursos**, desligue a **Pesquisa na web** (a regra 3 manda usar só os arquivos conferidos).
7. Clique em **Criar** e escolha quem pode ver: só você, quem tiver o link, ou a loja de GPTs.

## Gemini (Gem)

1. Entre em https://gemini.google.com > **Gems** > **Novo Gem**.
2. **Nome:** Contador MEI BR.
3. **Instruções:** cole todo o texto de `instrucoes.md`.
4. **Conhecimento:** envie os 10 arquivos.
5. Clique em **Salvar**. Para compartilhar, use o botão de compartilhar do Gem.

## Claude.ai (Projeto)

1. Entre em https://claude.ai > **Projetos** > **Criar projeto**.
2. **Nome:** Contador MEI BR.
3. Em **Instruções do projeto**, cole todo o texto de `instrucoes.md`.
4. Em **Conhecimento do projeto**, envie os 10 arquivos.
5. Comece uma conversa dentro do projeto.

Quem usa o Claude.ai também pode enviar a skill completa como zip (veja o README). A skill tem o script de busca de ocupações; o Projeto não tem, mas procura direto na tabela.

## Teste rápido

Faça estas 3 perguntas e confira:

| Pergunta | Tem que responder |
|---|---|
| "Quanto é o DAS em 2026? Sou prestador de serviço." | R$ 86,05, vence dia 20, com link da Receita |
| "Tenho DAS atrasado de 2025, vou ser perdoado?" | Só a parte do INSS, automático em 01/01/2027, se pagar em dia jan–jun/2027 |
| "Meu MEI está em dia?" | Faz 5 perguntas numa mensagem só antes de responder |

Se errar, confira se os 10 arquivos subiram e se a pesquisa na web está desligada.

## Mantenha atualizado

As regras mudam. Quando o repositório tiver uma versão nova (veja a data em `referencias/00-resumo-por-ano.md`), baixe de novo e troque os arquivos no seu GPT, Gem ou Projeto.

## Calendário de prazos

Importe [`prazos-mei.ics`](prazos-mei.ics) no Google Agenda, no calendário do iPhone ou no Outlook:
- **Google Agenda (computador):** Configurações > Importar e exportar > Importar > escolha o arquivo.
- **iPhone:** abra o arquivo pelo app Arquivos ou pelo e-mail e toque em **Adicionar tudo**.
- **Outlook:** Arquivo > Abrir e exportar > Importar.

Ele traz: DAS todo dia 20 (com aviso 3 dias antes), DASN até 31/05, o prazo de 31/12/2026 para quem quer virar ME em 2027, o fim do edital da PGFN em 29/01/2027, a entrada do perdão de dívidas e da nota obrigatória em 01/01/2027, e o lembrete de pagar em dia o DAS de janeiro a junho de 2027 (condição do perdão).

Quando o dia 20 cair em fim de semana ou feriado, o DAS pode ser pago no próximo dia útil.
