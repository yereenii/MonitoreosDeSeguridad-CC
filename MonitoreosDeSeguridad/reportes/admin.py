from django.contrib import admin
from .models import ActosInsegurosMod,ActosSegurosMod,CondicionesInsegurasMod,IncidentesMenoresMod
# Register your models here.

admin.site.register(ActosInsegurosMod)
admin.site.register(ActosSegurosMod)
admin.site.register(CondicionesInsegurasMod)
admin.site.register(IncidentesMenoresMod)
