from django.db import models

class Servico(models.Model):
    nome = models.CharField()
    descricao = models.CharField(null=True, blank=True)
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    duracao_minutos = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.nome}'