# Generated by Django 5.0.7 on 2024-08-05 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='адрес'),
        ),
    ]
