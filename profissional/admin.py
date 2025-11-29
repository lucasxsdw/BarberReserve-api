from django.contrib import admin
from .models import Profissional


@admin.register(Profissional)
class ProfissionalAdmin(admin.ModelAdmin):
    list_display = ("id", "nome_completo", "telefone")  # colunas da listagem
    search_fields = ("nome_completo", "telefone")       # busca no topo
