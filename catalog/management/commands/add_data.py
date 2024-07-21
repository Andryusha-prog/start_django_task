import json

from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        # Здесь мы получаем данные из фикстурв с категориями
        with open('catalog.json', 'r') as json_file:
            data = json.load(json_file)
        return [item for item in data if item["model"] == "catalog.category"]

    @staticmethod
    def json_read_products():
        # Здесь мы получаем данные из фикстурв с продуктами
        with open('catalog.json', 'r') as json_file:
            data = json.load(json_file)
        return [item for item in data if item["model"] == "catalog.product"]

    def handle(self, *args, **options):
        # Удалите все продукты
        Product.objects.all().delete()
        # Удалите все категории
        Category.objects.all().delete()

        # Создайте списки для хранения объектов
        product_for_create = []
        category_for_create = []

        # Обходим все значения категорий из фиктсуры для получения информации об одном объекте
        for category in Command.json_read_categories():
            category_for_create.append(
                Category(name=category['fields']['name'],
                         description=category['fields']['description'],
                         pk=category['pk'])
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Category.objects.bulk_create(category_for_create)

        # Обходим все значения продуктов из фиктсуры для получения информации об одном объекте
        for product in Command.json_read_products():
            product_for_create.append(
                Product(name=product['fields']['name'],
                        description=product['fields']['description'],
                        image=product['fields']['image'],
                        category=Category.objects.get(id=product['fields']['category']),
                        price=product['fields']['price'],
                        created_at=product['fields']['created_at'],
                        updated_at=product['fields']['updated_at'],
                        pk=product['pk']
                        )
            )

            # Создаем объекты в базе с помощью метода bulk_create()
        Product.objects.bulk_create(product_for_create)

