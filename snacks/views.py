from django.shortcuts import render
from django.views.generic import TemplateView



class Homepageview(TemplateView):
    template_name = 'home.html'


class Aboutpageview(TemplateView):
    template_name = 'about.html'