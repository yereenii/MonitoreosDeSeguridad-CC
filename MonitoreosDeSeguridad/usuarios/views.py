from django.contrib.auth.forms import AuthenticationForm
from django.utils.decorators import method_decorator
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.views.generic.edit import CreateView

from django.shortcuts import render, redirect
from .forms import UsuarioColaboradorForm

#decoradores
#from .decorators import unauthenticated_user
from django.contrib.auth.decorators import login_required
#para cuando necesite que este iniciado la sesión
#@method_decorator(login_required(), name='dispatch')

#Función para creación de un colaborador
#@unauthenticated_user
def registroColaborador(request):
    form = UsuarioColaboradorForm()
    if request.method == 'POST':
        form = UsuarioColaboradorForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name="colaborador")
            user.groups.add(group)
            messages.success(request, 'Cuenta creada exitosamente para: ' + username)
            #Regresa a home
            return redirect('reportesapp:home')

    context = {'form': form}
    return render(request, 'registro_colaborador.html', context)

#class ColaboradorCrear(CreateView):
 #   model = ColaboradorModel

#Si el usuario no está identificado, muestra Login
#@method_decorator(unauthenticated_user, name='dispatch')

class Login(LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('reportesapp:home')