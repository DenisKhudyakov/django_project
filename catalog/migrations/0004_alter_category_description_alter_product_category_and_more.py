# Generated by Django 5.0.3 on 2024-03-28 16:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0003_remove_product_manufactured_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="description",
            field=models.TextField(verbose_name="описание"),
        ),
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="catalog.category",
                verbose_name="категория",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="created_at",
            field=models.DateField(auto_now_add=True, verbose_name="дата создания"),
        ),
        migrations.AlterField(
            model_name="product",
            name="description",
            field=models.TextField(verbose_name="описание товара"),
        ),
        migrations.AlterField(
            model_name="product",
            name="updated_at",
            field=models.DateField(
                auto_now=True, verbose_name="дата последнего изменения"
            ),
        ),
    ]
