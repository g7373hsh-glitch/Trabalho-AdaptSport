# Melhorias desde o MVP — antes e depois

O pacote recebido continha a home, a página de modalidades e o arquivo de escopo. Não havia comentários ou nota formal da primeira entrega. Portanto, esta comparação registra somente limitações verificáveis do MVP e os avanços desta versão.

| Antes — MVP recebido | Depois — versão desta atividade |
| --- | --- |
| Havia duas páginas publicadas em arquivo: Início e Modalidades; as outras oito apareciam como planejadas no escopo. | Há dez arquivos HTML estáticos interligados, conforme o mapa de páginas do escopo AdaptSport. |
| O cabeçalho e rodapé listavam somente duas rotas e exibiam “MVP — mais 8 páginas no escopo”. | O menu e rodapé listam as dez páginas; a página atual é identificada por `aria-current="page"`. O aviso de MVP foi retirado. |
| A home apresentava três números sem fonte no HTML recebido: “24”, “+400” e “3 em cada 4”. | Esses números foram removidos. O dado do IBGE (14,4 milhões; 7,3%; Censo 2022, população com 2 anos ou mais) foi incluído com fonte e ressalva. |
| JavaScript era opcional e havia somente os controles de tamanho de texto e contraste. | JavaScript externo contém menu móvel, filtro de modalidades, guia local e formulário com `preventDefault`, mensagens, borda de erro e rascunho no `localStorage`. |
| Não havia formulário de contato/voluntariado. | Há formulário demonstrativo com `required`, e-mail, telefone com `pattern`, data, número, mensagens acessíveis e armazenamento temporário local. Ele informa claramente que não envia dados. |
| Não havia mídia de áudio/vídeo ou transcrição no MVP. | A página Depoimentos e mídia contém citações atribuídas ao CPB, narração, transcrição, vídeo com legenda e iframe oficial externo. |
| Não havia as páginas de saúde, atletas, diretório, acessibilidade, depoimentos e participação. | As páginas foram criadas seguindo os títulos e funções definidos no `escopo-adaptsport.docx`. |
| O escopo dizia que o JavaScript seria opcional no MVP, mas a entrega final exigia JavaScript obrigatório. | A implementação final usa arquivos `.js` externos e documenta cada interação. |
| O pacote recebido não continha histórico Git, URL publicada, feedback do professor, RA ou divisão de papéis. | A documentação e arquivos `.txt` registram essas lacunas. Nenhum commit, deploy, RA, papel ou resultado de avaliação foi fabricado. |

## Evidências

Os arquivos originais do MVP foram preservados em `docs/evidencias/mvp-original/`. As capturas de tela do antes e do depois devem ser mantidas em `docs/evidencias/`; somente as capturas que correspondem à versão real do código devem ser usadas em slides ou relatório.
