// Interações do AdaptSport. Não envia dados a serviços externos.
// O guia rápido usa regras locais e respostas fixas; não é um modelo generativo.
(function () {
  "use strict";
  document.documentElement.classList.add("js");

  document.addEventListener("DOMContentLoaded", function () {
    setupMobileMenu();
    setupModalitiesFilter();
    setupQuickGuide();
    setupContactForm();
  });

  function setupMobileMenu() {
    var button = document.getElementById("nav-toggle");
    var navigation = document.getElementById("nav-menu");
    if (!button || !navigation) return;

    var mobileQuery = window.matchMedia("(max-width: 650px)");
    function syncLayout() {
      navigation.classList.toggle("is-collapsed", mobileQuery.matches);
      button.setAttribute("aria-expanded", String(!mobileQuery.matches));
      button.textContent = mobileQuery.matches ? "Abrir menu" : "Menu";
    }
    syncLayout();
    if (mobileQuery.addEventListener) mobileQuery.addEventListener("change", syncLayout);
    else if (mobileQuery.addListener) mobileQuery.addListener(syncLayout);

    button.addEventListener("click", function () {
      var isOpen = button.getAttribute("aria-expanded") === "true";
      navigation.classList.toggle("is-collapsed", isOpen);
      button.setAttribute("aria-expanded", String(!isOpen));
      button.textContent = isOpen ? "Abrir menu" : "Fechar menu";
      if (!isOpen) {
        var firstLink = navigation.querySelector("a");
        if (firstLink) firstLink.focus();
      }
    });

    navigation.addEventListener("click", function (event) {
      if (event.target.closest("a") && mobileQuery.matches) {
        navigation.classList.add("is-collapsed");
        button.setAttribute("aria-expanded", "false");
        button.textContent = "Abrir menu";
      }
    });
  }

  function setupModalitiesFilter() {
    var input = document.getElementById("busca-modalidade");
    var list = document.getElementById("lista-modalidades");
    var status = document.getElementById("resultado-modalidades");
    if (!input || !list || !status) return;

    var items = Array.prototype.slice.call(list.querySelectorAll(".sport-card"));
    input.addEventListener("input", function () {
      var term = normalize(input.value.trim());
      var visible = 0;
      items.forEach(function (item) {
        var text = normalize(item.textContent + " " + (item.getAttribute("data-modalidade") || ""));
        var matches = !term || text.indexOf(term) !== -1;
        item.hidden = !matches;
        if (matches) visible += 1;
      });
      status.textContent = visible + (visible === 1 ? " modalidade exibida." : " modalidades exibidas.");
    });
  }

  function normalize(value) {
    return value.normalize("NFD").replace(/[\u0300-\u036f]/g, "").toLocaleLowerCase("pt-BR");
  }

  function setupQuickGuide() {
    var form = document.getElementById("guia-form");
    var input = document.getElementById("guia-pergunta");
    var answer = document.getElementById("guia-resposta");
    if (!form || !input || !answer) return;

    var rules = [
      { terms: ["modalidade", "esporte", "goalball", "bocha", "natacao", "basquete"], text: "Veja os esportes disponíveis na página Modalidades e consulte o CPB para regras e classes atualizadas.", href: "modalidades.html" },
      { terms: ["praticar", "clube", "nucleo", "centro", "onde"], text: "A página Onde praticar reúne diretórios oficiais e perguntas para fazer antes de visitar um núcleo.", href: "onde-praticar.html" },
      { terms: ["acessibilidade", "acesso", "rampa", "teclado", "contraste"], text: "Consulte as orientações de acessibilidade física e digital e use os controles de fonte e contraste no topo.", href: "acessibilidade.html" },
      { terms: ["voluntario", "voluntariado", "apoiar", "doacao", "doar"], text: "O AdaptSport não recebe doações nem oferece vagas. Consulte oportunidades diretamente com organizações oficiais.", href: "envolva-se.html" },
      { terms: ["contato", "formulario", "mensagem"], text: "O formulário de contato é uma demonstração local: ele valida e salva um rascunho neste navegador, mas não transmite mensagens.", href: "contato.html" }
    ];

    form.addEventListener("submit", function (event) {
      event.preventDefault();
      var query = normalize(input.value.trim());
      if (!query) {
        answer.textContent = "Digite um assunto para procurar uma orientação.";
        input.focus();
        return;
      }
      var match = rules.find(function (rule) {
        return rule.terms.some(function (term) { return query.indexOf(term) !== -1; });
      });
      answer.replaceChildren();
      var text = document.createElement("span");
      text.textContent = match ? match.text + " " : "Não encontrei uma resposta pronta. Consulte o mapa do site ou entre em contato pelo formulário. ";
      answer.appendChild(text);
      var link = document.createElement("a");
      link.href = match ? match.href : "contato.html";
      link.textContent = match ? "Abrir esta página" : "Abrir contato";
      answer.appendChild(document.createTextNode(" "));
      answer.appendChild(link);
    });
  }

  function setupContactForm() {
    var form = document.getElementById("form-contato");
    if (!form) return;
    form.noValidate = true;

    var status = document.getElementById("form-status");
    var storageKey = "adaptsport-contato-rascunho-v1";
    var fields = Array.prototype.slice.call(form.querySelectorAll("input[name], select[name], textarea[name]"));
    var clearButton = document.getElementById("limpar-rascunho");
    var dateField = document.getElementById("data-contato");
    if (dateField) {
      var localToday = new Date();
      localToday.setMinutes(localToday.getMinutes() - localToday.getTimezoneOffset());
      dateField.min = localToday.toISOString().slice(0, 10);
    }

    function readDraft() {
      try {
        var saved = JSON.parse(localStorage.getItem(storageKey) || "{}");
        fields.forEach(function (field) {
          if (Object.prototype.hasOwnProperty.call(saved, field.name)) field.value = saved[field.name];
        });
        if (Object.keys(saved).length && status) status.textContent = "Rascunho restaurado deste navegador. Nada foi enviado.";
      } catch (error) {
        if (status) status.textContent = "O navegador não permitiu restaurar o rascunho. Você ainda pode preencher o formulário.";
      }
    }

    function saveDraft() {
      var draft = {};
      fields.forEach(function (field) { draft[field.name] = field.value; });
      try {
        localStorage.setItem(storageKey, JSON.stringify(draft));
        if (status) status.textContent = "Rascunho salvo somente neste navegador. Nada foi enviado.";
      } catch (error) {
        if (status) status.textContent = "Não foi possível salvar o rascunho neste navegador.";
      }
    }

    function errorFor(field) {
      if (!field.willValidate || field.validity.valid) return "";
      if (field.validity.valueMissing) return "Preencha este campo.";
      if (field.validity.typeMismatch && field.type === "email") return "Digite um endereço de e-mail válido.";
      if (field.validity.patternMismatch) return field.title || "Confira o formato informado.";
      if (field.validity.tooShort) return "Digite pelo menos " + field.minLength + " caracteres.";
      if (field.validity.rangeUnderflow || field.validity.rangeOverflow) return "Informe um valor dentro do intervalo permitido.";
      if (field.validity.stepMismatch) return "Informe um número inteiro.";
      return "Confira o valor informado.";
    }

    function showError(field) {
      var error = errorFor(field);
      var errorBox = document.getElementById("erro-" + field.id);
      field.setAttribute("aria-invalid", String(Boolean(error)));
      if (errorBox) errorBox.textContent = error;
      return !error;
    }

    readDraft();
    fields.forEach(function (field) {
      field.addEventListener("input", saveDraft);
      field.addEventListener("change", saveDraft);
      field.addEventListener("blur", function () { showError(field); });
    });

    form.addEventListener("submit", function (event) {
      event.preventDefault();
      var firstInvalid = null;
      var valid = fields.every(function (field) {
        var isValid = showError(field);
        if (!isValid && !firstInvalid) firstInvalid = field;
        return isValid;
      });
      if (!valid) {
        if (status) status.textContent = "Há campos que precisam de correção. Revise as mensagens indicadas.";
        firstInvalid.focus();
        return;
      }
      try { localStorage.removeItem(storageKey); } catch (error) { /* A validação continua sem armazenamento. */ }
      form.reset();
      fields.forEach(function (field) { field.removeAttribute("aria-invalid"); });
      form.querySelectorAll(".field-error").forEach(function (node) { node.textContent = ""; });
      if (status) {
        status.textContent = "Validação concluída. Como este projeto é um protótipo estático, sua mensagem não foi enviada.";
        status.focus();
      }
    });

    if (clearButton) {
      clearButton.addEventListener("click", function () {
        form.reset();
        fields.forEach(function (field) { field.removeAttribute("aria-invalid"); });
        form.querySelectorAll(".field-error").forEach(function (node) { node.textContent = ""; });
        try { localStorage.removeItem(storageKey); } catch (error) { /* Sem armazenamento, nada a remover. */ }
        if (status) status.textContent = "Rascunho apagado deste navegador.";
      });
    }
  }
})();
