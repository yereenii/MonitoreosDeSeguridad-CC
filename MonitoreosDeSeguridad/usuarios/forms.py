from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms


### Clase de Form que permite agregar un usuario como alumno sin importar
### si es recien egresado o egresado con antiguedad
class UsuarioColaboradorForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(UsuarioColaboradorForm, self).__init__(*args, **kwargs)
        self.fields['password1'].label = 'Introduce la contraseña'
        self.fields['password2'].label = 'Introduce la contraseña nuevamente'
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''
        self.fields['username'].help_text = ''

        #self.fields['first_name'] = (self.fields['first_name']).uppercase()
        #self.fields['first_name'].widget= 'text-transform:uppercase;'
        #self.fields['first_name'].input_type =

        self.fields['first_name'].required = True
        self.fields['last_name'].required = True

    # tipo = forms.CharField(widget=forms.HiddenInput())
        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


    class Meta:

        model = User
        fields = ['username', 'first_name', 'last_name', 'email','password1']

