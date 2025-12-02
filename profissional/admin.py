from django.contrib import admin
from .models import Profissional

@admin.register(Profissional)
class ProfissionalAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'salao')
    search_fields = ('nome', 'salao__nome')
    list_filter = ('salao',)
