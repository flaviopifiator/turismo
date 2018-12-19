from django.contrib import admin
from core.admin import admin_general
from django.db.models import ManyToManyField
from django import forms
from . import models

from django.contrib.admin.widgets import FilteredSelectMultiple

from django import forms
from mapwidgets.widgets import GooglePointFieldWidget


class CapacitacionForm(forms.ModelForm):
    class Meta:
        model = models.Capacitacion
        fields = ("ubicacion",)
        widgets = {
            'ubicacion': GooglePointFieldWidget,
        }

@admin.register(models.Capacitacion, site=admin_general)
class CapacitacionAdmin(admin.ModelAdmin):
    form = CapacitacionForm
    fieldsets = [
        ('Datos',
         {
             'classes': ('tab-general',),
             'fields': ['nombre', 'horas', ('inicio', 'fin',), 'puntos_incrementar']
         }
         ),
        ('Ubicación',
         {
             'classes': ('tab-ubicacion',),
             'fields': [('nombre_dir', 'numero_dir',), 'localidad', 'ubicacion']
         }
         ),
    ]