# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import Question,Choice

class ChoiceInline(admin.TabularInline):
    model=Choice
    extra=1

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    fieldsets=[
        ('content',{'fields':['question_text']}),
        ('dateinfo',{'fields':['pub_date'],'classes':['collapse']}),
    ]
    inlines=[ChoiceInline]

admin.site.register(Question,QuestionAdmin)
# admin.site.register(Choice)

