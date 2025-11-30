from django.db import models
from usuario.models import CustomUser

class Cliente(models.Model):
    usuario = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
