from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from django.views import View

from .models import Produto

PER_PAGE = 10


class ListaProdutos(ListView):
    model = Produto
    template_name = 'produto/lista.html'
    context_object_name = 'produtos'
    paginate_by = PER_PAGE


class DetalheProduto(View):
    def get(self, *arg, **kwargs):
        return HttpResponse("Página de detalhe do produto")


class AdicionarAoCarrinho(View):
    def get(self, *arg, **kwargs):
        return HttpResponse("Página de teste para adicionar ao carrinho")


class RemoverDoCarrinho(View):
    def get(self, *arg, **kwargs):
        return HttpResponse("Página de teste para remover do carrinho")


class Carrinho(View):
    def get(self, *arg, **kwargs):
        return HttpResponse("Página de carrinho")


class Finalizar(View):
    def get(self, *arg, **kwargs):
        return HttpResponse("Página de finalização de compra")
