from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name='usuariourl'

#Aqui se determinan las urls a las que se puede acceder a la página
urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
]