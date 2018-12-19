from django.contrib import admin
from core.admin import admin_general
from . import models

from django import forms
from mapwidgets.widgets import GooglePointFieldWidget


class ProveedorForm(forms.ModelForm):
    class Meta:
        model = models.ProveedorServicio
        fields = ("ubicacion",)
        widgets = {
            'ubicacion': GooglePointFieldWidget,
        }


@admin.register(models.Servicio, site=admin_general)
class ServicioAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ProveedorServicio, site=admin_general)
class ProveedorAdmin(admin.ModelAdmin):
    form = ProveedorForm
    list_display = (
        'nombre', 'puntos', 'historico_puntos',
    )
    fieldsets = [
        ('Datos',
         {
             'classes': ('tab-general',),
             'fields': [('nombre', 'cuit',), 'telefono', 'servicio']
         }
         ),
        ('Ubicación',
         {
             'classes': ('tab-ubicacion',),
             'fields': [('nombre_dir', 'numero_dir',), 'localidad', 'ubicacion']
         }
         ),
    ]


@admin.register(models.Beneficio, site=admin_general)
class BeneficioAdmin(admin.ModelAdmin):
    pass

