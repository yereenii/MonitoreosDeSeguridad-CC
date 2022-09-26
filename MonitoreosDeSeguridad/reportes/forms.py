from django import forms

from .models import *

class ActosInsegurosForm(forms.ModelForm):

    class Meta:
        model = ActosInsegurosMod
        exclude = ['fecha']

    def __init__(self, *args, **kwargs):
        super(ActosInsegurosForm, self).__init__(*args, **kwargs)
        self.fields['es_contratista'].required = False