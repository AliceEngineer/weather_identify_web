# coding: utf8
""" 
@File: urls.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/10/9 20:44
"""

from django.urls import re_path
from public import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    re_path(r'', csrf_exempt(views.PublicTesting.as_view()), name='home')
]
