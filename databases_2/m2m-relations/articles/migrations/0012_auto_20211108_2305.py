# Generated by Django 3.1.2 on 2021-11-08 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0011_auto_20211108_2301'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='relationship',
            name='is_main',
        ),
        migrations.AddField(
            model_name='scope',
            name='is_main',
            field=models.BooleanField(default=False, verbose_name='Основной тег'),
        ),
    ]
