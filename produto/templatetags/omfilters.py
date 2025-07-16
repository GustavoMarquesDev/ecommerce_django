from django.template import Library
import utils

register = Library()


@register.filter
def formata_preco(valor):
    return utils.formata_preco(valor)
