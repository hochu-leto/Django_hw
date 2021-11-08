from pprint import pprint

from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope
from .models import Relationship


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_tags_count = 0
        false_and_true = {False: 0, True: 1}
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            if form.cleaned_data:
                main_tags_count += false_and_true[form.cleaned_data['is_main']]

        if main_tags_count > 1:
            raise ValidationError('Основной тег должен быть только один')
        elif main_tags_count == 0:
            raise ValidationError('Укажите основной тег')

        return super().clean()  # вызываем базовый код переопределяемого метода


class RelationshipInline(admin.TabularInline):
    model = Relationship
    formset = RelationshipInlineFormset


@admin.register(Scope)
class ObjectAdmin(admin.ModelAdmin):
    pass


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]
