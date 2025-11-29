from rest_framework import serializers
from .models import Profissional

class ProfissionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profissional
        fields = ["id", "nome_completo", "telefone"]
