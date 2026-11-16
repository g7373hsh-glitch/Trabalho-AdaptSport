from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NAV = [
    ("index.html", "Início"),
    ("modalidades.html", "Modalidades"),
    ("esporte-adaptado.html", "O que é"),
    ("atletas.html", "Atletas"),
    ("beneficios-saude.html", "Saúde"),
    ("onde-praticar.html", "Onde praticar"),
    ("acessibilidade.html", "Acessibilidade"),
    ("depoimentos.html", "Depoimentos e mídia"),
    ("envolva-se.html", "Como se envolver"),
    ("contato.html", "Contato"),
]

PAGES = [
    {
        "file": "index.html",
        "title": "AdaptSport | Esporte adaptado e saúde inclusiva",
        "description": "Informação acessível sobre esporte adaptado, modalidades paralímpicas, saúde inclusiva e caminhos para participar.",
        "body": '''
<section class="hero" aria-labelledby="titulo-pagina">
  <div class="container hero__layout">
    <div class="hero__copy">
      <p class="eyebrow">Sustentabilidade social · inclusão · ODS 3 e 10</p>
      <h1 id="titulo-pagina">Esporte adaptado é saúde, inclusão e pertencimento.</h1>
      <p class="lead">Um guia acessível para conhecer modalidades, encontrar caminhos para praticar e ampliar a participação de pessoas com deficiência no esporte.</p>
      <div class="actions">
        <a class="btn btn-primary" href="modalidades.html">Conheça as modalidades</a>
        <a class="btn btn-outline" href="contato.html">Fale com o projeto</a>
      </div>
    </div>
    <div class="hero-art" role="img" aria-label="Ilustração vetorial de uma atleta em cadeira de rodas esportiva, em movimento">
      <svg viewBox="0 0 420 330" aria-hidden="true" focusable="false">
        <circle cx="227" cy="245" r="65" fill="none" stroke="#0B6E4F" stroke-width="11"/>
        <circle cx="227" cy="245" r="8" fill="#0B6E4F"/>
        <path d="M227 190v-52l44-20m-44 72h59m-59-22-28 67m28-20 38 34" fill="none" stroke="#12211C" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/>
        <circle cx="278" cy="111" r="15" fill="#12211C"/>
        <circle cx="331" cy="245" r="14" fill="none" stroke="#0B6E4F" stroke-width="7"/>
        <path d="M25 210h98M46 235h76M10 184h86" stroke="#FF6B35" stroke-width="7" stroke-linecap="round"/>
        <path d="M35 294h345" stroke="#0B6E4F" stroke-opacity=".2" stroke-width="2"/>
      </svg>
    </div>
  </div>
</section>
<section class="section" aria-labelledby="impacto-titulo">
  <div class="container">
    <div class="section__head">
      <p class="eyebrow">Contexto com fonte pública</p>
      <h2 id="impacto-titulo">Acesso ao esporte também é participação social.</h2>
      <p>O Censo Demográfico 2022 estimou 14,4 milhões de pessoas com deficiência, equivalentes a 7,3% da população de 2 anos ou mais. O dado reforça a importância de remover barreiras e ampliar oportunidades — não define a experiência individual de ninguém.</p>
    </div>
    <div class="stat-grid">
      <article class="stat-card"><h3>14,4 mi</h3><p>pessoas com deficiência no Brasil, segundo o Censo 2022</p></article>
      <article class="stat-card"><h3>7,3%</h3><p>da população com 2 anos ou mais, na definição estatística usada pelo IBGE</p></article>
      <article class="stat-card"><h3>10 páginas</h3><p>informação organizada para conhecer, localizar e participar</p></article>
    </div>
    <p class="source-note">Fonte: <a href="https://biblioteca.ibge.gov.br/visualizacao/livros/liv102317_informativo.pdf" rel="noopener">IBGE, Pessoas com Deficiência e as Desigualdades Sociais no Brasil, 2ª edição (Censo 2022)</a>.</p>
  </div>
</section>
<section class="section section--alt" aria-labelledby="ods-titulo">
  <div class="container">
    <div class="section__head"><p class="eyebrow">Impacto social</p><h2 id="ods-titulo">Conexão explícita com os ODS</h2><p>O projeto é informativo e acadêmico. Sua contribuição é facilitar acesso a informação e a caminhos de participação; não representa certificação nem parceria institucional.</p></div>
    <div class="card-grid">
      <article class="card"><span class="tag">ODS 3</span><h3>Saúde e bem-estar</h3><p>Apresenta o esporte como oportunidade de movimento, convivência e bem-estar, respeitando orientação profissional e a escolha de cada pessoa.</p><a href="https://www.ipea.gov.br/ods/ods3.html">Conheça o ODS 3 no Ipea</a></article>
      <article class="card"><span class="tag">ODS 10</span><h3>Redução das desigualdades</h3><p>Destaca barreiras e caminhos para participação de pessoas com deficiência em igualdade de condições.</p><a href="https://www.ipea.gov.br/ods/ods10.html">Conheça o ODS 10 no Ipea</a></article>
      <article class="card"><span class="tag">ODS 11</span><h3>Cidades acessíveis</h3><p>Convida a observar transporte, calçadas e espaços esportivos seguros, inclusivos e acessíveis.</p><a href="https://www.ipea.gov.br/ods/ods11.html">Conheça o ODS 11 no Ipea</a></article>
    </div>
  </div>
</section>
<section class="section" aria-labelledby="noticias-titulo">
  <div class="container">
    <div class="section__head"><p class="eyebrow">Atualizações externas</p><h2 id="noticias-titulo">Notícias do movimento paralímpico</h2><p>As matérias abaixo são publicadas pelo Comitê Paralímpico Brasileiro (CPB). O AdaptSport não é a fonte dessas notícias.</p></div>
    <div class="card-grid">
      <article class="card"><p class="meta">26 out. 2026 · CPB</p><h3>Voluntariado nas Paralimpíadas Escolares 2026</h3><p>O CPB publicou informações sobre os voluntários selecionados e as etapas da competição.</p><a href="https://cpb.org.br/noticias/cpb-divulga-lista-de-voluntarios-selecionados-para-as-paralimpiadas-escolares-2026/">Ler matéria no CPB</a></article>
      <article class="card"><p class="meta">15 out. 2026 · CPB</p><h3>Seminário de modalidades em Centro de Referência</h3><p>Uma atualização sobre formação e modalidades paralímpicas em Aracaju.</p><a href="https://cpb.org.br/noticias/cpb-promove-seminario-de-modalidades-paralimpicas-em-centro-de-referencia-de-aracaju-no-sergipe/">Ler matéria no CPB</a></article>
      <article class="card"><p class="meta">Acompanhe · CPB</p><h3>Agenda e notícias oficiais</h3><p>Consulte a agenda completa, resultados e comunicados diretamente no canal do Comitê.</p><a href="https://cpb.org.br/noticias/">Abrir notícias do CPB</a></article>
    </div>
  </div>
</section>
<section class="section section--alt" aria-labelledby="guia-titulo">
  <div class="container two-column">
    <div><p class="eyebrow">Guia rápido local</p><h2 id="guia-titulo">Qual caminho você procura?</h2><p>Digite um assunto para receber uma orientação predefinida e links do próprio site. Este recurso funciona no navegador, não usa um modelo generativo e não envia dados.</p></div>
    <form class="quick-guide" id="guia-form">
      <label for="guia-pergunta">Sua dúvida</label>
      <div class="inline-form"><input id="guia-pergunta" name="pergunta" type="search" autocomplete="off" placeholder="Ex.: onde praticar?" aria-describedby="guia-ajuda"><button class="btn btn-primary" type="submit">Buscar</button></div>
      <small id="guia-ajuda">Experimente: modalidade, praticar, acessibilidade, voluntariado ou contato.</small>
      <p class="guide-answer" id="guia-resposta" role="status" aria-live="polite">As respostas são regras locais e fixas.</p>
    </form>
  </div>
</section>
<section class="section" aria-labelledby="mapa-titulo">
  <div class="container">
    <div class="section__head"><h2 id="mapa-titulo">Explore o AdaptSport</h2><p>De um panorama inicial a caminhos práticos para conhecer o esporte adaptado.</p></div>
    <ul class="page-map">{PAGE_LINKS}</ul>
  </div>
</section>
<aside class="ods-note container"><strong>ODS no projeto:</strong> saúde e bem-estar (ODS 3), redução das desigualdades (ODS 10) e espaços inclusivos (ODS 11). Veja <a href="docs/fontes-e-referencias.md">as fontes utilizadas</a>.</aside>
'''
    },
    {
        "file": "modalidades.html",
        "title": "Modalidades paralímpicas | AdaptSport",
        "description": "Conheça oito modalidades paralímpicas e adaptadas, com uma busca simples e informações básicas sobre cada esporte.",
        "body": '''
<section class="page-hero" aria-labelledby="titulo-pagina"><div class="container"><p class="eyebrow">Página 2 · catálogo esportivo</p><h1 id="titulo-pagina">Modalidades paralímpicas e esporte adaptado</h1><p class="lead">Cada modalidade tem regras e recursos próprios. Este panorama apresenta oito esportes; para regras atualizadas e classificação, consulte as entidades oficiais.</p></div></section>
<section class="section" aria-labelledby="catalogo-titulo"><div class="container">
  <div class="section__head"><h2 id="catalogo-titulo">Encontre uma modalidade</h2><p>Use a busca por nome, tipo ou característica. O filtro é opcional e funciona com teclado.</p></div>
  <div class="filter-bar"><label for="busca-modalidade">Filtrar modalidades</label><input id="busca-modalidade" type="search" placeholder="Ex.: piscina, quadra, goalball" aria-controls="lista-modalidades"><p id="resultado-modalidades" role="status" aria-live="polite">8 modalidades exibidas.</p></div>
  <ul class="sport-list" id="lista-modalidades">
    <li class="sport-card" data-modalidade="para-atletismo corrida salto arremesso pista"><span class="sport-icon" aria-hidden="true">01</span><div><h3>Para-atletismo</h3><p>Provas de pista e campo, incluindo corrida, salto e arremesso, com classes esportivas distintas.</p><ul class="chips"><li>Individual</li><li>Pista e campo</li><li>Classes esportivas</li></ul></div></li>
    <li class="sport-card" data-modalidade="basquete cadeira de rodas coletivo quadra"><span class="sport-icon" aria-hidden="true">02</span><div><h3>Basquete em cadeira de rodas</h3><p>Esporte coletivo em quadra, com cadeiras esportivas e classificação funcional.</p><ul class="chips"><li>Coletivo</li><li>Quadra</li><li>Cadeira esportiva</li></ul></div></li>
    <li class="sport-card" data-modalidade="natação piscina água classes"><span class="sport-icon" aria-hidden="true">03</span><div><h3>Natação paralímpica</h3><p>Provas em piscina com adaptações de largada e orientação conforme a classe e a necessidade do atleta.</p><ul class="chips"><li>Piscina</li><li>Individual e revezamento</li><li>Classes S</li></ul></div></li>
    <li class="sport-card" data-modalidade="goalball visual bola guizo quadra"><span class="sport-icon" aria-hidden="true">04</span><div><h3>Goalball</h3><p>Modalidade criada para pessoas com deficiência visual; a bola tem guizos e a orientação depende do som.</p><ul class="chips"><li>Deficiência visual</li><li>Quadra</li><li>Coletivo</li></ul></div></li>
    <li class="sport-card" data-modalidade="bocha precisão calha cadeira"><span class="sport-icon" aria-hidden="true">05</span><div><h3>Bocha paralímpica</h3><p>Jogo de precisão que pode utilizar calha e assistência, conforme a classe esportiva e as regras.</p><ul class="chips"><li>Precisão</li><li>Indoor</li><li>Classes BC</li></ul></div></li>
    <li class="sport-card" data-modalidade="rugby cadeira de rodas contato quadra"><span class="sport-icon" aria-hidden="true">06</span><div><h3>Rúgbi em cadeira de rodas</h3><p>Esporte coletivo de quadra com cadeiras específicas e regras de contato controlado.</p><ul class="chips"><li>Coletivo</li><li>Quadra</li><li>Cadeira esportiva</li></ul></div></li>
    <li class="sport-card" data-modalidade="vôlei sentado voleibol rede quadra coletivo"><span class="sport-icon" aria-hidden="true">07</span><div><h3>Vôlei sentado</h3><p>Variação do voleibol com rede e dimensões adaptadas, disputada com os atletas em contato com o solo.</p><ul class="chips"><li>Coletivo</li><li>Quadra</li><li>Rede adaptada</li></ul></div></li>
    <li class="sport-card" data-modalidade="para-ciclismo bicicleta tandem handbike estrada pista"><span class="sport-icon" aria-hidden="true">08</span><div><h3>Para-ciclismo</h3><p>Inclui bicicletas, handbikes e tandems, com configurações conforme a classe e a prova.</p><ul class="chips"><li>Estrada e pista</li><li>Individual e tandem</li><li>Equipamento adaptado</li></ul></div></li>
  </ul>
  <p class="source-note">Modalidades e nomenclaturas podem variar conforme a competição. Consulte a <a href="https://cpb.org.br/modalidades/">lista oficial de modalidades do CPB</a>.</p>
</div></section>
<aside class="ods-note container"><strong>ODS 3 e 10:</strong> ampliar informação sobre diferentes práticas ajuda a aproximar pessoas de opções de movimento e participação social, sem presumir que uma modalidade sirva para todas.</aside>
'''
    },
    {
        "file": "esporte-adaptado.html",
        "title": "O que é esporte adaptado? | AdaptSport",
        "description": "Entenda esporte adaptado, diferenças de uso com esporte paralímpico e princípios de participação inclusiva.",
        "body": '''
<section class="page-hero" aria-labelledby="titulo-pagina"><div class="container"><p class="eyebrow">Página 3 · conceitos</p><h1 id="titulo-pagina">O que é esporte adaptado?</h1><p class="lead">É esporte organizado para que diferentes pessoas possam participar, com regras, equipamentos, comunicação ou ambiente ajustados quando necessário.</p></div></section>
<section class="section" aria-labelledby="conceito-titulo"><div class="container two-column"><div><h2 id="conceito-titulo">Adaptação é remover barreiras</h2><p>A adaptação pode estar na regra, no equipamento, na forma de orientar, no espaço ou no apoio oferecido. O ponto de partida é ouvir a pessoa que pratica e reconhecer que as necessidades variam.</p><p>O esporte paralímpico reúne modalidades e competições regidas pelo Movimento Paralímpico. Nem toda atividade adaptada é uma modalidade paralímpica: projetos escolares, recreativos e comunitários também podem adaptar práticas sem integrar o programa dos Jogos.</p></div><aside class="callout"><h3>Uma pergunta melhor</h3><p>Em vez de perguntar “qual esporte é para esta deficiência?”, pergunte quais interesses, apoios, equipamentos e acessos a própria pessoa considera importantes.</p></aside></div></section>
<section class="section section--alt" aria-labelledby="principios-titulo"><div class="container"><div class="section__head"><h2 id="principios-titulo">Princípios de participação</h2><p>Um ambiente inclusivo não exige que todos pratiquem do mesmo modo.</p></div><div class="card-grid"><article class="card"><h3>Autonomia</h3><p>Oferecer informação acessível para que a pessoa escolha se, como e quando participar.</p></article><article class="card"><h3>Apoio negociado</h3><p>Perguntar antes de ajudar e combinar apoio com a pessoa, sem decidir por ela.</p></article><article class="card"><h3>Segurança sem exclusão</h3><p>Identificar riscos e adaptações possíveis com participantes e profissionais, evitando proibições automáticas.</p></article></div></div></section>
<section class="section" aria-labelledby="fontes-conceito"><div class="container"><h2 id="fontes-conceito">Fontes para aprofundar</h2><ul class="link-list"><li><a href="https://cpb.org.br/o-comite/quero-ser-um-atleta/">CPB: como iniciar no esporte paralímpico</a></li><li><a href="https://social.desa.un.org/issues/disability/sustainable-development-goals-sdgs-and-disability">ONU: deficiência e Objetivos de Desenvolvimento Sustentável</a></li><li><a href="https://www.ipea.gov.br/ods/ods10.html">Ipea: ODS 10, redução das desigualdades</a></li></ul></div></section>
<aside class="ods-note container"><strong>ODS 10:</strong> acessibilidade e participação são dimensões da inclusão; veja a relação com os ODS na <a href="index.html#ods-titulo">página inicial</a>.</aside>
'''
    },
    {
        "file": "atletas.html",
        "title": "Atletas em destaque | AdaptSport",
        "description": "Perfis de atletas paralímpicos brasileiros com informações atribuídas ao Comitê Paralímpico Brasileiro.",
        "body": '''
<section class="page-hero" aria-labelledby="titulo-pagina"><div class="container"><p class="eyebrow">Página 4 · trajetórias</p><h1 id="titulo-pagina">Atletas em destaque</h1><p class="lead">Trajetórias diferentes ajudam a conhecer o esporte paralímpico sem reduzir atletas à deficiência ou tratar conquistas como histórias de superação obrigatórias.</p></div></section>
<section class="section" aria-labelledby="perfis-titulo"><div class="container"><div class="section__head"><h2 id="perfis-titulo">Modalidades, classes e resultados</h2><p>Resumo de perfis publicados pelo CPB. Os dados foram consultados em 9 de novembro de 2026 e podem mudar; acesse as páginas oficiais para atualizações.</p></div><div class="card-grid athlete-grid">
  <article class="card athlete-card"><span class="tag">Natação · classe S12</span><h3>Carol Santiago</h3><p>Nadadora de Recife, Carol migrou da natação convencional para a paralímpica no fim de 2018. Seu perfil oficial registra seis ouros paralímpicos e o recorde mundial dos 50 m livre, 26s61, estabelecido em 2024.</p><a href="https://cpb.org.br/atletas/maria-carolina-santiago/">Ver perfil oficial do CPB</a></article>
  <article class="card athlete-card"><span class="tag">Atletismo · classe T47</span><h3>Petrúcio Ferreira</h3><p>Atleta paraibano dos 100 m. O perfil do CPB registra três ouros paralímpicos e o recorde mundial da prova em 10s29.</p><a href="https://cpb.org.br/atletas/petrucio-ferreira-dos-santos/">Ver perfil oficial do CPB</a></article>
  <article class="card athlete-card athlete-card--note"><span class="tag">Representatividade</span><h3>Mais histórias, muitas vozes</h3><p>Os perfis acima são dois exemplos. O movimento paralímpico tem atletas de diferentes idades, gêneros, regiões, modalidades e classes.</p><a href="https://cpb.org.br/atletas/">Explore outros perfis oficiais</a></article>
</div><p class="source-note">Fonte dos dados biográficos e resultados: perfis individuais do <a href="https://cpb.org.br/atletas/maria-carolina-santiago/">CPB — Carol Santiago</a> e do <a href="https://cpb.org.br/atletas/petrucio-ferreira-dos-santos/">CPB — Petrúcio Ferreira</a>, consultados em 09/11/2026.</p></div></section>
<section class="section section--alt" aria-labelledby="olhar-titulo"><div class="container"><h2 id="olhar-titulo">Como ler resultados esportivos</h2><p>Classes esportivas agrupam atletas segundo critérios próprios de cada modalidade. A classificação busca tornar a competição mais justa; não é uma medida geral de capacidade nem define a identidade da pessoa.</p><p>Para explicações e regras atuais, prefira as páginas oficiais das modalidades e da competição.</p></div></section>
<aside class="ods-note container"><strong>ODS 10:</strong> a representação importa quando mostra atletas como pessoas e competidoras, em vez de resumir suas histórias à deficiência.</aside>
'''
    },
    {
        "file": "beneficios-saude.html",
        "title": "Benefícios para a saúde | AdaptSport",
        "description": "Informações cuidadosas sobre atividade física, bem-estar, convivência e esporte adaptado, com fontes e ressalvas.",
        "body": '''
<section class="page-hero" aria-labelledby="titulo-pagina"><div class="container"><p class="eyebrow">Página 5 · saúde inclusiva</p><h1 id="titulo-pagina">Benefícios para a saúde e o bem-estar</h1><p class="lead">O esporte pode envolver movimento, aprendizado e convivência. Os efeitos variam entre pessoas; informação geral não substitui orientação clínica ou esportiva.</p></div></section>
<section class="section" aria-labelledby="dimensoes-titulo"><div class="container"><div class="section__head"><h2 id="dimensoes-titulo">O que pode fazer parte da experiência</h2><p>O CPB relata, a partir de pesquisa e depoimentos de atletas, experiências de convivência, autonomia, disciplina e bem-estar emocional.</p></div><div class="card-grid"><article class="card"><h3>Movimento</h3><p>Praticar uma atividade com adaptações combinadas pode ser uma forma de incorporar movimento à rotina.</p></article><article class="card"><h3>Convivência</h3><p>Treinos e equipes podem criar oportunidades de troca com pessoas que compartilham interesses e experiências.</p></article><article class="card"><h3>Autonomia e objetivos</h3><p>Aprender uma habilidade e acompanhar metas escolhidas pode fortalecer a confiança e a autonomia de algumas pessoas.</p></article></div><p class="source-note">Leia o contexto original no <a href="https://cpb.org.br/noticias/os-beneficios-do-esporte-paralimpico-no-emocional-da-pessoa-com-deficiencia/">artigo do CPB sobre esporte e aspectos emocionais</a>.</p></div></section>
<section class="section section--alt" aria-labelledby="cuidado-titulo"><div class="container two-column"><div><h2 id="cuidado-titulo">Comece com segurança e escolha</h2><p>Converse com a equipe esportiva sobre adaptações, acessibilidade, equipamentos e progressão da prática. Se houver dúvida de saúde ou retorno após lesão, procure profissionais que conheçam sua situação.</p><p>Este site não recomenda tratamento, não prescreve exercício e não promete resultado físico ou emocional.</p></div><aside class="callout"><h3>Seu ritmo, sua decisão</h3><p>Participar pode significar lazer, convivência, condicionamento, competição ou apenas experimentar uma modalidade. Não existe uma única meta correta.</p><a class="btn btn-outline" href="onde-praticar.html">Veja como procurar um núcleo</a></aside></div></section>
<aside class="ods-note container"><strong>ODS 3:</strong> saúde e bem-estar incluem acesso a oportunidades seguras de movimento, convivência e informação adequada.</aside>
'''
    },
    {
        "file": "onde-praticar.html",
        "title": "Onde praticar | AdaptSport",
        "description": "Passos e links oficiais para procurar clubes, associações e Centros de Referência Paralímpica no Brasil.",
        "body": '''
<section class="page-hero" aria-labelledby="titulo-pagina"><div class="container"><p class="eyebrow">Página 6 · caminhos de acesso</p><h1 id="titulo-pagina">Onde praticar</h1><p class="lead">A disponibilidade muda por cidade, modalidade e faixa etária. Use diretórios oficiais e confirme diretamente acessibilidade, horários e vagas antes de se deslocar.</p></div></section>
<section class="section" aria-labelledby="passos-titulo"><div class="container"><div class="section__head"><h2 id="passos-titulo">Quatro passos para procurar uma atividade</h2><p>O CPB recomenda começar consultando serviços de esporte, educação, assistência social ou direitos da pessoa com deficiência da sua cidade.</p></div><ol class="steps"><li><h3>Escolha o que deseja experimentar</h3><p>Pense em interesses, distância, horários e tipo de atividade; você pode começar perguntando sobre mais de uma modalidade.</p></li><li><h3>Busque um clube ou Centro de Referência</h3><p>Consulte clubes filiados e Centros de Referência Paralímpica nos canais oficiais.</p></li><li><h3>Faça perguntas antes da visita</h3><p>Confirme transporte, entrada sem degraus, banheiro acessível, equipamentos, comunicação e quem pode acompanhar.</p></li><li><h3>Combine uma visita ou aula inicial</h3><p>Peça informações sobre documentos, custos, disponibilidade e adaptação da atividade antes de ir.</p></li></ol></div></section>
<section class="section section--alt" aria-labelledby="diretorios-titulo"><div class="container two-column"><div><h2 id="diretorios-titulo">Diretórios e referências</h2><ul class="link-list"><li><a href="https://cpb.org.br/o-comite/quero-ser-um-atleta/">CPB: encontre clubes por estado, cidade e modalidade</a></li><li><a href="https://cpb.org.br/programas/centros-de-referencia/">CPB: endereços dos Centros de Referência Paralímpica</a></li><li><a href="https://cpb.org.br/ct-paralimpico/centro-de-treinamento/">CPB: informações do Centro de Treinamento Paralímpico</a></li></ul><p>Para o Centro de Treinamento em São Paulo, o CPB publica o endereço Rodovia dos Imigrantes, km 11,5, Vila Guarani. Confirme atendimento e condições de visita no canal oficial.</p></div><aside class="callout"><h3>Checklist para ligar</h3><ul><li>A modalidade está com inscrição aberta?</li><li>Quais adaptações e equipamentos existem?</li><li>Há custo, lista de espera ou idade mínima?</li><li>Como chegar e pedir apoio de comunicação?</li></ul></aside></div></section>
<aside class="ods-note container"><strong>ODS 10 e 11:</strong> informação sobre oferta local e acessibilidade ajuda a identificar barreiras em equipamentos, transporte e espaço público.</aside>
'''
    },
    {
        "file": "acessibilidade.html",
        "title": "Acessibilidade nos espaços esportivos | AdaptSport",
        "description": "Checklist de acessibilidade física, comunicacional e digital para espaços esportivos inclusivos.",
        "body": '''
<section class="page-hero" aria-labelledby="titulo-pagina"><div class="container"><p class="eyebrow">Página 7 · acesso e autonomia</p><h1 id="titulo-pagina">Acessibilidade nos espaços esportivos</h1><p class="lead">A acessibilidade não é um recurso isolado. Ela acompanha o caminho desde a informação e o transporte até a entrada, a prática e a saída do espaço.</p></div></section>
<section class="section" aria-labelledby="espaco-titulo"><div class="container"><div class="section__head"><h2 id="espaco-titulo">Checklist para conversar com o local</h2><p>Use as perguntas como ponto de partida. A necessidade e a solução devem ser combinadas com a pessoa que vai praticar.</p></div><div class="check-grid"><article class="check-card"><h3>Chegada e circulação</h3><ul><li>O trajeto desde o transporte tem rota sem degraus?</li><li>Há áreas de circulação e portas compatíveis com diferentes apoios?</li><li>O acesso a vestiários e quadras está sinalizado?</li></ul></article><article class="check-card"><h3>Comunicação</h3><ul><li>Informações podem ser recebidas em texto e áudio?</li><li>Há recursos visuais e sonoros para instruções e partidas?</li><li>Como são solicitados intérpretes ou outros apoios?</li></ul></article><article class="check-card"><h3>Prática e equipamentos</h3><ul><li>Existem equipamentos adaptados ou possibilidade de empréstimo?</li><li>Quem explica as regras e combinações de segurança?</li><li>É possível conhecer o espaço antes da primeira atividade?</li></ul></article></div></div></section>
<section class="section section--alt" aria-labelledby="site-titulo"><div class="container"><div class="section__head"><h2 id="site-titulo">Acessibilidade digital aplicada ao AdaptSport</h2><p>O projeto usa linguagem declarada em português brasileiro, landmarks semânticos, link para pular conteúdo, títulos em ordem, foco visível, formulários rotulados, mensagens de estado e controles de fonte/contraste.</p></div><ul class="feature-list"><li>As imagens informativas recebem alternativa textual; ícones decorativos são ocultados da tecnologia assistiva.</li><li>O menu móvel pode ser aberto e fechado por teclado e informa seu estado.</li><li>O conteúdo reorganiza-se em telas menores, sem depender somente de cor para transmitir informação.</li><li>A qualidade percebida pode variar por dispositivo e tecnologia assistiva; reporte barreiras pela página de contato.</li></ul><p class="source-note">A acessibilidade do código deve ser avaliada por pessoas e ferramentas. Consulte <a href="https://www.w3.org/WAI/standards-guidelines/wcag/">as diretrizes WCAG do W3C</a>.</p></div></section>
<aside class="ods-note container"><strong>ODS 10 e 11:</strong> acessibilidade digital e física é condição de participação em espaços públicos e comunitários.</aside>
'''
    },
    {
        "file": "depoimentos.html",
        "title": "Depoimentos e mídia | AdaptSport",
        "description": "Relatos publicados pelo CPB, vídeo local com legendas, áudio narrado com transcrição e vídeo externo oficial.",
        "body": '''
<section class="page-hero" aria-labelledby="titulo-pagina"><div class="container"><p class="eyebrow">Página 8 · histórias e mídia</p><h1 id="titulo-pagina">Depoimentos e mídia</h1><p class="lead">Relatos públicos e conteúdos com recursos de acesso. Os depoimentos abaixo foram publicados pelo CPB; a narração local é material informativo criado para este projeto acadêmico.</p></div></section>
<section class="section" aria-labelledby="relatos-titulo"><div class="container"><div class="section__head"><h2 id="relatos-titulo">Vozes do esporte paralímpico</h2><p>As citações são reproduzidas com atribuição ao Comitê Paralímpico Brasileiro.</p></div><div class="quote-grid"><figure class="quote-card"><blockquote>“Pela convivência com outros atletas com deficiência e também por poder competir nas mesmas condições.”</blockquote><figcaption>Welder Camargo Knaf, em resposta a pesquisa citada pelo CPB no artigo <a href="https://cpb.org.br/noticias/os-beneficios-do-esporte-paralimpico-no-emocional-da-pessoa-com-deficiencia/">sobre aspectos emocionais do esporte paralímpico</a>.</figcaption></figure><figure class="quote-card"><blockquote>“Muitos olhavam com pena e hoje, com o esporte, veem como inspiração...”</blockquote><figcaption>Sônia Gouveia, atleta de atletismo, em depoimento publicado pelo CPB no mesmo artigo. A citação é contextualizada na fonte original.</figcaption></figure></div></div></section>
<section class="section section--alt" aria-labelledby="video-local-titulo"><div class="container media-grid"><div><h2 id="video-local-titulo">Vídeo explicativo com legendas</h2><p>Motion graphic original para esta atividade, com narração em português e faixa de legendas selecionável no player.</p><video class="media-player" controls preload="metadata" poster="assets/media/video-poster.png" aria-label="Vídeo explicativo sobre esporte adaptado, com narração e legendas em português"><source src="assets/media/guia-esporte-adaptado.mp4" type="video/mp4"><track kind="captions" src="assets/media/guia-esporte-adaptado.vtt" srclang="pt-BR" label="Português" default>Seu navegador não reproduz este vídeo. Use o áudio narrado e a transcrição abaixo.</video></div><div><h2 id="audio-titulo">Ouça a narração</h2><p>O áudio também está disponível separadamente.</p><audio class="media-player" controls preload="none" aria-labelledby="audio-titulo"><source src="assets/media/guia-esporte-adaptado.mp3" type="audio/mpeg">Seu navegador não reproduz este áudio. Leia a transcrição a seguir.</audio><details class="transcript"><summary>Transcrição do áudio</summary><p>O esporte adaptado abre caminhos para que mais pessoas participem do movimento, da convivência e da competição. Cada modalidade combina regras, equipamentos e apoios diferentes. Para começar, procure a secretaria de esporte da sua cidade ou consulte os clubes e Centros de Referência Paralímpica no site do Comitê Paralímpico Brasileiro. A prática deve respeitar a escolha da pessoa e contar com orientação profissional. O AdaptSport é um projeto acadêmico de informação. Ele não substitui avaliação médica, de fisioterapia ou orientação esportiva.</p></details></div></div></section>
<section class="section" aria-labelledby="iframe-titulo"><div class="container"><div class="section__head"><h2 id="iframe-titulo">Conheça o Centro de Treinamento Paralímpico</h2><p>Vídeo hospedado pelo canal do Comitê Paralímpico Brasileiro. Se o conteúdo externo não carregar, abra o <a href="https://www.youtube.com/watch?v=wexJWQ9cTY4">vídeo no YouTube</a>.</p></div><div class="video-embed"><iframe title="Vídeo do Centro de Treinamento Paralímpico Brasileiro, publicado pelo Comitê Paralímpico Brasileiro" src="https://www.youtube-nocookie.com/embed/wexJWQ9cTY4" loading="lazy" referrerpolicy="strict-origin-when-cross-origin" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe></div><p class="source-note">Fonte externa: <a href="https://www.youtube.com/watch?v=wexJWQ9cTY4">canal oficial do CPB no YouTube</a>.</p></div></section>
<aside class="ods-note container"><strong>ODS 3 e 10:</strong> histórias e mídia acessíveis ajudam a compartilhar informação sobre esporte, saúde e participação sem substituir a voz da pessoa.</aside>
'''
    },
    {
        "file": "envolva-se.html",
        "title": "Como se envolver | AdaptSport",
        "description": "Maneiras de participar do esporte adaptado, buscar oportunidades de voluntariado e apoiar iniciativas oficiais.",
        "body": '''
<section class="page-hero" aria-labelledby="titulo-pagina"><div class="container"><p class="eyebrow">Página 9 · participação</p><h1 id="titulo-pagina">Como se envolver</h1><p class="lead">Praticar, compartilhar informação, atuar como voluntário ou apoiar um projeto são caminhos diferentes. Escolha o que combina com sua disponibilidade e confirme as condições diretamente com a organização responsável.</p></div></section>
<section class="section" aria-labelledby="opcoes-titulo"><div class="container"><div class="section__head"><h2 id="opcoes-titulo">Escolha seu caminho</h2><p>O AdaptSport é um projeto acadêmico e não representa uma ONG registrada. Não recebemos doações e não temos vagas próprias.</p></div><div class="card-grid"><article class="card"><span class="tag">Praticar</span><h3>Procure uma modalidade</h3><p>Use os diretórios oficiais para conhecer clubes e Centros de Referência Paralímpica na sua região.</p><a href="onde-praticar.html">Ir para onde praticar</a></article><article class="card"><span class="tag">Voluntariado</span><h3>Acompanhe chamadas oficiais</h3><p>Eventos e critérios mudam. Consulte a agenda e os canais do CPB antes de se inscrever.</p><a href="https://cpb.org.br/noticias/">Ver notícias e oportunidades do CPB</a></article><article class="card"><span class="tag">Apoio</span><h3>Compartilhe recursos confiáveis</h3><p>Divulgue informação acessível, apoie organizações reconhecidas e confirme a identidade do destinatário antes de contribuir financeiramente.</p><a href="https://cpb.org.br/o-comite/patrocinio-e-parcerias/">Consulte parcerias oficiais do CPB</a></article></div></div></section>
<section class="section section--alt" aria-labelledby="apoio-titulo"><div class="container two-column"><div><h2 id="apoio-titulo">Apoiar também é remover barreiras</h2><p>Uma equipe pode mapear acessos, oferecer comunicação clara, ouvir atletas e direcionar pessoas a serviços confiáveis. Ações locais devem ser combinadas com a comunidade e com a instituição responsável.</p></div><aside class="callout"><h3>Transparência</h3><p>Este site não solicita doação, não coleta pagamento e não encaminha cadastros para clubes. O formulário da página de contato serve somente para demonstrar validação no navegador.</p><a class="btn btn-outline" href="contato.html">Conheça o formulário de demonstração</a></aside></div></section>
<aside class="ods-note container"><strong>ODS 10:</strong> participar, compartilhar informação e apoiar iniciativas confiáveis são formas de contribuir para inclusão sem prometer resultados que não controlamos.</aside>
'''
    },
    {
        "file": "contato.html",
        "title": "Contato | AdaptSport",
        "description": "Formulário acessível de demonstração com validação JavaScript, mensagens de erro e rascunho local.",
        "body": '''
<section class="page-hero" aria-labelledby="titulo-pagina"><div class="container"><p class="eyebrow">Página 10 · fale com o projeto</p><h1 id="titulo-pagina">Contato</h1><p class="lead">Use o formulário para testar a validação acessível. Este protótipo acadêmico não envia mensagens para uma equipe ou ONG.</p></div></section>
<section class="section" aria-labelledby="formulario-titulo"><div class="container form-layout"><div><h2 id="formulario-titulo">Formulário demonstrativo</h2><p>O rascunho fica somente no armazenamento local deste navegador, para demonstrar o uso de localStorage. Em dispositivo compartilhado, use “Apagar rascunho” ao terminar.</p><p>Não inclua dados sensíveis. Ao confirmar, o site apenas mostra uma mensagem de sucesso local; nenhuma mensagem é transmitida.</p><div class="callout"><h3>Equipe do projeto</h3><p>AdaptSport — trabalho acadêmico de Desenvolvimento Front-end. A lista nominal da equipe está em <a href="integrantes.txt">integrantes.txt</a>.</p></div></div>
<form id="form-contato" class="contact-form" action="#formulario-titulo" method="post">
  <div class="form-status" id="form-status" role="status" aria-live="polite" tabindex="-1"></div>
  <div class="field"><label for="nome">Nome completo <span aria-hidden="true">*</span></label><input id="nome" name="nome" type="text" autocomplete="name" required minlength="3" maxlength="80" pattern="[A-Za-zÀ-ÖØ-öø-ÿ'’ -]{3,80}" aria-describedby="erro-nome"><small class="field-error" id="erro-nome"></small></div>
  <div class="field"><label for="email">E-mail <span aria-hidden="true">*</span></label><input id="email" name="email" type="email" autocomplete="email" required maxlength="120" aria-describedby="erro-email"><small class="field-error" id="erro-email"></small></div>
  <div class="field"><label for="telefone">Telefone para contato <span aria-hidden="true">*</span></label><input id="telefone" name="telefone" type="tel" autocomplete="tel" required pattern="[0-9+(). -]{8,20}" title="Use de 8 a 20 caracteres: números, espaço, parênteses, ponto ou hífen." aria-describedby="erro-telefone"><small class="field-error" id="erro-telefone"></small></div>
  <div class="form-row"><div class="field"><label for="data-contato">Melhor data para retorno (opcional)</label><input id="data-contato" name="data-contato" type="date" aria-describedby="erro-data-contato"><small class="field-error" id="erro-data-contato"></small></div><div class="field"><label for="frequencia">Dias de prática por semana (opcional)</label><input id="frequencia" name="frequencia" type="number" min="1" max="7" step="1" inputmode="numeric" aria-describedby="erro-frequencia"><small class="field-error" id="erro-frequencia"></small></div></div>
  <div class="field"><label for="assunto">Assunto <span aria-hidden="true">*</span></label><select id="assunto" name="assunto" required aria-describedby="erro-assunto"><option value="">Selecione uma opção</option><option value="pratica">Onde praticar</option><option value="voluntariado">Voluntariado</option><option value="acessibilidade">Acessibilidade</option><option value="outro">Outro assunto</option></select><small class="field-error" id="erro-assunto"></small></div>
  <div class="field"><label for="mensagem">Mensagem <span aria-hidden="true">*</span></label><textarea id="mensagem" name="mensagem" rows="5" required minlength="10" maxlength="1000" aria-describedby="erro-mensagem"></textarea><small class="field-error" id="erro-mensagem"></small></div>
  <div class="form-actions"><button class="btn btn-primary" type="submit">Validar formulário</button><button class="btn btn-outline" id="limpar-rascunho" type="button">Apagar rascunho</button></div>
</form></div></section>
<section class="section section--alt" aria-labelledby="canais-titulo"><div class="container"><h2 id="canais-titulo">Canais oficiais</h2><p>Para informações sobre clubes, inscrições, eventos e programas, consulte diretamente o <a href="https://cpb.org.br/">Comitê Paralímpico Brasileiro</a> ou a secretaria responsável no seu município.</p></div></section>
<aside class="ods-note container"><strong>ODS 10:</strong> canais claros, rotulados e acessíveis ajudam a reduzir barreiras de informação.</aside>
'''
    },
]


