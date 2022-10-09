# coding: utf8
""" 
@File: urls.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/9/20 16:00
"""

from django.urls.conf import re_path
from weather import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    re_path(route=r'^converter/$', view=csrf_exempt(views.ImagesToBase64.as_view()), name='converter_images_to_base64'),
]
