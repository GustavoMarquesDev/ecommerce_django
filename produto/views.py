from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views import View
from django.contrib import messages

from .models import Produto, Variacao

PER_PAGE = 9


class ListaProdutos(ListView):
    model = Produto
    template_name = 'produto/lista.html'
    context_object_name = 'produtos'
    paginate_by = PER_PAGE


class DetalheProduto(DetailView):
    model = Produto
    template_name = 'produto/detalhe.html'
    context_object_name = 'produto'
    slug_url_kwarg = 'slug'


class AdicionarAoCarrinho(View):
    def get(self, *arg, **kwargs):

        http_referer = self.request.META.get(
            'HTTP_REFERER', reverse('produto:lista')
        )

        variacao_id = self.request.GET.get('vid')

        if not variacao_id:
            messages.error(self.request, "Você precisa selecionar uma opção")
            return redirect(http_referer)

        variacao = get_object_or_404(Variacao, id=variacao_id)
        produto = variacao.produto

        produto_id = produto.id  # type: ignore
        produto_nome = produto.nome
        variacao_nome = variacao.nome or ''
        variacao_id = variacao.id  # type: ignore
        preco_unitario = variacao.preco
        preco_unitario_promocional = variacao.preco_promocional
        quantidade = 1
        slug = produto.slug
        imagem = produto.imagem

        if imagem:
            imagem = imagem.name
        else:
            imagem = ''

        if variacao.estoque < 1:
            messages.error(self.request, "Estoque insuficiente")
            return redirect(http_referer)

        if not self.request.session.get('carrinho'):
            self.request.session['carrinho'] = {}
            self.request.session.save()

        carrinho = self.request.session['carrinho']

        if variacao_id in carrinho:
            pass
        else:
            carrinho[variacao_id] = {
                'produto_id': produto_id,
                'produto_nome': produto_nome,
                'variacao_nome': variacao_nome,
                'variacao_id': variacao_id,
                'preco_unitario': preco_unitario,
                'preco_unitario_promocional': preco_unitario_promocional,
                'preco_quantitativo': preco_unitario,
                'preco_quantitativo_promocional': preco_unitario_promocional,
                'quantidade': 1,
                'slug': slug,
                'imagem': imagem,
            }

        return HttpResponse(f'Variação: {variacao.produto} {variacao.nome}')


class RemoverDoCarrinho(View):
    def get(self, *arg, **kwargs):
        return HttpResponse("Página de teste para remover do carrinho")


class Carrinho(View):
    def get(self, *arg, **kwargs):
        return HttpResponse("Página de carrinho")


class Finalizar(View):
    def get(self, *arg, **kwargs):
        return HttpResponse("Página de finalização de compra")