def nav_markup(active_file: str) -> str:
    items = []
    for href, label in NAV:
        current = ' aria-current="page"' if href == active_file else ""
        items.append(f'<li><a href="{href}"{current}>{label}</a></li>')
    return "\n        ".join(items)


def footer_markup() -> str:
    links = "\n          ".join(f'<li><a href="{href}">{label}</a></li>' for href, label in NAV)
    return f'''<footer class="site-footer">
  <div class="container footer-grid">
    <section aria-labelledby="rodape-projeto"><h2 id="rodape-projeto">AdaptSport</h2><p>Projeto acadêmico de informação sobre esporte adaptado, saúde inclusiva e acessibilidade digital.</p><p class="footer-ods">ODS 3 · ODS 10 · ODS 11</p></section>
    <nav aria-label="Navegação do rodapé"><h2>Navegação</h2><ul class="footer-nav">{links}</ul></nav>
    <section aria-labelledby="rodape-acessibilidade"><h2 id="rodape-acessibilidade">Acessibilidade</h2><p>Link para pular conteúdo, foco visível, menu por teclado, fonte ajustável e alto contraste.</p><p><a href="acessibilidade.html">Conheça os recursos</a></p></section>
  </div>
  <div class="container footer-bottom"><p>Material informativo e acadêmico. Fontes externas identificadas junto aos conteúdos; informações consultadas em 09/11/2026.</p><p><a href="docs/README.md">Documentação do projeto</a> · <a href="docs/fontes-e-referencias.md">Fontes e referências</a></p></div>
</footer>'''


