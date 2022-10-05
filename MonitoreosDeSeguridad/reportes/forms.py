from django import forms

from .models import *

class ActosInsegurosForm(forms.ModelForm):

    class Meta:
        model = ActosInsegurosMod
        exclude = ['fecha']

    def __init__(self, *args, **kwargs):
        super(ActosInsegurosForm, self).__init__(*args, **kwargs)
        self.fields['es_contratista'].required = False

        for name, field in self.fields.items():
            if name == 'nombre_reportado' or name == 'es_contratista' \
                or 'nombre_reportador' or name == 'observaciones':
                field.widget.attrs['class'] = 'form-control'
            else:
                field.widget.attrs['class'] = 'form-select'