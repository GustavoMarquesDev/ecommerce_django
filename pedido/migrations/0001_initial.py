# Generated by Django 5.2.4 on 2025-07-10 00:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Pedido",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("total", models.FloatField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("A", "Aprovado"),
                            ("C", "Criado"),
                            ("R", "Reprovado"),
                            ("P", "Pendente"),
                            ("E", "Enviado"),
                            ("F", "Finalizado"),
                        ],
                        default="C",
                        max_length=1,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Pedido",
                "verbose_name_plural": "Pedidos",
            },
        ),
        migrations.CreateModel(
            name="ItemPedido",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("produto", models.CharField(max_length=50)),
                ("produto_id", models.PositiveIntegerField()),
                ("variacao", models.CharField(max_length=255)),
                ("variacao_id", models.PositiveIntegerField()),
                ("preco", models.FloatField()),
                ("preco_promocional", models.FloatField(default=0)),
                ("quantidade", models.PositiveIntegerField()),
                ("imagem", models.ImageField(max_length=2000, upload_to="")),
                (
                    "pedido",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="pedido.pedido"
                    ),
                ),
            ],
            options={
                "verbose_name": "Item do pedido",
                "verbose_name_plural": "Itens do pedido",
            },
        ),
    ]
