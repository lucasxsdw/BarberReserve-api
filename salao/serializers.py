from rest_framework import serializers
from .models import Salao

class SalaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salao
        fields = ['id', 'nome']

    def create(self, validated_data):
        user = self.context['request'].user
        salao, _ = Salao.objects.get_or_create(usuario=user)
        salao.nome = validated_data['nome']
        salao.save()
        return salao
