// Controles opcionais de acessibilidade: tamanho de fonte e alto contraste.
// Progressive enhancement — o site funciona por completo sem este script.
(function () {
  var root = document.documentElement;
  var sizes = ['normal', 'grande', 'maior'];

  function applyState() {
    var size = localStorage.getItem('adaptsport-fontsize') || 'normal';
    var contrast = localStorage.getItem('adaptsport-contraste') || 'normal';
    root.setAttribute('data-fontsize', size);
    if (contrast === 'alto') {
      root.setAttribute('data-contrast', 'alto');
    } else {
      root.removeAttribute('data-contrast');
    }
    var sizeBtn = document.getElementById('btn-fonte');
    var contrastBtn = document.getElementById('btn-contraste');
    if (sizeBtn) sizeBtn.setAttribute('aria-pressed', size !== 'normal');
    if (contrastBtn) contrastBtn.setAttribute('aria-pressed', contrast === 'alto');
  }

  document.addEventListener('DOMContentLoaded', function () {
    applyState();

    var sizeBtn = document.getElementById('btn-fonte');
    if (sizeBtn) {
      sizeBtn.addEventListener('click', function () {
        var current = localStorage.getItem('adaptsport-fontsize') || 'normal';
        var next = sizes[(sizes.indexOf(current) + 1) % sizes.length];
        localStorage.setItem('adaptsport-fontsize', next);
        applyState();
      });
    }

    var contrastBtn = document.getElementById('btn-contraste');
    if (contrastBtn) {
      contrastBtn.addEventListener('click', function () {
        var current = localStorage.getItem('adaptsport-contraste') || 'normal';
        localStorage.setItem('adaptsport-contraste', current === 'alto' ? 'normal' : 'alto');
        applyState();
      });
    }
  });
})();
