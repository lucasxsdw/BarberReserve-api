from django.db import models
from profissional.models import Profissional
from salao.models import Salao

class Servico(models.Model):
    nome = models.CharField()
    descricao = models.CharField(null=True, blank=True)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    duracao_minutos = models.PositiveSmallIntegerField()
    salao = models.ForeignKey(Salao, on_delete=models.CASCADE)
    profissionais = models.ManyToManyField(Profissional, related_name="servicos", blank=True)

    def __str__(self):
        return f'{self.nome}'