from django.contrib import admin
from .models import Servico

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'salao_nome', 'preco', 'duracao_minutos')  

    def salao_nome(self, obj):
        return obj.salao.nome if obj.salao else "—"

    salao_nome.short_description = "Salão"
