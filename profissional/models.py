from django.db import models
from salao.models import Salao

class Profissional(models.Model):
    salao = models.ForeignKey(
        Salao,
        on_delete=models.CASCADE,
        related_name='profissionais',
    )
    nome = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.nome} ({self.salao.nome})'
