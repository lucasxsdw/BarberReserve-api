from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    telefone = models.CharField("Telefone", max_length=20, blank=True, null=True)

    TIPO_PERFIL_CHOICES = (
        ('CLIENTE', 'Cliente'),
        ('SALAO', 'Salão'),
    )

    tipo_perfil = models.CharField(
        max_length=15,
        choices=TIPO_PERFIL_CHOICES,
        default='CLIENTE',  # ISSO AQUI é importante pra migração
    )

    def __str__(self):
        return self.first_name or self.username
