from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from django.views import View


class Criar(View):
    def get(self, *arg, **kwargs):
        return HttpResponse("Página de teste para criar perfil")


class Atualizar(View):
    def get(self, *arg, **kwargs):
        return HttpResponse("Página de teste para atualizar perfil")


class Login(View):
    def get(self, *arg, **kwargs):
        return HttpResponse("Página de teste para login")


class Logout(View):
    def get(self, *arg, **kwargs):
        return HttpResponse("Página de teste para logout")
