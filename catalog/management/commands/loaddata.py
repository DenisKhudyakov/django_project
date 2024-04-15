from django.core.management import BaseCommand
from catalog.models import Category, Product
import json
from typing import Any


class Command(BaseCommand):
    @staticmethod
    def json_read_categories(json_data_file: Any) -> str:
        """Функция чтения фикстуры с категориями"""
        with open(json_data_file, "r", encoding="utf-8") as fp:
            return json.load(fp)

    @staticmethod
    def json_read_products(json_data_file: Any) -> list:
        """Функция чтения фикстуры с продуктами"""
        with open(json_data_file, "r", encoding="utf-8") as fp:
            return json.load(fp)

    def handle(self, *args, **options):

        Product.objects.all().delete()
        Category.objects.all().delete()

        product_for_create: list = []
        category_for_create: list = []

        # Обходим все значения категорий из фиктсуры для получения информации об одном объекте
        for category in Command.json_read_categories('blog/catalog_data.json'):
            category_for_create.append(
                Category(name=category['fields']['name'],description=category['fields']['description'])
            )

        Category.objects.bulk_create(category_for_create)

        # работа в с моделью Product делается полностью аналогично.