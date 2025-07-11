from django.template import Library
from utils import formata_preco

register = Library()


@register.filter
def formata_preco_filter(valor):
    return formata_preco(valor)
