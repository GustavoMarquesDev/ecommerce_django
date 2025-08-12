from django.urls import path
from . import views

app_name = "pedido"

urlpatterns = [
    path('pagar/<int:pk>', views.Pagar.as_view(), name='pagar'),
    path('salvarpedido/', views.SalvarPedido.as_view(), name='salvarpedido'),
    path('lista/', views.Lista.as_view(), name='lista'),
    path('detalhe/<int:pk>', views.Detalhe.as_view(), name='detalhe'),
    path('deletar/<int:pk>', views.DeletarPedido.as_view(), name='deletar'),
    path('envio/<int:pk>', views.AcompanharEnvio.as_view(), name='envio'),

]
