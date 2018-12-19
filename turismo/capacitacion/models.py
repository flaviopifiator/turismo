from django.db import models

from util.models import AbstractDireccion


class Capacitacion(AbstractDireccion):
    class Meta:
        verbose_name_plural = 'Capacitaciones'

    nombre = models.CharField(max_length=250)
    inicio = models.DateTimeField(null=True, blank=True)
    fin = models.DateTimeField(null=True, blank=True)
    horas = models.TimeField()
    puntos_incrementar = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.nombre