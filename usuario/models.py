from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    telefone = models.CharField("Telefone", max_length=20, blank=True, null=True)

    def __str__(self):
        return self.first_name or self.username
