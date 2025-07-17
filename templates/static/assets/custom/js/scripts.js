(function () {
  select_variacao = document.getElementById("select-variacoes");
  variation_preco = document.getElementById("variation-preco");
  variation_preco_promocional = document.getElementById(
    "variation-preco-promocional"
  );
  variation_preco_antigo = document.getElementById("variation-preco-antigo");

  if (!select_variacao) {
    return;
  }
  if (!variation_preco) {
    return;
  }

  function atualizarPrecos() {
    var selectedOption = select_variacao.options[select_variacao.selectedIndex];
    var preco = selectedOption.getAttribute("data-preco");
    var preco_promocional = selectedOption.getAttribute(
      "data-preco-promocional"
    );

    if (preco_promocional && preco_promocional !== "") {
      // Mostra preço promocional e preço antigo
      variation_preco_promocional.style.display = "inline";
      variation_preco_promocional.textContent = preco_promocional;
      variation_preco.style.display = "none";
      variation_preco_antigo.style.display = "inline";
      variation_preco_antigo.textContent = preco;
    } else {
      // Mostra só o preço normal
      variation_preco_promocional.style.display = "none";
      variation_preco_antigo.style.display = "none";
      variation_preco.style.display = "inline";
      variation_preco.textContent = preco;
    }
  }

  // Inicializa ao carregar
  atualizarPrecos();
  // Atualiza ao trocar variação
  select_variacao.addEventListener("change", atualizarPrecos);
})();
