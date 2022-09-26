from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .forms import ActosInsegurosMod, ActosInsegurosForm


# Create your views here.
class Home (TemplateView):
    template_name = 'home.html'
    success_url = reverse_lazy('reportesapp:home')

class ActosInseguros(CreateView):
    model = ActosInsegurosMod
    form_class = ActosInsegurosForm
    template_name = 'reportes/actosinseguros_form.html'
