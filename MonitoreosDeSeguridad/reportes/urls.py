from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .views import *

app_name='reportesapp'

#Aqui se determinan las urls a las que se puede acceder a la página
urlpatterns = [
    path('actos-inseguros/', views.ActosInseguros.as_view(), name='actosinseguros'),
    path('actos-seguros/', views.ActosSeguros.as_view(), name='actosseguros'),
    path('incidentes-menores/', views.IncidentesMenores.as_view(), name='incidentesmenores'),
    path('condiciones-inseguras/', views.CondicionesInseguras.as_view(), name='condicionesinseguras'),

    path('reporte-exitoso/<int:id>', views.ReporteExitoso.as_view(), name='reporteexitoso'),

    path('reporte_actins/', GenExcel_ActosIns.as_view(), name="excel_ai"),
    path('reporte_actseg/', GenExcel_ActosSeg.as_view(), name="excel_as"),
    path('reporte_condins/', GenExcel_CondInseg.as_view(), name="excel_ci"),
    path('reporte_incmen/', GenExcel_IncidMenores.as_view(), name="excel_im"),
]