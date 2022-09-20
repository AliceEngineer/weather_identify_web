# coding: utf8
""" 
@File: urls.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/9/20 16:00
"""

from django.urls.conf import path, re_path
from weather import views

urlpatterns = [
    path(route='converter/', view=views.images_to_base64, name='converter_images_to_base64'),
]
