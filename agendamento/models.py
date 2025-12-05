from django.db import models
from profissional.models import Profissional
from servico.models import Servico
from django.contrib.auth import get_user_model

Usuario = get_user_model()

class Agendamento(models.Model):
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data_agendada = models.DateField()
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()
    
    class Meta:
        unique_together = ('profissional', 'data_agendada', 'hora_inicio', 'hora_fim')


    
