from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name='usuariourl'

#Aqui se determinan las urls a las que se puede acceder a la página
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('home/', views.Home.as_view(), name='home'),
    path('login/', views.Login.as_view(), name='login'),
    path('registro/', views.registroColaborador, name='registro_colab'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('colaboradores/', views.listaUsuarios, name='lista_colaboradores'),
]