from django.db import models

class Profissional(models.Model):
    nome_completo = models.CharField(max_length=150)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.nome_completo}'