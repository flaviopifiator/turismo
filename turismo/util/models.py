from django.db import models
from django.contrib.gis.db import models as models_gis


class Departamento(models.Model):

    class Meta:
        ordering = ('nombre',)
        verbose_name_plural = ('Departamentos')

    nombre = models.CharField(max_length=60)

    def __str__(self):
        return self.nombre


class Localidad(models.Model):

    class Meta:
        ordering = ('nombre',)
        verbose_name_plural = ('Localidades')

    nombre = models.CharField(max_length=100)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    cod_postal = models.IntegerField(null=True, blank=True, default=None)

    def __str__(self):
        return self.nombre


class AbstractDireccion(models.Model):

    class Meta:
        abstract = True

    nombre_dir = models.CharField(
        'Nombre de Calle',
        max_length=100,
        null=True, blank=True
    )
    numero_dir = models.PositiveIntegerField(
        'Número de Calle',
        null=True, blank=True
    )
    localidad = models.ForeignKey(Localidad, null=True, blank=True, on_delete=models.CASCADE)
    ubicacion = models_gis.PointField(null=True, blank=True)
