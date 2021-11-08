from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Scope(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    articles = models.ManyToManyField(Article, through='Relationship')

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class Relationship(models.Model):
    scope = models.ForeignKey(Scope, on_delete=models.CASCADE, verbose_name='Теги')
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    is_main = models.BooleanField(verbose_name='Основной тег', default=False)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.scope.name
