from django.db import models
from django.utils import timezone

from proveedor.models import ProveedorServicio
from capacitacion.models import Capacitacion


class Asistencia(models.Model):
    fecha = models.DateTimeField(default=timezone.now)
    descripcion = models.TextField(null=True, blank=True)
    proveedor = models.ManyToManyField(ProveedorServicio)
    capacitacion = models.ForeignKey(Capacitacion, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.fecha)