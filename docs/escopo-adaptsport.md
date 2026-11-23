# Escopo do projeto — AdaptSport

**Projeto/site:** AdaptSport — Esporte Adaptado e Saúde Inclusiva  
**Equipe:** Emily Mayara Matos Moreira; Kauã Gomes Da Silva; Lucas Gabriel Roman Martins; Lucas Ramon Bezerra Gomes; Gabriel Arnaldo Da Silva.  
**Professor/disciplina:** Paulo Sergio Fratta Junior — Desenvolvimento Front-end
**Data de referência do projeto original:** 21/09/2026  
**Versão final deste documento:** 16/11/2026

## Contexto e justificativa

O projeto aborda esporte adaptado, saúde inclusiva e acesso de pessoas com deficiência à informação e à prática esportiva. A proposta relaciona-se à sustentabilidade social por tratar de participação, acessibilidade, bem-estar e redução de barreiras. O tema se conecta aos ODS 3 (Saúde e Bem-estar), 10 (Redução das Desigualdades) e 11 (Cidades e Comunidades Sustentáveis). As relações são justificadas no conteúdo do site e em fontes do Ipea e da ONU.

O público inclui pessoas com deficiência interessadas em experimentar esporte, familiares, educadores, profissionais de saúde e educação física, clubes, núcleos e gestores. A informação não substitui contato direto com o serviço ou orientação profissional.

## Objetivo geral

Entregar dez páginas estáticas e interligadas sobre esporte adaptado e saúde inclusiva, responsivas e acessíveis, com informações atribuídas a fontes, conteúdo multimídia, interações em JavaScript e documentação de processo.

## Objetivos específicos e status

| Objetivo/critério | Status observado nesta versão |
| --- | --- |
| Manter as dez páginas do escopo do MVP e ligá-las por um menu funcional em todas. | Implementado nos arquivos HTML. |
| Apresentar esporte adaptado, modalidades, atletas, saúde, locais de prática, acessibilidade, depoimentos, envolvimento e contato. | Implementado conforme as dez páginas listadas abaixo. |
| Aplicar HTML semântico, CSS responsivo e identidade visual única. | Implementado; a verificação registrada aponta 10/10 páginas sem erros ou avisos no Nu HTML Checker. |
| Validar o formulário por JavaScript com `preventDefault`, mensagens de erro e destaque visual. | Implementado como demonstração local, sem envio para servidor. |
| Salvar e recuperar um rascunho de formulário e preferências com `localStorage`. | Implementado; o rascunho pode ser apagado pelo usuário. |
| Incorporar pelo menos uma interação de DOM acionada por evento. | Implementado: menu móvel, filtro, guia local e formulário. |
| Incluir notícias atribuídas, apoio/participação e multimídia útil. | Notícias do CPB na home, apoio com links oficiais e vídeo/áudio/iframe em Depoimentos e mídia. |
| Registrar fontes, escopo, orçamento, diário, testes, melhorias e uso de IA. | Documentos incluídos em `/docs`; testes finais e status de publicação detalhados separadamente. |
| Publicar todas as páginas por HTTPS e manter histórico GitHub com commits/PR. | Site publicado no GitHub Pages e histórico mantido no repositório; commits individuais e pull request ainda dependem da organização da equipe. |
| Entregar apresentação conforme o roteiro de 14 itens. | Apresentação com 12 lâminas cobrindo os 14 tópicos do roteiro, com roteiro de fala por integrante em `docs/roteiro-apresentacao.md`. |

## Arquitetura final de dez páginas

1. `index.html` — resumo, contexto, dado de impacto com fonte, ODS, notícias e mapa do site.
2. `modalidades.html` — catálogo de oito modalidades com filtro por JavaScript.
3. `esporte-adaptado.html` — conceito, diferença entre prática adaptada e programa paralímpico, participação.
4. `atletas.html` — trajetórias de atletas com perfis oficiais do CPB.
5. `beneficios-saude.html` — saúde, convivência e ressalvas.
6. `onde-praticar.html` — diretórios oficiais, Centros de Referência e perguntas antes da visita.
7. `acessibilidade.html` — acessibilidade física, digital e comunicação.
8. `depoimentos.html` — citações do CPB, narração local, vídeo com legendas, transcrição e iframe.
9. `envolva-se.html` — prática, voluntariado, compartilhamento e apoio sem arrecadação fictícia.
10. `contato.html` — formulário local de demonstração e contatos oficiais externos.

As notícias e multimídia requeridas pela rubrica foram incluídas dentro das páginas previstas no escopo, sem acrescentar uma décima primeira rota.

## Requisitos não funcionais

- HTML5 semântico, `lang="pt-BR"`, títulos únicos, navegação consistente e landmarks.
- CSS com variáveis, layout Flexbox/Grid e ajustes para telas pequenas.
- Foco visível, controles de teclado, botão de contraste, aumento de fonte, rótulos e mensagens acessíveis.
- Arquivos estáticos sem frameworks. O projeto funciona sem backend; o formulário não envia dados.
- Fontes e data de consulta apresentadas junto a dados e notícias.
- O site está publicado em hospedagem estática no GitHub Pages; não há domínio próprio configurado.

## Critérios de aceitação ainda recomendados

As etapas principais de conteúdo, código, documentação, versionamento e publicação foram concluídas. Antes da apresentação, recomenda-se revisar as evidências visuais, ensaiar a navegação por teclado, manter commits atribuídos às pessoas que realmente trabalharam e abrir um pull request se a equipe quiser demonstrar esse fluxo. A URL pública e o repositório confirmados estão em `url-site.txt` e `repositorio.txt`.
