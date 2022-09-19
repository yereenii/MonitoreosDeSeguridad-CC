from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView


# Create your views here.
class Home (TemplateView):
    template_name = 'home.html'
    success_url = reverse_lazy('reportesapp:home')