from django.shortcuts import render

# Create your views here.

from django.views import View
from django.shortcuts import redirect
from django.urls import reverse



class PublicTesting(View):
    
    def get(self, request):
        return redirect(to=reverse('weather:converter_images_to_base64'))
