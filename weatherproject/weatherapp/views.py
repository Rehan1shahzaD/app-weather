from django.shortcuts import render
import datetime
import requests


API_KEY = 'd61f5869052c466a4eb0d05722190347'
DEFAULT_IMAGE = 'https://images.pexels.com/photos/3008509/pexels-photo-3008509.jpeg?auto=compress&cs=tinysrgb&w=1600'


def home(request):
    city = 'lahore'
    image_url = DEFAULT_IMAGE
    exception_occurred = False

    if request.method == 'POST':
        city = request.POST.get('city', '').strip() or 'lahore'

    try:
        url = 'https://api.openweathermap.org/data/2.5/weather'
        params = {'q': city, 'appid': API_KEY, 'units': 'metric'}
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        if 'weather' not in data or 'main' not in data:
            raise ValueError('Weather data not found')

        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']
        city = data.get('name', city)
        image_url = f'https://source.unsplash.com/1600x900/?{city},weather'
        day = datetime.date.today()

        return render(
            request,
            'index.html',
            {
                'city': city,
                'description': description,
                'icon': icon,
                'temp': temp,
                'day': day,
                'image_url': image_url,
                'exception_occurred': False,
            },
        )
    except Exception:
        exception_occurred = True
        return render(
            request,
            'index.html',
            {
                'city': city,
                'description': 'Weather unavailable',
                'icon': '',
                'temp': '--',
                'day': datetime.date.today(),
                'image_url': image_url,
                'exception_occurred': exception_occurred,
            },
        )