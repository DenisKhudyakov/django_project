# Generated by Django 5.0.3 on 2024-03-16 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_remove_product_manufactured_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="created_at",
            field=models.DateField(auto_now_add=True, verbose_name="дата создания"),
        ),
        migrations.AlterField(
            model_name="product",
            name="updated_at",
            field=models.DateField(
                auto_now=True, verbose_name="дата последнего изменения"
            ),
        ),
    ]
