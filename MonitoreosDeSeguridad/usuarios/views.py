from django.contrib.auth.forms import AuthenticationForm
from django.utils.decorators import method_decorator
#from .decorators import unauthenticated_user
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
import decorators
import pandas as pd

#@method_decorator(unauthenticated_user, name='dispatch')
class Login(LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('reportesapp:home')