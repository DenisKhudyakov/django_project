# Generated by Django 5.0.3 on 2024-04-20 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="country",
            field=models.CharField(
                blank=True,
                help_text="Введите страну",
                max_length=12,
                null=True,
                verbose_name="country",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="number_tel",
            field=models.CharField(
                blank=True,
                help_text="Введите номер телефона",
                max_length=11,
                null=True,
                unique=True,
                verbose_name="telephone_number",
            ),
        ),
    ]
