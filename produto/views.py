from django.shortcuts import redirect, get_object_or_404, render
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

        # para remover do carrinho, descomente as linhas abaixo
        # if self.request.session.get('carrinho'):
        #     del self.request.session['carrinho']
        #     self.request.session.save()

        # para voltar para a página anterior, ous a home aqui no caso
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
            messages.error(self.request, "Estoque insuficiente ")
            return redirect(http_referer)

        if not self.request.session.get('carrinho'):
            self.request.session['carrinho'] = {}
            self.request.session.save()

        carrinho = self.request.session['carrinho']

        if variacao_id in carrinho:
            quantidade_carrinho = carrinho[variacao_id]['quantidade']
            quantidade_carrinho += 1

            if variacao.estoque < quantidade_carrinho:
                messages.error(
                    self.request,
                    f'Infelizmente nosso estoque do produto "{produto_nome}" '
                    f'acabou. Adicionamos {variacao.estoque} itens do produto '
                    f'ao seu carrinho.'
                )
                quantidade_carrinho = variacao.estoque

            carrinho[variacao_id]['quantidade'] = quantidade_carrinho
            carrinho[variacao_id]['preco_quantitativo'] = preco_unitario * \
                quantidade_carrinho
            carrinho[variacao_id]['preco_quantitativo_promocional'] = preco_unitario_promocional * \
                quantidade_carrinho

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

        self.request.session.save()

        messages.success(
            self.request,
            f'Produto {produto_nome} {variacao_nome} adicionado ao carrinho'
            f' com sucesso! {carrinho[variacao_id]["quantidade"]}x'
        )

        return redirect(http_referer)


class RemoverDoCarrinho(View):
    def get(self, *arg, **kwargs):
        return HttpResponse("Página de teste para remover do carrinho")


class Carrinho(View):
    def get(self, *arg, **kwargs):
        contexto = {
            'carrinho': self.request.session.get('carrinho', {}),
        }
        return render(self.request, 'produto/carrinho.html', contexto)


class Finalizar(View):
    def get(self, *arg, **kwargs):
        return HttpResponse("Página de finalização de compra")
