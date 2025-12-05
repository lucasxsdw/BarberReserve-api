from django.db import models
from usuario.models import CustomUser

class Salao(models.Model):
    usuario = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='salao',
    )
    nome = models.CharField(max_length=255, default="Desconhecido")

    def __str__(self):
        return self.nome
