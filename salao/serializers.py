from rest_framework import serializers
from .models import Salao

class SalaoSerializer(serializers.ModelSerializer):
    usuario = serializers.IntegerField(source='usuario.id', read_only=True)

    class Meta:
        model = Salao
        fields = ['id', 'nome', 'usuario']

    def create(self, validated_data):
        user = self.context['request'].user
        salao, created = Salao.objects.get_or_create(usuario=user)

        salao.nome = validated_data['nome']
        salao.save()
        return salao

    def update(self, instance, validated_data):
        instance.nome = validated_data.get('nome', instance.nome)
        instance.save()
        return instance



#Retorna o usuário
#Cria ou atualiza corretamente
#Serve para o Flutter listar, criar e editar