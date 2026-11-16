# AdaptSport

Projeto acadêmico estático sobre esporte adaptado, saúde inclusiva e acessibilidade. A versão mantém as dez páginas definidas no escopo original. O menu é compartilhado, o CSS conserva a identidade do MVP e as interações ficam em JavaScript externo.

## Abrir

Abra `index.html` no navegador ou rode `python3 -m http.server 8000` nesta pasta e visite `http://localhost:8000`.

## Estrutura

- `index.html` a `contato.html`: dez páginas interligadas.
- `assets/style.css`: identidade visual responsiva.
- `assets/a11y.js`: preferências de fonte e contraste.
- `assets/app.js`: navegação móvel, filtro, guia local e formulário de demonstração.
- `assets/media/`: MP3, vídeo MP4, poster e legendas; `assets/guia-esporte-adaptado.wav` é o áudio-fonte.
- `scripts/build_pages.py`: gera as dez páginas a partir do conteúdo compartilhado.
- `scripts/build_media.py`: regenera os recursos de mídia usando FFmpeg e Pillow.
- `docs/`: documentação da atividade, orçamento, testes e fontes.
- `apresentacao-adaptsport.pdf` e `apresentacao-adaptsport.pptx`: apresentação da Atividade 2 com 12 lâminas que cobrem os 14 tópicos do roteiro, com notas de fala por integrante.

O formulário não envia mensagens, a página não recebe doações, o guia não usa um modelo generativo e este pacote ainda não tem URL pública ou repositório GitHub conectado. Veja [a documentação completa](docs/README.md).
