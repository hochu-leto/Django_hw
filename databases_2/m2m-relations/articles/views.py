from pprint import pprint

from django.views.generic import ListView
from django.shortcuts import render

from articles.models import Article, Relationship


def articles_list(request):
    template = 'articles/news.html'
    context = {
        'object_list': Article.objects.all()
    }
    pprint(Article.objects.all()[1].scope)#.prefetch_related('scopes'))
    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = '-published_at'

    return render(request, template, context)
