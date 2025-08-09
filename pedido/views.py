from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import DetailView, ListView
from django.views import View
from django.http import HttpResponse
from django.contrib import messages

from produto.models import Variacao
from .models import Pedido, ItemPedido
import utils


class DispatchLoginRequiredMixin(View):
    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('perfil:criar')

        return super().dispatch(*args, **kwargs)

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)  # type: ignore
        qs = qs.filter(usuario=self.request.user)

        return super().get_queryset()  # type: ignore


class Pagar(DispatchLoginRequiredMixin, DetailView):
    template_name = 'pedido/pagar.html'
    model = Pedido
    pk_url_kwarg = 'pk'
    context_object_name = 'pedido'


class SalvarPedido(View):
    template_name = 'pedido/pagar.html'

    def get(self, *arg, **kwargs):
        if not self.request.user.is_authenticated:
            messages.error(
                self.request,
                'Você precisa estar logado para realizar esta ação.'
            )
            return redirect('perfil:criar')

        if not self.request.session.get('carrinho'):
            messages.error(
                self.request,
                'Carrinho vazio..'
            )
            return redirect('produto:lista')

        carrinho = self.request.session.get('carrinho', {})

        carrinho_variacao_ids = [v for v in carrinho]
        bd_variacoes = list(
            Variacao.objects.filter(id__in=carrinho_variacao_ids)
        )

        for variacao in bd_variacoes:
            vid = str(variacao.pk)

            estoque = variacao.estoque
            quantidade_carrinho = carrinho[vid]['quantidade']
            preco_unitario = carrinho[vid]['preco_unitario']
            preco_unitario_promocional = carrinho[vid]['preco_unitario_promocional']

            erro_msg_estoque = ''

            if estoque < quantidade_carrinho:
                carrinho[vid]['quantidade'] = estoque
                carrinho[vid]['preco_quantitativo'] = estoque * preco_unitario
                carrinho[vid]['preco_quantitativo_promocional'] = estoque * \
                    preco_unitario_promocional

                erro_msg_estoque = 'Estoque insuficiente para alguns itens do carrinho. ' \
                    'Nos desculpe, mas reduzimos a quantidade destes produtos, ' \
                    'Favor verifique quais itens estão faltando.'

            if erro_msg_estoque:
                messages.error(
                    self.request,
                    erro_msg_estoque
                )
                self.request.session.save()

                return redirect('produto:carrinho')

        qtd_total_carrinho = utils.cart_total_qtd(carrinho)
        valor_total_carrinho = utils.cart_total_price(carrinho)

        pedido = Pedido(
            usuario=self.request.user,
            total=valor_total_carrinho,
            qtd_total=qtd_total_carrinho,
            status='C'
        )
        pedido.save()

        ItemPedido.objects.bulk_create([
            ItemPedido(
                pedido=pedido,
                produto=v['produto_nome'],
                produto_id=v['produto_id'],
                variacao=v['variacao_nome'],
                variacao_id=v['variacao_id'],
                preco=v['preco_quantitativo'],
                preco_promocional=v['preco_quantitativo_promocional'],
                quantidade=v['quantidade'],
                imagem=v['imagem']
            ) for v in carrinho.values()
        ])

        del self.request.session['carrinho']

        return redirect(
            reverse(
                'pedido:pagar',
                kwargs={
                    'pk': pedido.pk
                }
            )
        )


class Detalhe(DispatchLoginRequiredMixin, DetailView):
    template_name = 'pedido/detalhe.html'
    model = Pedido
    context_object_name = 'pedido'
    pk_url_kwarg = 'pk'


class Lista(DispatchLoginRequiredMixin, ListView):
    template_name = 'pedido/lista.html'
    model = Pedido
    context_object_name = 'pedidos'
    paginate_by = 10
    ordering = ['-id']


class DeletarPedido(DispatchLoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        pedido_id = self.kwargs.get('pk')
        pedido = get_object_or_404(
            Pedido, pk=pedido_id, usuario=self.request.user)

        # Deletar o pedido
        pedido.delete()

        messages.success(
            self.request,
            f'Pedido #{pedido_id} foi deletado com sucesso!'
        )

        return redirect('pedido:lista')
