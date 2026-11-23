(function () {
  "use strict";

  // Conteúdo didático de cada modalidade: o HTML guarda a lista e este objeto guarda os detalhes.
  var details = {
    "01": {
      name: "Para-atletismo",
      what: "Modalidade paralímpica de atletismo praticada por atletas com deficiência física, visual ou intelectual. Reúne provas de pista, campo e rua, como corridas, saltos, arremessos e lançamentos.",
      how: "Os atletas competem em classes funcionais identificadas por T, para pista e rua, ou F, para campo. As adaptações podem incluir cadeira de rodas, próteses, bancos de arremesso, atleta-guia e apoios para algumas classes visuais. Vence quem obtiver o melhor tempo, distância ou marca na prova.",
      youtube: "https://www.youtube.com/watch?v=--rHYSaq49Q",
      youtubeTitle: "Classificação do atletismo paralímpico",
      source: "https://cpb.org.br/modalidades/atletismo/"
    },
    "02": {
      name: "Basquete em cadeira de rodas",
      what: "Modalidade adaptada do basquete convencional, praticada por atletas com deficiência físico-motora em cadeiras de rodas próprias para o esporte. A quadra e a altura da cesta seguem o padrão olímpico.",
      how: "Duas equipes de cinco jogadores disputam quatro quartos de 10 minutos. A cada dois toques na cadeira, o atleta deve quicar, passar ou arremessar a bola. Os jogadores são avaliados por classificação funcional e a soma das classes em quadra não pode ultrapassar 14 pontos.",
      youtube: "https://www.youtube.com/watch?v=lv7bwjqDuqk",
      youtubeTitle: "Basquete em cadeira de rodas - Regras e classes",
      source: "https://cpb.org.br/modalidades/basquete-em-cr/"
    },
    "03": {
      name: "Natação paralímpica",
      what: "Modalidade disputada em piscina por atletas com deficiência físico-motora, visual ou intelectual, organizada por classes esportivas que consideram o tipo e o grau do comprometimento funcional.",
      how: "As provas incluem nado livre, costas, peito, borboleta e medley, em distâncias de 50 a 400 metros. As classes usam S, SB ou SM acompanhadas de um número. Podem existir adaptações nas largadas, viradas e chegadas, como largada na água e uso de tapper para avisar atletas com deficiência visual.",
      youtube: "https://www.youtube.com/watch?v=Lsjmge-GBx0",
      youtubeTitle: "Natação paralímpica - Regras e classes",
      source: "https://cpb.org.br/modalidades/natacao/"
    },
    "04": {
      name: "Goalball",
      what: "Esporte paralímpico criado exclusivamente para pessoas com deficiência visual. Duas equipes usam uma bola com guizo interno e todos os atletas competem vendados para assegurar condições iguais.",
      how: "Cada equipe tem três jogadores em quadra. O objetivo é arremessar a bola com as mãos para ultrapassar o gol adversário; os defensores orientam-se pelo som do guizo. A quadra mede 9 m por 18 m, os gols têm 9 m de largura e a partida tem dois tempos de 12 minutos.",
      youtube: "https://www.youtube.com/watch?v=xV3iw5WYAEc",
      youtubeTitle: "Goalball | Regras e classes - Com audiodescrição",
      source: "https://cpb.org.br/modalidades/goalball/"
    },
    "05": {
      name: "Bocha paralímpica",
      what: "Esporte de precisão praticado por atletas em cadeira de rodas, incluindo pessoas com paralisia cerebral ou outras deficiências severas. O objetivo é lançar bolas coloridas o mais perto possível do bolim, a bola branca.",
      how: "As disputas podem ser individuais, em duplas ou por equipes. Os atletas lançam suas bolas usando mãos, pés ou instrumentos como calhas. Conforme a classe funcional, podem contar com um calheiro ou assistente. Vence quem tiver mais bolas próximas do bolim ao fim da partida.",
      youtube: "https://www.youtube.com/watch?v=Y_p2dwUjwiM",
      youtubeTitle: "Bocha",
      source: "https://cpb.org.br/modalidades/bocha/"
    },
    "06": {
      name: "Rúgbi em cadeira de rodas",
      what: "Esporte paralímpico coletivo para atletas com tetraplegia ou deficiências equivalentes. Homens e mulheres competem juntos em cadeiras de rodas esportivas, buscando atravessar a linha de gol adversária com a bola.",
      how: "As partidas são disputadas em quadra de 28 m por 15 m, com quatro períodos de oito minutos. Cada equipe joga com quatro atletas. Os atletas são classificados de 0,5 a 3,5 e a soma das classes em quadra não pode ultrapassar oito pontos. Há contato físico e a posse é conduzida pelas mãos.",
      youtube: "https://www.youtube.com/watch?v=GEkNYfTh1ZE",
      youtubeTitle: "Rúgbi em cadeira de rodas - Regras e classes",
      source: "https://cpb.org.br/modalidades/rugbi-em-cr/"
    },
    "07": {
      name: "Vôlei sentado",
      what: "Modalidade paralímpica praticada por homens e mulheres com deficiência física ou relacionada à locomoção. É jogada sentada no chão, com os atletas mantendo contato com o solo durante a partida.",
      how: "Duas equipes de seis jogadores competem em uma quadra de 10 m por 6 m, separadas por uma rede de 1,15 m no masculino e 1,05 m no feminino. A partida segue melhor de cinco sets, e vence quem ganhar três. É permitido bloquear o saque e os jogadores devem manter contato com o solo.",
      youtube: "https://www.youtube.com/watch?v=5mqj6MzpX-w",
      youtubeTitle: "Vôlei sentado - Regras e classes",
      source: "https://cpb.org.br/modalidades/volei-sentado/"
    },
    "08": {
      name: "Para-ciclismo",
      what: "Modalidade paralímpica praticada por pessoas com deficiência visual, físico-motora ou paralisia cerebral em bicicletas convencionais adaptadas, triciclos, handbikes ou tandems.",
      how: "As competições ocorrem em provas de estrada e de pista. Os atletas são agrupados em classes funcionais conforme o tipo e o grau da deficiência. Entre as provas estão corrida de estrada, contrarrelógio, sprint, perseguição e scratch.",
      youtube: "https://www.youtube.com/watch?v=YOeJvHhn5eo",
      youtubeTitle: "Você conhece o Paraciclismo?",
      source: "https://cpb.org.br/modalidades/ciclismo/"
    }
  };

  // Liga cada nome clicável ao diálogo que mostra explicação, funcionamento e fontes.
  function setupDetails() {
    var dialog = document.getElementById("modal-modalidade");
    if (!dialog) return;
    var title = document.getElementById("modalidade-titulo");
    var what = document.getElementById("modalidade-o-que-e");
    var how = document.getElementById("modalidade-como-funciona");
    var video = document.getElementById("modalidade-youtube");
    var source = document.getElementById("modalidade-fonte");
    var close = dialog.querySelector("[data-modal-close]");

    // Percorre os oito botões e registra um evento independente para cada modalidade.
    document.querySelectorAll("[data-modalidade-id]").forEach(function (button) {
      // Ao clicar, busca os dados pelo código 01–08 e preenche o diálogo.
      button.addEventListener("click", function () {
        var item = details[button.getAttribute("data-modalidade-id")];
        if (!item) return;
        title.textContent = item.name;
        what.textContent = item.what;
        how.textContent = item.how;
        video.href = item.youtube;
        video.textContent = "Assistir: " + item.youtubeTitle;
        source.href = item.source;
        if (typeof dialog.showModal === "function") dialog.showModal();
        else dialog.setAttribute("open", "");
        close.focus();
      });
    });

    // Permite fechar pelo botão X.
    close.addEventListener("click", function () { dialog.close(); });
    // Também fecha quando a pessoa clica no fundo externo do diálogo.
    dialog.addEventListener("click", function (event) {
      if (event.target === dialog) dialog.close();
    });
  }

  // Inicializa a interação depois do carregamento do documento.
  document.addEventListener("DOMContentLoaded", setupDetails);
})();
