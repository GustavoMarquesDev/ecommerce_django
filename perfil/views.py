from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.views import View
from django.contrib.auth.models import User
import copy

from . import forms
from . import models


class BasePerfil(View):
    template_name = 'perfil/criar.html'

    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)

        self.carrinho = copy.deepcopy(self.request.session.get('carrinho', {}))

        self.perfil = None

        if self.request.user.is_authenticated:
            self.perfil = models.Perfil.objects.filter(
                usuario=self.request.user
            ).first()

            self.contexto = {
                'userform': forms.UserForm(
                    data=self.request.POST or None,
                    usuario=self.request.user,
                    instance=self.request.user,
                ),
                'perfilform': forms.PerfilForm(
                    data=self.request.POST or None,
                    instance=self.perfil
                )
            }

        else:
            self.contexto = {
                'userform': forms.UserForm(data=self.request.POST or None),
                'perfilform': forms.PerfilForm(data=self.request.POST or None),
            }

        self.userform = self.contexto['userform']
        self.perfilform = self.contexto['perfilform']

        self.renderizar = render(
            self.request, self.template_name, self.contexto)

    def get(self, *arg, **kwargs):
        return self.renderizar


class Criar(BasePerfil):
    def post(self, *arg, **kwargs):
        if not self.userform.is_valid() or not self.perfilform.is_valid():
            messages.error(
                self.request,
                'Existem erros no formulário de cadastro. Verifique se todos '
                'os campos foram preenchidos corretamente.'
            )

            return self.renderizar

        username = self.userform.cleaned_data.get('username')
        password = self.userform.cleaned_data.get('password')
        email = self.userform.cleaned_data.get('email')
        first_name = self.userform.cleaned_data.get('first_name')
        last_name = self.userform.cleaned_data.get('last_name')

        # Usuario estando logado
        if self.request.user.is_authenticated:
            usuario = get_object_or_404(
                User, username=self.request.user.username
            )
            usuario.username = username

            if password:
                usuario.set_password(password)

            usuario.email = email  # type: ignore
            usuario.first_name = first_name  # type: ignore
            usuario.last_name = last_name  # type: ignore
            usuario.save()

        # Usuario não logado
        else:
            usuario = self.userform.save(commit=False)
            usuario.set_password(password)
            usuario.save()

            perfil = self.perfilform.save(commit=False)
            perfil.usuario = usuario
            perfil.save()

        self.request.session['carrinho'] = self.carrinho
        self.request.session.save()
        return self.renderizar


class Atualizar(View):
    def get(self, *arg, **kwargs):
        return HttpResponse("Página de teste para atualizar perfil")


class Login(View):
    def get(self, *arg, **kwargs):
        return HttpResponse("Página de teste para login")


class Logout(View):
    def get(self, *arg, **kwargs):
        return HttpResponse("Página de teste para logout")
