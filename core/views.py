from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse_lazy
# Create your views here.

class HomeView(TemplateView):
    template_name = 'index.html'
