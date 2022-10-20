from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .forms import ActosInsegurosMod, ActosInsegurosForm, ActosSegurosMod, ActosSegurosForm, IncidentesMenoresMod, \
    IncidentesMenoresForm, CondicionesInsegurasMod, CondicionesInsegurasForm


# Create your views here.



class ActosInseguros(CreateView):

    model = ActosInsegurosMod
    form_class = ActosInsegurosForm
    success_url = reverse_lazy('reportesapp:reporteexitoso')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        self.success_url = reverse_lazy('reportesapp:reporteexitoso', kwargs={"id": self.object.id})
        return super().form_valid(form)

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        return form_class(**self.get_form_kwargs())

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()

        if hasattr(self, 'object'):
            kwargs.update({'instance': self.object})
        return kwargs

class ActosSeguros(CreateView):
    model = ActosSegurosMod
    form_class = ActosSegurosForm
    success_url = reverse_lazy('reportesapp:reporteexitoso')
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        self.success_url = reverse_lazy('reportesapp:reporteexitoso', kwargs={"id": self.object.id})
        return super().form_valid(form)

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        return form_class(**self.get_form_kwargs())

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()

        if hasattr(self, 'object'):
            kwargs.update({'instance': self.object})
        return kwargs

class IncidentesMenores(CreateView):
    model = IncidentesMenoresMod
    form_class = IncidentesMenoresForm
    template_name = 'reportes/incidentesmenores_form.html'
    success_url = reverse_lazy('usuariourl:home')


class CondicionesInseguras(CreateView):
    model = CondicionesInsegurasMod
    form_class = CondicionesInsegurasForm
    template_name = 'reportes/condicionesinseguras_form.html'
    success_url = reverse_lazy('usuariourl:home')


class ReporteExitoso(TemplateView):
    model = User
    template_name = 'reporte_exitoso.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        self.extra_context = {
            'id': context['id']
        }
        print(self.extra_context)
        return self.render_to_response(context)



