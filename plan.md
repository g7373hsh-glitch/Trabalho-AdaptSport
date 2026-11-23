# Plano técnico — AdaptSport (continuação do MVP)

## Objetivo e implementação

Continuar o projeto recebido em HTML5/CSS3/JavaScript puros, sem framework e sem backend. Manter a marca AdaptSport, a paleta verde/laranja, tipografia Space Grotesk/Work Sans e o recorte esporte adaptado e saúde inclusiva. Completar as oito páginas planejadas e preservar `index.html` e `modalidades.html` como rotas iniciais, atualizando conteúdo, navegação e interações.

As páginas são documentos estáticos independentes. `scripts/build_pages.py` centraliza menu, rodapé e conteúdo e gera as dez páginas HTML, cada uma com metadados, `aria-current`, landmarks e conteúdo próprio. O CSS em `assets/style.css` fornece variáveis e componentes comuns, com CSS Grid/Flexbox e breakpoints. O JavaScript fica em `assets/app.js` e `assets/a11y.js`. A versão de contato é deliberadamente demonstrativa: valida localmente, armazena o rascunho apenas no navegador e informa que não envia dados.

O site incorpora notícias externas atribuídas, fontes junto a estatísticas/perfis, controle de preferências, filtro de modalidades, guia de navegação local, mídia acessível e documentação. As respostas do guia são fixas e baseadas em regras; nenhuma API generativa ou credencial é incorporada ao front-end.

## Estrutura e responsabilidades

- `index.html` … `contato.html`: dez páginas estáticas, todas usando o mesmo CSS e scripts.
- `assets/style.css`: tokens visuais, responsividade, foco e componentes.
- `assets/app.js`: menu, filtro, guia e formulário.
- `assets/a11y.js`: fonte e contraste, com persistência local.
- `assets/media/`: MP3, MP4, poster e arquivo WebVTT.
- `assets/guia-esporte-adaptado.wav`: fonte de áudio para regenerar MP3/vídeo.
- `scripts/build_pages.py`: gerador das dez páginas; editar conteúdo aqui e gerar de novo.
- `scripts/build_media.py`: ferramenta de regeneração do áudio/vídeo, requer FFmpeg e Pillow.
- `docs/`: escopo, fontes, orçamento, diário, plano de contexto, testes, antes/depois e passos de publicação.
- `integrantes.txt`, `url-site.txt`, `repositorio.txt`: entregáveis textuais com os integrantes, a URL pública e o repositório confirmados.

## Design reutilizado

A identidade aprovada pelo MVP é mantida: estética esportiva editorial, verde como cor de ação e associação à saúde, laranja como energia visual, fundo claro, cartões e navegação com foco visível. O cabeçalho de duas páginas foi reorganizado para comportar dez rotas em desktop e menu expansível no celular, sem alterar a marca. O conteúdo usa desenho SVG próprio e texto; nenhum retrato de pessoa real foi inventado ou copiado.

## Dependências e entrega

A aplicação não requer backend para navegar. A mídia é local, exceto o iframe do CPB e os links para fontes oficiais, que exigem Internet. O formulário não pode encaminhar contato sem integração com serviço/servidor e permanece explícito como demonstração. O deploy estático pode usar GitHub Pages, Netlify ou Vercel; esta versão está publicada no GitHub Pages em https://g7373hsh-glitch.github.io/Trabalho-AdaptSport/ e versionada em https://github.com/g7373hsh-glitch/Trabalho-AdaptSport. A aplicação continua sendo código estático e documentação, sem backend.
