// Função para aplicar máscara de CEP
function mascaraCEP(input) {
  let value = input.value.replace(/\D/g, ""); // Remove caracteres não numéricos

  // Limita a 8 dígitos
  if (value.length > 8) {
    value = value.substring(0, 8);
  }

  // Aplica a máscara
  if (value.length > 5) {
    value = value.replace(/^(\d{5})(\d{0,3})/, "$1-$2");
  }

  input.value = value;
}

// Função para aplicar máscara de CPF
function mascaraCPF(input) {
  let value = input.value.replace(/\D/g, ""); // Remove caracteres não numéricos

  // Limita a 11 dígitos
  if (value.length > 11) {
    value = value.substring(0, 11);
  }

  // Aplica a máscara
  if (value.length > 0) {
    value = value.replace(/(\d{3})(\d)/, "$1.$2");
    value = value.replace(/(\d{3})(\d)/, "$1.$2");
    value = value.replace(/(\d{3})(\d{1,2})$/, "$1-$2");
  }

  input.value = value;
}

// Função para remover máscaras (para enviar apenas números)
function removerMascaraCEP(value) {
  return value.replace(/\D/g, "");
}

function removerMascaraCPF(value) {
  return value.replace(/\D/g, "");
}

// Aplicar máscaras quando o documento estiver carregado
document.addEventListener("DOMContentLoaded", function () {
  // Aplicar máscara em campos CEP existentes
  const cepInputs = document.querySelectorAll(
    'input[name="cep"], input[id*="cep"], input[placeholder*="CEP"], input[placeholder*="cep"]'
  );
  cepInputs.forEach(function (input) {
    // Aplica máscara se o campo não estiver vazio
    if (input.value) {
      mascaraCEP(input);
    }

    input.addEventListener("input", function () {
      mascaraCEP(this);
    });

    input.addEventListener("blur", function () {
      if (this.value && this.value.replace(/\D/g, "").length !== 8) {
        this.style.borderColor = "#dc3545";
      } else {
        this.style.borderColor = "#007bff";
      }
    });
  });

  // Aplicar máscara em campos CPF existentes
  const cpfInputs = document.querySelectorAll(
    'input[name="cpf"], input[id*="cpf"], input[placeholder*="CPF"], input[placeholder*="cpf"]'
  );
  cpfInputs.forEach(function (input) {
    // Aplica máscara se o campo não estiver vazio
    if (input.value) {
      mascaraCPF(input);
    }

    input.addEventListener("input", function () {
      mascaraCPF(this);
    });

    input.addEventListener("blur", function () {
      if (this.value && this.value.replace(/\D/g, "").length !== 11) {
        this.style.borderColor = "#dc3545";
      } else {
        this.style.borderColor = "#007bff";
      }
    });
  });
});

// Função global para aplicar máscaras em campos dinamicamente criados
window.aplicarMascaras = function () {
  // Reaplica as máscaras em todos os campos
  const cepInputs = document.querySelectorAll(
    'input[name="cep"], input[id*="cep"], input[placeholder*="CEP"], input[placeholder*="cep"]'
  );
  cepInputs.forEach(function (input) {
    if (!input.hasAttribute("data-mascara-aplicada")) {
      input.setAttribute("data-mascara-aplicada", "true");
      input.addEventListener("input", function () {
        mascaraCEP(this);
      });
    }
  });

  const cpfInputs = document.querySelectorAll(
    'input[name="cpf"], input[id*="cpf"], input[placeholder*="CPF"], input[placeholder*="cpf"]'
  );
  cpfInputs.forEach(function (input) {
    if (!input.hasAttribute("data-mascara-aplicada")) {
      input.setAttribute("data-mascara-aplicada", "true");
      input.addEventListener("input", function () {
        mascaraCPF(this);
      });
    }
  });
};