def render(page: dict) -> str:
    nav = nav_markup(page["file"])
    body = page["body"].replace("{PAGE_LINKS}", "\n".join(f'<li><a href="{href}">{label}</a></li>' for href, label in NAV))
    return f'''<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{page['description']}">
  <meta name="theme-color" content="#0B6E4F">
  <title>{page['title']}</title>
  <link rel="stylesheet" href="assets/style.css">
  <script src="assets/a11y.js" defer></script>
  <script src="assets/app.js" defer></script>
</head>
<body>
<a class="skip-link" href="#conteudo">Pular para o conteúdo principal</a>
<div class="a11y-bar" role="group" aria-label="Controles de acessibilidade"><div class="container a11y-bar__inner"><span class="a11y-bar__label">Acessibilidade</span><div class="a11y-bar__controls"><button type="button" id="btn-fonte" aria-pressed="false">Aumentar tamanho do texto</button><button type="button" id="btn-contraste" aria-pressed="false">Alto contraste</button></div></div></div>
<header class="site-header">
  <div class="container header-top">
    <a class="logo" href="index.html" aria-label="AdaptSport — página inicial"><svg class="logo__mark" viewBox="0 0 40 40" fill="none" aria-hidden="true" focusable="false"><circle cx="20" cy="20" r="19" stroke="currentColor" stroke-width="2"/><path d="M10 26 17 17l5 5 8-10" stroke="#FF6B35" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/><circle cx="30" cy="12" r="3" fill="#FF6B35"/></svg><span>Adapt<span class="accent-word">Sport</span></span></a>
    <span class="nav-note">Esporte adaptado · informação e participação</span>
    <button class="nav-toggle" id="nav-toggle" type="button" aria-controls="nav-menu" aria-expanded="true">Menu</button>
  </div>
  <nav class="main-nav container" id="nav-menu" aria-label="Navegação principal"><ul>{nav}</ul></nav>
</header>
<main id="conteudo" tabindex="-1">
{body}
</main>
{footer_markup()}
</body>
</html>
'''


def main() -> None:
    for page in PAGES:
        path = ROOT / page["file"]
        path.write_text(render(page), encoding="utf-8")
    print(f"Geradas {len(PAGES)} páginas HTML em {ROOT}")


if __name__ == "__main__":
    main()
