from django.shortcuts import render
import requests
import datetime

# Create your views here.

def home(request):
    if 'city' in request.post:
        city = request.post['city']
    else:
        city = 'lahore'
      
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid= d61f5869052c466a4eb0d05722190347'
    PARAMS = {'units': 'metric'}
   
    return render(request,'weatherapp/index.html')