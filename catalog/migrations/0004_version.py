# Generated by Django 5.0.7 on 2024-08-18 08:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0003_alter_product_options"),
    ]

    operations = [
        migrations.CreateModel(
            name="Version",
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
                ("num_ver", models.IntegerField(verbose_name="номер версии")),
                (
                    "name_ver",
                    models.CharField(max_length=50, verbose_name="название версии"),
                ),
                ("cur_ver", models.BooleanField(verbose_name="признак текущей версии")),
                (
                    "product",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="products",
                        to="catalog.product",
                    ),
                ),
            ],
            options={
                "verbose_name": "версия",
                "verbose_name_plural": "версии",
            },
        ),
    ]
