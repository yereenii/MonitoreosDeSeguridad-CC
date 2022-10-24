from django import forms

from .models import *

class ActosInsegurosForm(forms.ModelForm):

    class Meta:
        model = ActosInsegurosMod
        exclude = ['reporte_generado_el','user']

    def __init__(self, *args, **kwargs):
        super(ActosInsegurosForm, self).__init__(*args, **kwargs)
        self.fields['es_contratista'].required = False

        for name, field in self.fields.items():
            if name == 'nombre_reportado' or name == 'es_contratista' \
                or 'nombre_reportador' or name == 'observaciones':
                field.widget.attrs['class'] = 'form-control'
            else:
                field.widget.attrs['class'] = 'form-select'

class ActosSegurosForm(forms.ModelForm):
    class Meta:
        model = ActosSegurosMod
        exclude = ['reporte_generado_el','user']

    def __init__(self, *args, **kwargs):
        super(ActosSegurosForm, self).__init__(*args, **kwargs)
        self.fields['es_contratista'].required = False

        for name, field in self.fields.items():
            if name == 'nombre_reportado' or name == 'nombre_jefinm' \
                    or 'es_contratista' or name == 'area' \
                    or 'nombre_reportador' or name == 'descripcion_as':
                field.widget.attrs['class'] = 'form-control'
            else:
                field.widget.attrs['class'] = 'form-select'


class IncidentesMenoresForm(forms.ModelForm):
    class Meta:
        model = IncidentesMenoresMod
        exclude = ['reporte_generado_el','user']

    def __init__(self, *args, **kwargs):
        super(IncidentesMenoresForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            if name == 'nombre_reportador' or name == 'departamento' \
                    or 'area' or name == 'maqoequipo' \
                    or 'descripcion' or name == 'semana' or name== 'mes':
                field.widget.attrs['class'] = 'form-control'
            else:
                field.widget.attrs['class'] = 'form-select'

class CondicionesInsegurasForm(forms.ModelForm):
    fecha_inicio = forms.DateField( widget=forms.SelectDateWidget())
    fecha_fin = forms.DateField(widget=forms.SelectDateWidget())
    class Meta:
        model = CondicionesInsegurasMod
        exclude = ['reporte_generado_el','user']

    def __init__(self, *args, **kwargs):
        super(CondicionesInsegurasForm, self).__init__(*args, **kwargs)


        for name, field in self.fields.items():
            if name == 'descr_condicion' or name == 'departamento' \
                    or 'area' or name == 'nombre_reportador' \
                    or 'num_aviso' or name == 'time_corre' or name== 'grupoycond':
                field.widget.attrs['class'] = 'form-control'
            else:
                field.widget.attrs['class'] = 'form-select'