# Generated by Django 5.0.3 on 2024-03-28 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Blog",
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
                ("title", models.CharField(max_length=50, verbose_name="заголовок")),
                ("slug", models.CharField(max_length=50, verbose_name="URL")),
                ("content", models.TextField(verbose_name="содержимое")),
                (
                    "preview",
                    models.ImageField(
                        blank=True, null=True, upload_to="blog/", verbose_name="превью"
                    ),
                ),
                (
                    "date_created",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="дата создания"
                    ),
                ),
                (
                    "publication",
                    models.BooleanField(default=True, verbose_name="факт публикации"),
                ),
                (
                    "views",
                    models.IntegerField(
                        default=0, verbose_name="количество просмотров"
                    ),
                ),
            ],
            options={
                "verbose_name": "блог",
                "verbose_name_plural": "блоги",
            },
        ),
    ]