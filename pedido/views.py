from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib import messages

from produto.models import Variacao
from .models import Pedido, ItemPedido
import utils


class Pagar(View):
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

        contexto = {}

        del self.request.session['carrinho']

        return redirect('pedido:lista')


class SalvarPedido(View):
    def get(self, *arg, **kwargs):
        return HttpResponse("Página de teste para fechar pedido")


class Detalhe(View):
    def get(self, *arg, **kwargs):
        return HttpResponse("Página de detalhe do pedido")


class Lista(View):
    def get(self, *arg, **kwargs):
        return HttpResponse("Página de lista de pedidos")
