from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .forms import ActosInsegurosMod, ActosInsegurosForm, ActosSegurosMod, ActosSegurosForm, IncidentesMenoresMod, \
    IncidentesMenoresForm, CondicionesInsegurasMod, CondicionesInsegurasForm

from sqlalchemy import create_engine
import pandas as pd
import mysql.connector as connection
from django.conf import settings
from io import BytesIO
from django.http.response import HttpResponse

##Conexión a la Base de datos a través de SQLAlchemy y uso posterior a Pandas.
engine = create_engine("mysql://user:passwd@host/db",
                       connect_args= dict(host=settings.DATABASES['default']['HOST'], db = settings.DATABASES['default']['NAME'],
                                          user = settings.DATABASES['default']['USER'],passwd = settings.DATABASES['default']['PASSWORD']))

connection = engine.connect()

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


class CondicionesInseguras(CreateView):
    model = CondicionesInsegurasMod
    form_class = CondicionesInsegurasForm
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


class GenExcel_ActosIns(TemplateView):
    def get(self, request, *args, **kwargs):
        archivo = BytesIO()
        result_dataFrame = pd.read_sql("Select * from reportes_actosinsegurosmod;", con=connection)
        result_dataFrame.head()
        response = HttpResponse(content_type='application/vnd.ms-excel')
        execl_name = '01_ActosInseguros'
        response['Content-Disposition'] = 'attachment;filename={0}.xlsx'.format(execl_name)
        result_dataFrame.to_excel(archivo, index=False)
        response.write(archivo.getvalue())
        return response

class GenExcel_ActosSeg(TemplateView):
    def get(self, request, *args, **kwargs):
        archivo = BytesIO()
        result_dataFrame = pd.read_sql("Select * from reportes_actossegurosmod;", con=connection)
        result_dataFrame.head()
        response = HttpResponse(content_type='application/vnd.ms-excel')
        execl_name = '02_ActosSeguros'
        response['Content-Disposition'] = 'attachment;filename={0}.xlsx'.format(execl_name)
        result_dataFrame.to_excel(archivo, index=False)
        response.write(archivo.getvalue())
        return response

class GenExcel_CondInseg(TemplateView):
    def get(self, request, *args, **kwargs):
        archivo = BytesIO()
        result_dataFrame = pd.read_sql("Select * from reportes_condicionesinsegurasmod;", con=connection)
        result_dataFrame.head()
        response = HttpResponse(content_type='application/vnd.ms-excel')
        execl_name = '03_CondicionesInseguras'
        response['Content-Disposition'] = 'attachment;filename={0}.xlsx'.format(execl_name)
        result_dataFrame.to_excel(archivo, index=False)
        response.write(archivo.getvalue())
        return response

class GenExcel_IncidMenores(TemplateView):
    def get(self, request, *args, **kwargs):
        archivo = BytesIO()
        result_dataFrame = pd.read_sql("Select * from reportes_incidentesmenoresmod;", con=connection)
        result_dataFrame.head()
        response = HttpResponse(content_type='application/vnd.ms-excel')
        execl_name = '04_IncidentesMenores'
        response['Content-Disposition'] = 'attachment;filename={0}.xlsx'.format(execl_name)
        result_dataFrame.to_excel(archivo, index=False)
        response.write(archivo.getvalue())
        return response
