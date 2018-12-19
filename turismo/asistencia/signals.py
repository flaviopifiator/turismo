from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver

from . import models


@receiver(post_save, sender=models.Asistencia)
def incrementar_puntos(sender, **kwargs):
    instance = kwargs['instance']
    puntos = instance.capacitacion.puntos_incrementar
    for proveedor in instance.proveedor.all():
        proveedor.incrementar_puntos(puntos)

m2m_changed.connect(incrementar_puntos, sender=models.Asistencia.proveedor.through)