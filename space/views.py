from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView


class HomeView(TemplateView) :
    template_name = "index.html"


class MenuView(TemplateView) :
    template_name = "Menu/Home.html"

class solsys(TemplateView) :
    template_name = "Menu/SolarSystemSimulation.html"
