from django.db import models
from proveedor.models import ProveedorServicio
from capacitacion.models import Capacitacion


class FeedBack(models.Model):
    TIPO = (
        ('CL', 'Cliente'),
        ('PR', 'Proveedor'),
    )
    tipo = models.CharField(choices=TIPO, max_length=2, null=True, blank=True)
    mensaje = models.TextField()
    valoracion = models.PositiveIntegerField(null=True, blank=True)
    proveedor = models.ForeignKey(ProveedorServicio, null=True, blank=True, on_delete=models.CASCADE)
    capacitacion = models.ForeignKey(Capacitacion, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.mensaje
