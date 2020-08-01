from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView


class HomeView(TemplateView) :
    template_name = "base.html"