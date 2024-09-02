from django.db import models

from users.models import User


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(verbose_name='описание', blank=True, null=True)

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return f'{self.name} - {self.description}'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(verbose_name='описание', blank=True, null=True)
    image = models.ImageField(upload_to='products/photo', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True, related_name='categories')
    price = models.FloatField(verbose_name='цена за покупку')
    created_at = models.DateTimeField(verbose_name='дата создания', blank=True, null=True)
    updated_at = models.DateTimeField(verbose_name='дата послденего изменения', blank=True, null=True)
    owner = models.ForeignKey(User, null=True, blank=True, verbose_name='Пользователь', on_delete=models.SET_NULL)
    is_publicate = models.BooleanField(verbose_name='Признак публикации', default=False)

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ['pk']
        permissions = [
            ('can_change_publicate', 'can change publicate pr'),
            ('can_change_description_product', 'can change publication product'),
            ('can_change_category_product', 'can change category product')
        ]

    def __str__(self):
        return f'{self.name} - {self.price}'


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True, related_name='products')
    num_ver = models.IntegerField(verbose_name='номер версии')
    name_ver = models.CharField(max_length=50, verbose_name='название версии')
    cur_ver = models.BooleanField(verbose_name='признак текущей версии')

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'

    def __str__(self):
        return f'Версия {self.num_ver}: {self.name_ver}'
