(function () {
  document.addEventListener("DOMContentLoaded", function () {
    const select = document.getElementById("select-variacoes");
    const estoqueInfo = document.getElementById("estoque-variacao");

    if (select && estoqueInfo) {
      function updateEstoque() {
        const selected = select.options[select.selectedIndex];
        const estoque = parseInt(selected.getAttribute("data-estoque"), 10);
        if (estoque < 5) {
          estoqueInfo.innerHTML = `<span style="color: #d9534f; font-weight: bold;">Últimas ${estoque} unidades!</span>`;
        } else {
          estoqueInfo.textContent = "Quantidade em estoque: " + estoque;
        }
      }

      select.addEventListener("change", updateEstoque);
      updateEstoque(); // Atualiza ao carregar a página
    }
  });
})();
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

// Script para atualizar quantidade no carrinho
(function () {
  document.addEventListener("DOMContentLoaded", function () {
    // Interceptar cliques nos botões + e -
    document
      .querySelectorAll('a[href*="atualizarquantidade"]')
      .forEach(function (link) {
        link.addEventListener("click", function (e) {
          e.preventDefault();

          const url = this.getAttribute("href");
          const variacaoId = this.getAttribute("href").match(/vid=(\d+)/)[1];
          const acao = this.getAttribute("href").match(/acao=(\w+)/)[1];

          // Fazer requisição AJAX
          fetch(url)
            .then((response) => {
              if (response.ok) {
                // Recarregar a página para mostrar as mudanças
                window.location.reload();
              } else {
                console.error("Erro ao atualizar quantidade");
              }
            })
            .catch((error) => {
              console.error("Erro:", error);
            });
        });
      });
  });
})();

// Payment Method Selection
document.addEventListener("DOMContentLoaded", function () {
  const paymentCards = document.querySelectorAll(".payment-method-card");

  paymentCards.forEach((card) => {
    card.addEventListener("click", function () {
      // Remove selected class from all cards
      paymentCards.forEach((c) => c.classList.remove("selected"));

      // Add selected class to clicked card
      this.classList.add("selected");

      // You can add additional logic here, like updating a hidden input
      // or enabling/disabling the pay button
    });
  });

  // Add hover effects for better UX
  paymentCards.forEach((card) => {
    card.addEventListener("mouseenter", function () {
      if (!this.classList.contains("selected")) {
        this.style.transform = "translateY(-5px)";
      }
    });

    card.addEventListener("mouseleave", function () {
      if (!this.classList.contains("selected")) {
        this.style.transform = "translateY(0)";
      }
    });
  });
});

// Smooth scrolling for anchor links
document.addEventListener("DOMContentLoaded", function () {
  const links = document.querySelectorAll('a[href^="#"]');

  links.forEach((link) => {
    link.addEventListener("click", function (e) {
      e.preventDefault();

      const targetId = this.getAttribute("href");
      const targetElement = document.querySelector(targetId);

      if (targetElement) {
        targetElement.scrollIntoView({
          behavior: "smooth",
          block: "start",
        });
      }
    });
  });
});

// Add loading states to buttons
document.addEventListener("DOMContentLoaded", function () {
  const payButton = document.querySelector(".pagar-btn");

  if (payButton) {
    payButton.addEventListener("click", function (e) {
      // Add loading state
      this.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Processando...';
      this.disabled = true;

      // Simulate processing (remove this in production)
      setTimeout(() => {
        this.innerHTML = "Pagar";
        this.disabled = false;
      }, 2000);
    });
  }
});

// Table row hover effects
document.addEventListener("DOMContentLoaded", function () {
  const tableRows = document.querySelectorAll(
    ".pedidos-table tbody tr, .produtos-table tbody tr"
  );

  tableRows.forEach((row) => {
    row.addEventListener("mouseenter", function () {
      this.style.transform = "translateY(-2px)";
    });

    row.addEventListener("mouseleave", function () {
      this.style.transform = "translateY(0)";
    });
  });
});

// Status badge animations
document.addEventListener("DOMContentLoaded", function () {
  const statusBadges = document.querySelectorAll(".pedido-status");

  statusBadges.forEach((badge) => {
    badge.addEventListener("mouseenter", function () {
      this.style.transform = "scale(1.05)";
    });

    badge.addEventListener("mouseleave", function () {
      this.style.transform = "scale(1)";
    });
  });
});
