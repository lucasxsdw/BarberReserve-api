from django.contrib import admin
from .models import Profissional

@admin.register(Profissional)
class ProfissionalAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'salao')
    search_fields = ('nome', 'salao__nome')
    list_filter = ('salao',)
    actions = ["delete_profissionais_selecionados"]

    def delete_profissionais_selecionados(self, request, queryset):
        total = queryset.count()
        queryset.delete()
        self.message_user(
            request,
            f"{total} profissionais foram excluídos com sucesso!"
        )

    delete_profissionais_selecionados.short_description = "Excluir profissionais selecionados"
