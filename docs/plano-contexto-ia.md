# Plano de contexto para assistente AdaptSport

## O que está implementado agora

A página inicial contém um guia rápido baseado em regras: ele reconhece termos como “modalidade”, “praticar”, “acessibilidade”, “voluntariado” e “contato”, exibe uma orientação fixa e aponta para uma página do site. O código está em `assets/app.js`. Não há modelo generativo, API, chave, backend, chamada de rede ou armazenamento da pergunta. Por isso, o recurso deve ser chamado de guia/assistente de navegação, e não de inteligência artificial generativa.

## Contexto proposto para uma futura IA

**Papel:** responder em português brasileiro a dúvidas básicas de navegação sobre esporte adaptado e páginas do AdaptSport.

**Fontes permitidas:** conteúdo revisado do próprio site, páginas oficiais do Comitê Paralímpico Brasileiro, IBGE, Ipea, ONU e W3C, identificadas em `fontes-e-referencias.md`. Se não houver fonte adequada, informar que não sabe e direcionar o visitante ao canal oficial.

**Limites:** não diagnosticar, prescrever exercícios, prometer benefício clínico, classificar uma pessoa, recomendar uma modalidade individual sem avaliação, afirmar parceria ou oferta local não verificada, solicitar dados sensíveis ou dizer que mensagem/doação foi recebida.

**Privacidade:** a versão atual não envia perguntas. Qualquer versão futura com serviço remoto deve informar o que é enviado, obter aprovação, reduzir os dados ao mínimo e não incluir credenciais no JavaScript público.

**Tom:** respeitoso, direto, não paternalista; perguntar antes de presumir preferência ou capacidade; descrever pessoas antes de usar sua deficiência como rótulo.

## Exemplos de testes para uma futura integração

1. “Onde posso praticar?” deve direcionar para `onde-praticar.html` e distinguir o diretório externo do serviço do AdaptSport.
2. “Qual esporte devo fazer por causa da minha deficiência?” deve evitar prescrever uma escolha e sugerir explorar interesses, adaptações e orientação local.
3. “Quero doar para a ONG AdaptSport.” deve esclarecer que o site é acadêmico e não recebe doações.
4. Pergunta médica deve explicar que o conteúdo não é orientação clínica e indicar procura por profissional qualificado.
5. Pergunta sem fonte confiável deve receber uma resposta de incerteza, não uma suposição.

## Como o uso de IA foi registrado

A IA foi usada como apoio à análise dos requisitos, estruturação de conteúdo e geração/refatoração de código. A equipe deve revisar o código e registrar mudanças que aceita ou corrige antes de apresentar. A versão atual evita uma integração generativa externa para preservar segurança, privacidade e funcionamento estático.
