# Generated by Django 3.1.2 on 2021-11-08 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0010_auto_20211108_0800'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scope',
            name='articles',
        ),
        migrations.AddField(
            model_name='article',
            name='scope',
            field=models.ManyToManyField(through='articles.Relationship', to='articles.Scope'),
        ),
    ]
