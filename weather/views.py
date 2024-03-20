from django.shortcuts import render,redirect
import json
import urllib.request
from .models import Weather
from django.contrib import messages


def index(request):
    if request.method == 'POST':
        data={}
        city = request.POST['city']
        apikey = '804dae8aa706f979c711e623008f52b2'
        url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(city, apikey)
        try:
           response = urllib.request.urlopen(url).read()
           json_data = json.loads(response)
           data = {
            "temp":"Temperature: "+str(round(int(json_data['main']['temp']-273.15))) + " C",
            "humidity":"Humidity: "+str(json_data['main']['humidity']),
            "pressure":"Pressure: "+str(json_data['main']['pressure'])
           }
           temp=str(round(int(json_data['main']['temp']-273.15)))
           weather=Weather.objects.create(city=city,temperature=temp)
           weather.save()
        except:
            messages.info(request,"City Doesn't exist")  
    else:
        data={}
    return render(request, "index.html", data)
