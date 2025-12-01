from rest_framework import serializers
from .models import Servico
from profissional.models import Profissional

class ServicoSerializer(serializers.ModelSerializer):
    profissionais = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Profissional.objects.all()
    )

    class Meta:
        model = Servico
        fields = [
            "id", "nome", "descricao", "preco", "duracao_minutos",
            "profissionais"
        ]

    def create(self, validated_data):
        profissionais = validated_data.pop("profissionais", [])
        servico = Servico.objects.create(**validated_data)
        servico.profissionais.set(profissionais)
        return servico

    def update(self, instance, validated_data):
        profissionais = validated_data.pop("profissionais", None)
        servico = super().update(instance, validated_data)

        if profissionais is not None:
            servico.profissionais.set(profissionais)

        return servico