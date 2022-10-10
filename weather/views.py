import os

from django.shortcuts import render

# Create your views here.

from weather_identify_web import settings
import datetime
import base64
from django.http import JsonResponse
import requests
import json
from django.views import View
from django.shortcuts import redirect
from django.urls import reverse


class ImagesToBase64(View):
    
    def get(self, request):
        return render(self.request, template_name='weather/index.html')
    
    
    def post(self, request):
        # 定义返回数据
        data_dict_return: dict = {
            'base64': None
        }
        # 获取form表单的文件数据
        image = self.request.FILES.get('image')
        # 获取文件的扩展名
        image_ext = os.path.splitext(image.name)[1]
        # 定义文件名
        image_name = f'{datetime.datetime.now().strftime("%Y%m%d%H%M%S")}{image_ext}'
        # 定义文件上传文件夹
        images_folder = rf'{str(settings.BASE_DIR)}/uploads/images'
        # 判断文件上传文件夹是否存在
        if not os.path.exists(images_folder):
            # 不存在 -> 创建文件夹
            os.makedirs(images_folder)
        # 上传文件路径
        image_path = rf'{images_folder}/{image_name}'
        # 写入文件
        with open(file=image_path, mode='wb') as image_file:
            for image_data in image.chunks():
                image_file.write(image_data)
            image_file.close()
        # 文件转为base64
        with open(file=image_path, mode='rb') as image_file:
            converter_to_base64 = base64.b64encode(image_file.read()).decode('utf8')
            data_dict_return.update(base64=converter_to_base64)
            image_file.close()
        # 转换json格式
        data_json_return = json.dumps(data_dict_return)
        # response = requests.post('http://127.0.0.1:52001/weather/converter/', data=data_json_return)
        # 返回json类型
        # return JsonResponse(data=data_dict_return, json_dumps_params={'ensure_ascii': False})
        return render(self.request, template_name='weather/identify.html', context=locals())
        

