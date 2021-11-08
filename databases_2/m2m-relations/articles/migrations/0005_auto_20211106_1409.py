# Generated by Django 3.1.2 on 2021-11-06 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20211106_1028'),
    ]

    operations = [
        migrations.AddField(
            model_name='object',
            name='article',
            field=models.ManyToManyField(through='articles.Relationship', to='articles.Article'),
        ),
        migrations.AlterField(
            model_name='relationship',
            name='object',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.object', verbose_name='Теги'),
        ),
    ]
