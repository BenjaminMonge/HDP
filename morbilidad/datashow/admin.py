from django.contrib import admin

# Register your models here.
from .models import Ano, Mes, Enfermedad, Consulta
#making interface for editing on the admin site
admin.site.register(Ano)
admin.site.register(Mes)
admin.site.register(Enfermedad)
admin.site.register(Consulta)