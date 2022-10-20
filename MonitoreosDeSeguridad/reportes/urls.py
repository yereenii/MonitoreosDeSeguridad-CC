from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name='reportesapp'

#Aqui se determinan las urls a las que se puede acceder a la página
urlpatterns = [
    path('actos-inseguros/', views.ActosInseguros.as_view(), name='actosinseguros'),
    path('actos-seguros/', views.ActosSeguros.as_view(), name='actosseguros'),
    path('incidentes-menores/', views.IncidentesMenores.as_view(), name='incidentesmenores'),
    path('condiciones-inseguras/', views.CondicionesInseguras.as_view(), name='condicionesinseguras'),

    path('reporte-exitoso/<int:id>', views.ReporteExitoso.as_view(), name='reporteexitoso'),
]