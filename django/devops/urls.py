#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
author: hcylus
license: GPL
site: https://github.com/hcylus
file: urls.py
time: 2017/8/2 上午11:32
copyright: © DevOps

"""

from django.conf.urls import url
from . import views

app_name='devops'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
