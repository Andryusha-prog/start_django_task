from django.contrib import admin

from blog.models import Blog
from catalog.models import Category, Product


@admin.register(Category)  # Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "category")
    list_filter = ("category",)
    search_fields = ("name", "description")


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'tittle', 'slug', 'content', 'preview', 'create_date', 'publication')
