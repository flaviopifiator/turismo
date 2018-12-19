from django.db import models
from django.contrib.auth.models import AbstractUser

from proveedor.models import Proveedor


class User(AbstractUser):
    class Meta:
        db_table = 'auth_user'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ('username', 'last_name', 'first_name')

    TIPO = (
        ('ADM', 'Administrador'),
        ('PST', 'Proveedor de Servicio Turístico'),
    )
    tipo = models.CharField(choices=TIPO, max_length=3, null=True, blank=True)
    proveedor = models.OneToOneField(
        Proveedor,
        null=True, blank=True,
        related_name='user_proveedor',
        on_delete=models.PROTECT
    )

USERNAME_FIELD = 'username'