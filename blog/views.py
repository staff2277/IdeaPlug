from django.shortcuts import render
from django.views.generic import CreateView, TemplateView


# Create your views here.
class HomeView(TemplateView):
    template_name = 'blog/home.html'





