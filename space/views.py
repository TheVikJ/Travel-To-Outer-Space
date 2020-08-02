from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
import requests 


class HomeView(TemplateView) :
    template_name = "index.html"


class MenuView(TemplateView) :
    template_name = "Menu/Home.html"

class solsys(TemplateView) :
    template_name = "Menu/SolarSystemSimulation.html"


def issview(request) :
    url = "https://api.wheretheiss.at/v1/satellites/25544"
    response = requests.get(url).json()
    context = {
        "name" : response["name"],
        "id" : response["id"],
        "lat" : response["latitude"],
        "lon" : response["longitude"],
        "alt" : response["altitude"],
        "vel" : response["velocity"],
        "time" : response["timestamp"],
        "unit" : response["units"],
    }

    return render(request,"iss.html",context)
