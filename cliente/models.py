# cliente/models.py
from django.db import models
from usuario.models import CustomUser


class Cliente(models.Model):
    usuario = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='cliente',
    )
    # depois você coloca mais campos aqui

    def __str__(self):
        return self.usuario.username
