// Preferências acessíveis do AdaptSport: fonte e alto contraste.
// As preferências permanecem locais neste navegador e não são enviadas a servidores.
(function () {
  "use strict";

  var root = document.documentElement;
  var sizes = ["normal", "grande", "maior"];
  var fontKey = "adaptsport-fontsize";
  var contrastKey = "adaptsport-contraste";

  function read(key, fallback) {
    try {
      return localStorage.getItem(key) || fallback;
    } catch (error) {
      return fallback;
    }
  }

  function write(key, value) {
    try {
      localStorage.setItem(key, value);
      return true;
    } catch (error) {
      return false;
    }
  }

  function applyState() {
    var size = read(fontKey, "normal");
    var contrast = read(contrastKey, "normal");
    if (!sizes.includes(size)) size = "normal";

    root.setAttribute("data-fontsize", size);
    if (contrast === "alto") root.setAttribute("data-contrast", "alto");
    else root.removeAttribute("data-contrast");

    var sizeButton = document.getElementById("btn-fonte");
    var contrastButton = document.getElementById("btn-contraste");
    if (sizeButton) {
      sizeButton.setAttribute("aria-pressed", String(size !== "normal"));
      sizeButton.setAttribute("aria-label", "Aumentar ou redefinir tamanho do texto. Nível atual: " + size);
    }
    if (contrastButton) contrastButton.setAttribute("aria-pressed", String(contrast === "alto"));
  }

  document.addEventListener("DOMContentLoaded", function () {
    applyState();

    var sizeButton = document.getElementById("btn-fonte");
    if (sizeButton) {
      sizeButton.addEventListener("click", function () {
        var current = read(fontKey, "normal");
        var next = sizes[(sizes.indexOf(current) + 1) % sizes.length];
        write(fontKey, next);
        applyState();
      });
    }

    var contrastButton = document.getElementById("btn-contraste");
    if (contrastButton) {
      contrastButton.addEventListener("click", function () {
        write(contrastKey, read(contrastKey, "normal") === "alto" ? "normal" : "alto");
        applyState();
      });
    }
  });
})();
