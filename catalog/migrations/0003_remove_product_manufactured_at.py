# Generated by Django 5.0.3 on 2024-03-16 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_product_manufactured_at"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="manufactured_at",
        ),
    ]
