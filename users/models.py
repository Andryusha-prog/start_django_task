from django.contrib.auth.models import AbstractUser
from django.db import models
from django.shortcuts import render

# Create your views here.


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email')
    phone = models.CharField(max_length=15, verbose_name='телефон', blank=True, null=True)
    avatar = models.ImageField(upload_to='users/avatars', verbose_name='аватар', blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True, verbose_name='страна')

    token = models.CharField(max_length=100, blank=True, null=True, verbose_name='token')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email
