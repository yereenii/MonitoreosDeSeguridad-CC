from django.contrib.auth.forms import AuthenticationForm
from django.utils.decorators import method_decorator
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from django.shortcuts import render, redirect
from .forms import UsuarioColaboradorForm

#decoradores
#from .decorators import unauthenticated_user
from django.contrib.auth.decorators import login_required
#para cuando necesite que este iniciado la sesión
#@method_decorator(login_required(), name='dispatch')

class Home(TemplateView):
    template_name = 'usuarios/homebase.html'
    success_url = reverse_lazy('usuariourl:home')


#Función para creación de un colaborador
@login_required
def registroColaborador(request):
    form = UsuarioColaboradorForm()
    if request.method == 'POST':
        form = UsuarioColaboradorForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name="colaborador")
            user.groups.add(group)
            #messages.success(request, 'Cuenta creada exitosamente para: ' + username)
            return redirect('usuariourl:lista_colaboradores')

    context = {'form': form}
    return render(request, 'registro_colaborador2.html', context)

#class ColaboradorCrear(CreateView):
 #   model = ColaboradorModel

#Si el usuario no está identificado, muestra Login
#@method_decorator(unauthenticated_user, name='dispatch')

class Login(LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('usuariourl:home')


def listaUsuarios(request):
    usuarios = User.objects.all()
    return render(request, 'usuarios/detalle/admin_colaboradores.html', {'usuarios': usuarios})


############# Ver detalles de un usuario #########
class UsuarioDetalle(TemplateView):
    template_name = 'usuarios/detalle/usuario_detail.html'
    model = User
    extra_context = {'etiquetatipousuario': 'colaborator'}
###################################################