from django.shortcuts import render
import requests

# Create your views here.

def home(request):

     city=request.GET.get("city")
     url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=a1e5a9bc91ab12495ba3de08e746f958"
     data=requests.get(url).json()
     icon=data["weather"][0]["icon"]
     payload={
          "city":data["name"],
          "weather":data["weather"][0]["main"],
          "icon":data["weather"][0]["icon"],
          "temperature":data["main"]["temp"]-273,
          "ctemperature":data["main"]["temp"],
          "pressure":data["main"]["pressure"],
          "humidity":data["main"]["humidity"],
          "description":data["weather"][0]["description"],
          "u":f" http:openwhethermap.org/img/wn/{icon}.png",
          "url":f"https://images.pexels.com/photos/1107717/pexels-photo-1107717.jpeg?cs=srgb&dl=pexels-fotios-photos-1107717.jpg&fm=jpg"
     }
     context={"data":payload}
     print(context)



     return render(request,'home.html',context)