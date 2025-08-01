from django.db import models
from django.utils.text import slugify

from utils import resize_image, formata_preco


class Produto(models.Model):
    nome = models.CharField(max_length=50)
    descricao_curta = models.TextField(max_length=255)
    descricao_longa = models.TextField()
    imagem = models.ImageField(
        upload_to="produto_imagens/%Y/%m/%d",
        blank=True,
        null=True,
    )
    slug = models.SlugField(unique=True, blank=True, null=True)
    preco_marketing = models.FloatField(verbose_name="Preço")
    preco_marketing_promocional = models.FloatField(
        default=0, verbose_name="Preço Promo."
    )
    tipo = models.CharField(
        default="V",
        max_length=1,
        choices=(
            ("V", "Variavel"),
            ("S", "Simples"),
        )
    )

    def get_preco_formatado(self):
        return formata_preco(self.preco_marketing)
    get_preco_formatado.short_description = "Preço"  # type: ignore

    def get_preco_promocional_formatado(self):
        return formata_preco(self.preco_marketing_promocional)
    get_preco_promocional_formatado.short_description = "Preço Promo."  # type: ignore

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = f'{slugify(self.nome)}'
            self.slug = slug

        super().save(*args, **kwargs)

        if self.imagem:
            resize_image(self.imagem)  # type: ignore

    def __str__(self):
        return self.nome


class Variacao(models.Model):

    class Meta:
        verbose_name = "Variação"
        verbose_name_plural = "Variações"

    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50, blank=True, null=True)
    preco = models.FloatField()
    preco_promocional = models.FloatField(default=0)
    estoque = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.nome or self.produto.nome
