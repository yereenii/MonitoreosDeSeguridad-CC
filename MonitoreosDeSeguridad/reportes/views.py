from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView
from .forms import ActosInsegurosMod, ActosInsegurosForm, ActosSegurosMod, ActosSegurosForm, IncidentesMenoresMod, \
    IncidentesMenoresForm, CondicionesInsegurasMod, CondicionesInsegurasForm

from sqlalchemy import create_engine
import pandas as pd
import mysql.connector as connection
from django.conf import settings
from io import BytesIO, StringIO
from django.http.response import HttpResponse

from datetime import datetime

import xlsxwriter

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
        #bloque = self.object.get_bloqueVPO_display()
        #print(bloque)
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


class IterandoInseguros(ListView):
    model = ActosInsegurosMod

    template_name = "iterandoInseguro.html"

    # def get(self,*args,**kwargs):
    #     objeto = self.object.get_bloqueVPO_display()
    #     return print(objeto)
    #     # bloque = self.object.get_bloqueVPO_display()
    #     # print(bloque)


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
        obtener_registros = ActosInsegurosMod.objects.all()

        bloque = list()
        clasificacion = list()
        nreportado = list()
        descripcion = list()
        dep = list()
        contra = list()
        area = list()
        usuario = list()
        nreportador = list()
        observaciones = list()
        grupoc = list()
        precursor = list()
        fech = list()

        for registro in obtener_registros:
            bloque.append(registro.get_bloqueVPO_display())
            clasificacion.append(registro.get_clasificacionAI_display())
            nreportado.append(registro.nombre_reportado)
            descripcion.append(registro.get_desc_sancion_display())
            dep.append(registro.get_departamento_display())
            contra.append(registro.es_contratista)
            area.append(registro.area)
            nreportador.append(registro.nombre_reportador)
            observaciones.append(registro.observaciones)
            grupoc.append(registro.get_grupos_display())
            precursor.append(registro.get_precursor_display())

            # Fecha
            objDate = str(registro.reporte_generado_el)
            fech.append(objDate)
            usuario.append((registro.user))

        archivo = BytesIO()
        df = pd.DataFrame(
            {'BLOQUE VPO': bloque, 'CLASIFICACION ACTO INSEGURO': clasificacion, 'NOMBRE PERSONA REPORTADA': nreportado,
             'DESCRIPCIÓN DE LA SANCIÓN': descripcion,
             'DEPARTAMENTO O COMPAÑÍA AL QUE SE LE DETECTA EL ACTO INSEGURO': dep,
             'EN CASO DE COMPAÑÍA CONTRATISTA ESPECIFICAR DE CUAL SE TRATA': contra, 'AREA': area,
             'NOMBRE DE QUIEN DETECTA / FUNCION ': nreportador, 'OBSERVACIONES GENERALES': observaciones,
             'GRUPOS DE COMPORTAMIENTO': grupoc, 'ESTA ACTO PUEDE SER UN PRECURSO SIF ': precursor, 'FECHA': fech,
             'Usuario Que Registró el Reporte': usuario

             })

        response = HttpResponse(content_type='application/vnd.ms-excel')
        execl_name = '01_ActosInseguros'
        response['Content-Disposition'] = 'attachment;filename={0}.xlsx'.format(execl_name)
        df.to_excel(archivo, index=True)
        response.write(archivo.getvalue())
        return response

class GenExcel_ActosSeg(TemplateView):
    def get(self, request, *args, **kwargs):
        obtener_registros = ActosSegurosMod.objects.all()

        bloque = list()
        nreportado = list()
        felic = list()
        njefe = list()
        dep = list()
        escontr = list()
        are = list()
        nreportador = list()
        descrip = list()
        fech=list()
        usuario=list()


        for registro in obtener_registros:
            bloque.append(registro.get_bloqueVPO_display())
            nreportado.append(registro.nombre_reportado)
            felic.append(registro.get_felicitacion_display())
            njefe.append(registro.nombre_jefinm)
            dep.append(registro.get_departamento_display())
            escontr.append(registro.es_contratista)
            are.append(registro.area)
            nreportador.append(registro.nombre_reportador)
            descrip.append(registro.descripcion_as)
            # Fecha
            objDate = str(registro.reporte_generado_el)
            fech.append(objDate)
            usuario.append((registro.user))

        archivo = BytesIO()
        df = pd.DataFrame(
            {'BLOQUE VPO': bloque,'NOMBRE PERSONA OBSERVADA':nreportado,
             'FELICITO Y/O RECONOCIO AL PERSONALFELICITO Y/O RECONOCIO AL PERSONAL': felic,
             'NOMBRE JEFE INMEDIATO / FUNCION ':njefe, 'DEPARTAMENTO O COMPAÑÍA CONTRATISTA':dep,
             'NOMBRE DE LA COMPAÑÍA CONTRATISTA':escontr, 'AREA': are, 'NOMBRE DE QUIEN DETECTA / FUNCION': nreportador,
             'DESCRIPCIÓN DEL ACTO SEGURO':descrip,'FECHA':fech,'Usuario Que Registró el Reporte': usuario
             })

        response = HttpResponse(content_type='application/vnd.ms-excel')
        execl_name = '02_ActosSeguros'
        response['Content-Disposition'] = 'attachment;filename={0}.xlsx'.format(execl_name)
        df.to_excel(archivo, index=True)
        response.write(archivo.getvalue())
        return response

