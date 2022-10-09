from django.shortcuts import render

# Create your views here.

from django.views import View
from django.shortcuts import redirect
from django.urls import reverse
from django.shortcuts import HttpResponse
import os
import datetime
from weather_identify_web import settings
import base64
import json
from django.http import JsonResponse



class PublicTesting(View):
    
    def get(self, request):
        return redirect(to=reverse('weather:converter_images_to_base64'))
