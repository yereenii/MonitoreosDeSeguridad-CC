from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .forms import ActosInsegurosMod, ActosInsegurosForm, ActosSegurosMod, ActosSegurosForm, IncidentesMenoresMod, \
    IncidentesMenoresForm, CondicionesInsegurasMod, CondicionesInsegurasForm


# Create your views here.
class Home(TemplateView):
    template_name = 'home.html'
    success_url = reverse_lazy('reportesapp:home')


class ActosInseguros(CreateView):
    model = ActosInsegurosMod
    form_class = ActosInsegurosForm
    template_name = 'reportes/actosinseguros_form.html'
    success_url = reverse_lazy('reportesapp:home')


class ActosSeguros(CreateView):
    model = ActosSegurosMod
    form_class = ActosSegurosForm
    template_name = 'reportes/actosseguros_form.html'
    success_url = reverse_lazy('reportesapp:home')


class IncidentesMenores(CreateView):
    model = IncidentesMenoresMod
    form_class = IncidentesMenoresForm
    template_name = 'reportes/incidentesmenores_form.html'
    success_url = reverse_lazy('reportesapp:home')


class CondicionesInseguras(CreateView):
    model = CondicionesInsegurasMod
    form_class = CondicionesInsegurasForm
    template_name = 'reportes/condicionesinseguras_form.html'
    success_url = reverse_lazy('reportesapp:home')
