# Evidências e verificações

**Versão verificada:** 09/11/2026. As verificações a seguir são locais; ainda não há URL pública nem repositório conectado.

## Validação HTML e recursos

As dez páginas finais da raiz foram submetidas ao Nu HTML Checker do W3C em 09/11/2026. Resultado: **10/10 páginas, 0 erros e 0 avisos**. Os arquivos validados foram `index.html`, `modalidades.html`, `esporte-adaptado.html`, `atletas.html`, `beneficios-saude.html`, `onde-praticar.html`, `acessibilidade.html`, `depoimentos.html`, `envolva-se.html` e `contato.html`.

A checagem automatizada de `href`, `src` e fragmentos locais encontrou **0 links/recursos internos inexistentes** após corrigir o caminho para `integrantes.txt`. O relatório também verificou os metadados de página. O arquivo de orçamento em `docs/orcamento_hospedagem.html` é complementar e não faz parte das dez rotas do site; validar esse documento separadamente antes de alterá-lo.

## Sintaxe e testes de interação

`node --check assets/app.js` e `node --check assets/a11y.js` passaram. `python3 -m py_compile scripts/build_pages.py scripts/build_media.py` também passou.

Um harness temporário em Chromium headless executou **9 de 9 testes**: carregar as páginas; abrir/fechar o menu móvel; aplicar fonte maior e contraste; buscar orientação no guia local; filtrar Goalball; bloquear envio vazio e mostrar erro associado; gravar rascunho em `localStorage`; validar os campos preenchidos; e apresentar a confirmação sem transmitir a mensagem, removendo o rascunho após a validação. O harness foi retirado do pacote depois do teste.

O vídeo local foi verificado com FFprobe: H.264, 1280×720, faixa AAC, duração 32,84 segundos. O pacote de mídia local é composto por MP3, MP4, poster PNG e legenda WebVTT. O iframe do CPB depende de Internet.

## Contraste verificado por amostragem

Foram calculados por fórmula WCAG pares principais definidos em `assets/style.css`: texto `#12211C` sobre fundo `#F5F6F0` = 15,34:1; texto `#3C4B44` sobre branco = 9,20:1; branco sobre verde `#0B6E4F` = 6,25:1; texto claro sobre verde-escuro `#084F39` = 8,86:1; texto escuro sobre laranja `#FF6B35` = 5,88:1; verde-escuro `#005236` sobre verde-claro `#DCEFE3` = 7,74:1. Todos esses pares superam 4,5:1 para texto normal. A amostragem não substitui auditoria completa de estados, mídia, zoom, leitor de tela ou contraste de cada combinação dinâmica.

## Capturas e plano B

- `docs/evidencias/interface-desktop.png`: home final, 1440×1100.
- `docs/evidencias/interface-celular.png`: home final, 390×1150.
- `docs/evidencias/mvp-original-desktop.png` e `mvp-original-celular.png`: home do MVP antes da mudança.
- `docs/evidencias/mvp-original/`: cópia local preservada do HTML/CSS/JS original.

As capturas PNG e o vídeo local podem apoiar uma demonstração se a Internet falhar; o site também pode ser aberto com `python3 -m http.server 8000`. Isso não substitui o requisito de URL pública HTTPS.

## Revisões ainda necessárias

A equipe deve testar fisicamente cada página em desktop/tablet/celular, teclado real, tecnologias assistivas e reprodução de mídia em mais navegadores. O roteiro pede navegação completa por teclado; o código tem foco visível, link de pular conteúdo e controles semânticos, mas o ensaio humano ainda precisa ser feito. Também faltam verificar a versão pública após deploy, os limites de hospedagem e os commits/PR reais.
