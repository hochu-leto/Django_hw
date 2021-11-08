# Generated by Django 3.1.2 on 2021-11-08 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_auto_20211106_2125'),
    ]

    operations = [
        migrations.RenameField(
            model_name='relationship',
            old_name='scopes',
            new_name='scope',
        ),
        migrations.RemoveField(
            model_name='scope',
            name='article',
        ),
        migrations.AddField(
            model_name='scope',
            name='articles',
            field=models.ManyToManyField(through='articles.Relationship', to='articles.Article'),
        ),
    ]
