from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    telefone = models.CharField("Telefone", max_length=20, blank=True, null=True)
    tipo_perfil = models.CharField(max_length=15)

    def __str__(self):
        return self.first_name or self.username