class GenExcel_CondInseg(TemplateView):
    def get(self, request, *args, **kwargs):
        obtener_registros = CondicionesInsegurasMod.objects.all()

        cond = list()
        fechinicio = list()
        fechfin = list()
        estat = list()
        dep = list()
        area = list()
        nreportador = list()
        clasif = list()
        alc = list()
        numaviso = list()
        timecorrec = list()
        prec = list()
        grupycon = list()
        usuario = list()

        for registro in obtener_registros:
            cond.append(registro.descr_condicion)
            # Fecha Inicio
            inicioobjDate = str(registro.fecha_inicio)
            fechinicio.append(inicioobjDate)
            # Fecha Fin
            finobjDate = str(registro.fecha_fin)
            fechfin.append(finobjDate)
            estat.append(registro.get_estatus_display())
            dep.append(registro.departamento)
            area.append(registro.area)
            nreportador.append(registro.nombre_reportador)
            clasif.append(registro.get_clas_condic_display())
            alc.append(registro.get_alcance_display())
            numaviso.append(registro.num_aviso)
            timecorrec.append(registro.time_corre)
            prec.append(registro.get_precursor_display())
            grupycon.append(registro.grupoycond)

            usuario.append((registro.user))

        archivo = BytesIO()
        df = pd.DataFrame(
            {'Condición Insegura Detectada': cond, 'Fecha Incio': fechinicio, 'Fecha Fin':fechfin,
             'Estatus':estat, 'Departamento o Comañía':dep, 'Área':area,'Nombre de Quién la Detectó': nreportador,
             'Clasificación de la Condición':clasif, 'Alcance':alc,'No. de Aviso':numaviso, 'Tiempo de Corrección':timecorrec,
             '¿Es Precursor SIF?':prec,'Grupo de Condiciones':grupycon, 'Usuario Que Registró el Reporte': usuario
             })

        response = HttpResponse(content_type='application/vnd.ms-excel')
        execl_name = '03_CondicionesInseguras'
        response['Content-Disposition'] = 'attachment;filename={0}.xlsx'.format(execl_name)
        df.to_excel(archivo, index=True)
        response.write(archivo.getvalue())
        return response

class GenExcel_IncidMenores(TemplateView):
    def get(self, request, *args, **kwargs):
        obtener_registros = IncidentesMenoresMod.objects.all()

        fech = list()
        turn = list()
        nreportador = list()
        usuario =list()
        tipoinc = list()
        caus= list()
        dep = list()
        are = list()
        maqequipo = list()
        poterc = list()
        puest = list()
        desc = list()
        sem = list()
        mes = list()

        for registro in obtener_registros:
            # Fecha
            objDate = str(registro.reporte_generado_el)
            fech.append(objDate)
            turn.append(registro.get_turno_display())
            nreportador.append(registro.nombre_reportador)
            tipoinc.append(registro.get_tipo_incidente_display())
            caus.append(registro.causa)
            dep.append(registro.departamento)
            are.append(registro.area)
            maqequipo.append(registro.maqoequipo)
            poterc.append(registro.get_propoterc_display())
            puest.append(registro.get_puesto_display())
            desc.append(registro.descripcion)
            sem.append(registro.semana)
            mes.append(registro.mes)
            usuario.append((registro.user))

        archivo = BytesIO()
        df = pd.DataFrame(
            {'Fecha': fech,'TURNO':turn,'NOMBRE DE LA PERSONA QUE REPORTA EL INCIDENTE':nreportador,
             'TIPO DE INCIDENTES REPORTADO':tipoinc,'CAUSA':caus,'DEPARTAMENTO':dep,'ÁREA':are,
             'MAQUINARIA O EQUIPO':maqequipo,'PROPIO O TERCIARIA':poterc,'PUESTO DE QUIEN REPORTA':puest,
             'DESCRIPCIÓN GENERAL DEL INCIDENTE':desc, 'SEMANA':sem,'MES':mes,
             'Usuario Que Registró el Reporte': usuario
             })

        response = HttpResponse(content_type='application/vnd.ms-excel')
        execl_name = '04_IncidentesMenores'
        response['Content-Disposition'] = 'attachment;filename={0}.xlsx'.format(execl_name)
        df.to_excel(archivo, index=True)
        response.write(archivo.getvalue())
        return response

