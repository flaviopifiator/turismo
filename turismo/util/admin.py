from django.contrib import admin
from core.admin import admin_general
from . import models


@admin.register(models.Departamento, site=admin_general)
class DepartamentoAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Localidad, site=admin_general)
class LocalidadAdmin(admin.ModelAdmin):
    pass