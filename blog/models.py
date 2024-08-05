from django.db import models


# Create your models here.
class Blog(models.Model):
    tittle = models.CharField(max_length=150, verbose_name='Заголовок')
    slug = models.CharField(max_length=150, verbose_name='адрес', blank=True, null=True)
    content = models.TextField(verbose_name='содержимое')
    preview = models.ImageField(upload_to='blog/photo', blank=True, null=True)
    create_date = models.DateTimeField(verbose_name='дата создания', blank=True, null=True)
    publication = models.BooleanField(verbose_name='признк публикации')
    view_count = models.PositiveIntegerField(verbose_name='счетчик просмотров', default=0)

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'записи'

    def __str__(self):
        return f'{self.tittle}'
