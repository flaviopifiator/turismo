from django.contrib import admin
from core.admin import admin_general
from . import models


@admin.register(models.Asistencia, site=admin_general)
class AsistenciaAdmin(admin.ModelAdmin):
    pass
