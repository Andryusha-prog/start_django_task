from django.db import models


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

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ['pk']

    def __str__(self):
        return f'{self.name} - {self.price}'

