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

urlpatterns = [
    url(r'^$', views.index, name='index')
]
