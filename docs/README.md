# AdaptSport — documentação da entrega final

**Disciplina:** Desenvolvimento Front-end para Web — UNICID  
**Projeto:** AdaptSport — Esporte Adaptado e Saúde Inclusiva  
**Equipe:** Emily Mayara Matos Moreira; Kauã Gomes Da Silva; Lucas Gabriel Roman Martins; Lucas Ramon Bezerra Gomes; Gabriel Arnaldo Da Silva.  
**Data da versão:** 16/11/2026.  
**Professor informado no escopo:** Paulo Fratta.

## Objetivo

O AdaptSport é um projeto acadêmico de informação sobre esporte adaptado, saúde inclusiva e acessibilidade. A versão final mantém o tema e a arquitetura de dez páginas do escopo original. O site não se apresenta como ONG registrada, não possui parcerias próprias, não recebe doações e não envia mensagens para uma equipe.

## Páginas

| Arquivo | Conteúdo |
| --- | --- |
| `index.html` | Apresentação, dado do IBGE com fonte, ODS 3/10/11, notícias atribuídas ao CPB e guia rápido local. |
| `modalidades.html` | Oito modalidades e filtro por texto com JavaScript. |
| `esporte-adaptado.html` | Conceitos, adaptação, participação e barreiras. |
| `atletas.html` | Perfis de Carol Santiago e Petrúcio Ferreira, com fontes oficiais do CPB. |
| `beneficios-saude.html` | Bem-estar, convivência e ressalvas de saúde. |
| `onde-praticar.html` | Passos e links oficiais para procurar clubes e Centros de Referência. |
| `acessibilidade.html` | Checklist para espaços esportivos e recursos digitais do site. |
| `depoimentos.html` | Citações atribuídas ao CPB, vídeo MP4 local com legenda, áudio MP3 com transcrição e iframe externo do CPB. |
| `envolva-se.html` | Prática, voluntariado e apoio transparente a iniciativas oficiais. |
| `contato.html` | Formulário de demonstração com validação em JavaScript e rascunho local. |

As notícias ficam na página inicial e os três formatos de mídia ficam em `depoimentos.html`, sem criar páginas extras além das dez estabelecidas no escopo AdaptSport.

## Como abrir e regenerar

O site é estático: basta abrir `index.html` em um navegador ou servir a pasta por HTTP. Para evitar restrições de origem de mídia, prefira um servidor local:

```bash
python3 -m http.server 8000
```

Depois abra `http://localhost:8000`. Não há framework, dependência de banco de dados nem pacote JavaScript externo.

As dez páginas HTML são geradas por `scripts/build_pages.py`, que contém o conteúdo e o menu compartilhado. Execute `python3 scripts/build_pages.py` após editar esse arquivo. O áudio-base `assets/guia-esporte-adaptado.wav`, as ferramentas FFmpeg e Pillow são usados por `scripts/build_media.py` para reconstruir os arquivos em `assets/media/`.

## JavaScript e dados

`assets/a11y.js` guarda somente preferências de fonte e contraste em `localStorage`. `assets/app.js` contém o menu móvel, filtro de modalidades, guia de respostas fixas e formulário. O formulário intercepta `submit` com `preventDefault()`, verifica campos, mostra mensagens e destaca erros. O rascunho fica neste navegador e pode ser apagado pelo controle disponível. Mesmo quando tudo está válido, o site informa que nada foi transmitido, pois não existe backend.

O guia rápido é baseado em regras e respostas pré-escritas, sem IA generativa e sem serviço remoto. O plano de contexto e limites para eventual IA futura está em `docs/plano-contexto-ia.md`.

## Acessibilidade e conteúdo

O site declara `lang="pt-BR"`, usa landmarks semânticos, link para pular para o conteúdo principal, foco visível, navegação móvel por teclado, rótulos de formulário, estados ARIA quando necessários, alternativa textual da ilustração, transcrição de áudio e faixa de legenda para o vídeo local. A página `acessibilidade.html` reúne as medidas e o checklist de uso.

Números, perfis e notícias têm fonte junto ao conteúdo e em `docs/fontes-e-referencias.md`. O material é informativo e não substitui avaliação ou orientação profissional.

## Publicação, URL e GitHub

**URL HTTPS publicada:** ainda não configurada — o site ainda não foi publicado.  
**Repositório GitHub:** https://github.com/g7373hsh-glitch/Trabalho-AdaptSport  

O repositório informado pela equipe é `https://github.com/g7373hsh-glitch/Trabalho-AdaptSport`. A publicação HTTPS, os commits reais de cada integrante e o pull request ainda precisam ser confirmados. As instruções de publicação estão em `docs/guia-publicacao-github-pages.md`; custos e comparação estão em `docs/orcamento-hospedagem.md`. Os arquivos `url-site.txt` e `repositorio.txt` na raiz registram esses campos sem inventar endereços.

## Integrantes, RAs e papéis

A equipe confirmada nesta versão é composta por cinco integrantes: Emily Mayara Matos Moreira (RA 47323523), Kauã Gomes Da Silva (RA 47262265), Lucas Gabriel Roman Martins (RA 46487618), Lucas Ramon Bezerra Gomes (RA 47766362) e Gabriel Arnaldo Da Silva (RA 47480441). As responsabilidades confirmadas são, respectivamente, conteúdo e pesquisa; HTML e páginas; testes e acessibilidade; CSS e responsividade; documentação e apresentação. A lista completa está em `integrantes.txt`.

## Arquivos de documentação

- `apresentacao-adaptsport.pdf` e `apresentacao-adaptsport.pptx` (na raiz do projeto) — deck da Atividade 2, com 12 lâminas cobrindo os 14 tópicos do roteiro.
- `docs/roteiro-apresentacao.md` — divisão dos tópicos entre os slides, tempo e roteiro da demonstração.
- `docs/escopo-adaptsport.md` — objetivos, requisitos e status planejado × entregue.
- `docs/diario-de-bordo.md` — registro datado de decisões, uso de IA e ajustes.
- `docs/orcamento-hospedagem.md` — comparação de provedores e domínios.
- `docs/orcamento_hospedagem.html` — versão navegável da comparação de hospedagem.
- `docs/evidencias-de-testes.md` — testes e verificações executados, com limites conhecidos.
- `docs/melhorias-do-mvp.md` — antes e depois, sem inventar comentários do professor.
- `docs/plano-contexto-ia.md` — limites e fontes para um futuro assistente generativo.
- `docs/guia-publicacao-github-pages.md` — passos para versionar e publicar após definir a conta/repositorio.
- `docs/fontes-e-referencias.md` — referências consultadas.
- `docs/evidencias/` — capturas de tela e cópia do MVP original.
