from django.shortcuts import render
from django.views.generic import ListView
from django.views import View
from django.http import HttpResponse


class Pagar(View):
    def get(self, *arg, **kwargs):
        return HttpResponse("Página de teste para pagar")


class FecharPedido(View):
    def get(self, *arg, **kwargs):
        return HttpResponse("Página de teste para fechar pedido")


class Detalhe(View):
    def get(self, *arg, **kwargs):
        return HttpResponse("Página de detalhe do pedido")
