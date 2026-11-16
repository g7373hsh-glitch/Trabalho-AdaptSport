# Diário de bordo — AdaptSport

## 09/11/2026 — Auditoria do MVP e dos critérios

Foram lidos o enunciado da segunda entrega, a rubrica, o escopo `escopo-adaptsport.docx` e os arquivos HTML, CSS e JavaScript existentes. O MVP continha `index.html` e `modalidades.html`, embora o escopo já previsse dez páginas. O menu tinha somente duas rotas e o rodapé identificava a entrega como MVP. O formulário e a publicação ainda não existiam.

**Prompt/resumo de trabalho assistido por IA:** continuar a versão `adaptsport-mvp` conforme o enunciado e a rubrica, manter o escopo e a identidade do projeto, produzir as oito páginas restantes, implementar as interações exigidas e documentar o que não pode ser confirmado.

**Aceito:** preservar a paleta verde/laranja, tipografia, marca e tema social; usar HTML/CSS/JavaScript sem framework; manter as dez páginas específicas do escopo; criar conteúdo multimídia acessível e referências citadas.

**Revisado/corrigido:** o projeto não recebeu feedback formal da primeira avaliação, então não foi inventada uma lista de comentários do professor. As melhorias foram descritas comparando limitações observáveis no MVP e no escopo recebido.

## 09/11/2026 — Conteúdo e dados

Os números “24 modalidades”, “+400 atletas” e “3 em cada 4 brasileiros com deficiência nunca praticaram esporte”, que apareciam na home original sem fonte no arquivo, foram removidos. A home passou a citar o IBGE: 14,4 milhões (7,3%) de pessoas com deficiência com 2 anos ou mais no Censo 2022, com link para a publicação oficial. A informação foi atribuída ao IBGE e contextualizada como dado populacional, não como descrição de experiências individuais.

Foram consultados os perfis oficiais do CPB para Carol Santiago e Petrúcio Ferreira, os diretórios oficiais para clubes e Centros de Referência, notícias do CPB, páginas do Ipea sobre ODS e material da ONU sobre deficiência e desenvolvimento sustentável. As fontes e datas estão em `fontes-e-referencias.md`.

## 09/11/2026 — Implementação e IA

As páginas foram geradas por `scripts/build_pages.py`, com menu comum e `aria-current="page"`. `assets/app.js` implementa menu móvel, filtro de modalidades, guia local e validação do formulário. `assets/a11y.js` mantém preferências de fonte/contraste.

O guia rápido da home responde a palavras-chave usando regras e textos fixos. Essa escolha foi feita para não fingir uma conexão generativa sem backend nem credenciais. O guia não recebe nem armazena perguntas. As regras, fontes, limites e um plano para eventual IA futura estão em `plano-contexto-ia.md`.

O formulário demonstra validação, destaque e armazenamento temporário de rascunho no dispositivo. A mensagem final informa que nenhum dado foi enviado. A ausência de backend foi mantida explícita para não induzir visitantes a acreditar que há atendimento real.

A seção multimídia inclui narração sintética em português brasileiro, transcrição, vídeo local com faixa de legendas e iframe externo do CPB. A narração apresenta esporte adaptado sem imitar a voz de pessoa real ou oferecer aconselhamento médico.

## 09/11/2026 — Limites externos

O ZIP original não continha repositório Git, URL, credenciais de publicação, RAs dos integrantes nem divisão de papéis. Nenhum GitHub, serviço de hospedagem, domínio, site público ou participação individual foi inventado. A documentação marca essas etapas como pendentes e fornece instruções para a equipe concluí-las.

A rubrica pede 14 slides, mas o limite de criação disponível nesta sessão é 12. A apresentação foi planejada com 12 slides que agrupam os 14 tópicos; o arquivo de apresentação deve informar essa condensação. A equipe pode complementar/editar o deck se precisar cumprir literalmente 14 lâminas.

## Revisão da equipe antes de apresentar

Os integrantes devem revisar os textos e explicar cada função JavaScript, testar o formulário com erro e sucesso, verificar o rascunho local e navegar com teclado. Também devem confirmar RAs e tarefas reais, atualizar os links de publicação/repositório e corrigir qualquer divergência encontrada no W3C Validator.
