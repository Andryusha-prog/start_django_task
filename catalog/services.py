from catalog.models import Category
from config.settings import CACHE_ENABLED
from django.core.cache import cache

def get_category_data():
    if not CACHE_ENABLED:
        return Category.objects.all()
    key = "category_list"
    categories = cache.get(key)
    if categories is not None:
        return categories
    categories = Category.objects.all()
    cache.set(key, categories)
    return categories

