from django.db import models
from salao.models import Salao

class Profissional(models.Model):
    salao = models.ForeignKey(
        Salao,
        on_delete=models.CASCADE,
        related_name='profissionais', default=1
    )
    nome = models.CharField(max_length=255, default="Desconhecido")

    def __str__(self):
        return f'{self.nome} ({self.salao.nome})'
    
    