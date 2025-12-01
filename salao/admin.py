from django.contrib import admin
from .models import Salao

@admin.register(Salao)
class SalaoAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "usuario")
