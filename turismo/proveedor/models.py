from django.db import models

from util.models import AbstractDireccion


class Servicio(models.Model):
    nombre = models.CharField(max_length=250)

    def __str__(self):
        return self.nombre


class Beneficio(models.Model):
    nombre = models.CharField(max_length=250)
    puntos = models.PositiveIntegerField(default=1)
    servicio = models.ForeignKey(Servicio, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class ProveedorServicio(AbstractDireccion):
    class Meta:
        verbose_name_plural = 'Proveedores'

    nombre = models.CharField(max_length=250)
    cuit= models.CharField('CUIT', max_length=11, unique=True, null=True, blank=True)
    telefono = models.BigIntegerField('Número de Teléfono', null=True, blank=True)
    puntos = models.PositiveIntegerField(default=0, blank=True)
    historico_puntos = models.PositiveIntegerField(default=0, blank=True)
    servicio = models.ManyToManyField(Servicio)

    def __str__(self):
        return self.nombre

    def incrementar_puntos(self, puntos_incremento):
        self.puntos += puntos_incremento
        self.historico_puntos += puntos_incremento
        print('fefe')
        self.save()

    def decrementar_puntos(self, puntos_decremento):
        if self.puntos < puntos_decremento:
            return False
        self.puntos -= puntos_decremento
        self.save()
        return True
