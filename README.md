# 🛒 E-commerce em Django

Este projeto é um **e-commerce** desenvolvido com **Django 3.1.6**, contendo funcionalidades completas para autenticação, gerenciamento de pedidos, carrinho de compras e listagem de produtos.

## 🚀 Funcionalidades

- **Autenticação de usuários**

  - Login e logout
  - Cadastro de conta
  - Atualização de dados do perfil

- **Catálogo de produtos**

  - Listagem de todos os produtos disponíveis
  - Busca de produtos pelo nome
  - Visualização detalhada de um produto

- **Carrinho de compras**

  - Adicionar e remover itens do carrinho
  - Atualizar quantidades
  - Resumo da compra antes de finalizar

- **Pedidos**
  - Finalização de compra
  - Visualizar histórico de pedidos concluídos
  - Detalhes de cada pedido finalizado

## 🛠 Tecnologias utilizadas

- [Django 3.1.6](https://docs.djangoproject.com/en/3.1/) — Framework web principal
- [django-crispy-forms 1.9.0](https://django-crispy-forms.readthedocs.io/) — Formulários mais organizados e estilizados
- [django-debug-toolbar 2.2](https://django-debug-toolbar.readthedocs.io/) — Ferramenta para debug e otimização durante o desenvolvimento
- [Pillow 7.1.1](https://pillow.readthedocs.io/) — Manipulação de imagens (usado para fotos de produtos)

## 📦 Instalação e execução

1. **Clonar o repositório**

   ```bash
   git clone git@github.com:GustavoMarquesDev/ecommerce_django.git
   cd ecommerce_django
   ```

2. **Criar e ativar um ambiente virtual**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. **Instalar as dependências**

   ```bash
   pip install -r requirements.txt
   ```

4. **Executar migrações**

   ```bash
   python manage.py migrate
   ```

5. **Criar superusuário**

   ```bash
   python manage.py createsuperuser
   ```

6. **Executar o servidor**

   ```bash
   python manage.py runserver
   ```

7. Acesse no navegador:
   ```
   http://127.0.0.1:8000
   ```

## 📂 Estrutura do projeto (exemplo)

```
ecommerce/
├── pedido/             # App de pedidos, detalhes e pagamento
├── perfil/            # App de perfil, criação e atualização
├── produto/            # App de listagem e detalhes de produtos
├── manage.py
├── project/           # Configurações do projeto
├── utils/            # Funções utilitárias, como validação de cpf, redimencionamento de imagens, etc.
└── templates/           # Templates HTML reusáveis e arquivos estaticos
```

## 💡 Observações

- Certifique-se de configurar corretamente o `MEDIA_URL` e `MEDIA_ROOT` no `settings.py` para upload de imagens.
- O `django-debug-toolbar` deve ser usado apenas em **ambiente de desenvolvimento**.
- O banco de dados padrão é SQLite, mas pode ser alterado no `settings.py`.

---

📌 **Autor:** [Gustavo Marques](https://github.com/GustavoMarquesDev)
