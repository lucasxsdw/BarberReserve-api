from django.db import models
from usuario.models import CustomUser

class Salao(models.Model):
    usuario = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
