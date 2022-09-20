import os

from django.shortcuts import render

# Create your views here.

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import HttpResponse
from weather_identify_web import settings
import datetime
import base64
from django.http import JsonResponse
import requests
import json


@csrf_exempt
def images_to_base64(request):
    if request.method == 'POST':
        data_json_return = {
            'base64': None
        }
        image = request.FILES.get('image')
        image_ext = os.path.splitext(image.name)[1]
        image_name = f'{datetime.datetime.now().strftime("%Y%m%d%H%M%S")}{image_ext}'
        images_folder = rf'{str(settings.BASE_DIR)}/uploads/images'
        if not os.path.exists(images_folder):
            os.makedirs(images_folder)
        image_path = rf'{images_folder}/{image_name}'
        print(images_folder)
        print(image_path)
        with open(file=image_path, mode='wb') as image_file:
            for image_data in image.chunks():
                image_file.write(image_data)
            image_file.close()
        with open(file=image_path, mode='rb') as image_file:
            converter_to_base64 = base64.b64encode(image_file.read()).decode('utf8')
            data_json_return.update(base64=converter_to_base64)
            image_file.close()
        data_json_return = json.dumps(data_json_return)
        response = requests.post('http://127.0.0.1:52001/weather/converter/', data=data_json_return)
        return JsonResponse(data=response, json_dumps_params={'ensure_ascii': False})
    return HttpResponse('请求方法错误') 

