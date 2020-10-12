from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

# Index view
class HomePageView(TemplateView):
    template_name = 'index.html'


# About view
class AboutPageView(TemplateView):
    template_name = 'about.html'