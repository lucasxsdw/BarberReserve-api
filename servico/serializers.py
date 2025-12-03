from rest_framework import serializers
from .models import Servico
from profissional.models import Profissional


class ServicoSerializer(serializers.ModelSerializer):
    # entrada: lista de IDs
    profissionais = serializers.ListField(
        child=serializers.IntegerField(),
        write_only=True
    )

    # saída: nomes bonitos dos profissionais
    profissionais_detalhes = serializers.StringRelatedField(
        many=True,
        read_only=True,
        source="profissionais"
    )

    class Meta:
        model = Servico
        fields = [
            "id",
            "nome",
            "descricao",
            "preco",
            "duracao_minutos",
            "profissionais",          # ids que vêm do Flutter/Thunder
            "profissionais_detalhes"  # nomes que voltam na resposta
        ]

    def create(self, validated_data):
        ids_profissionais = validated_data.pop("profissionais", [])

        profissionais_qs = Profissional.objects.filter(id__in=ids_profissionais)

        if len(profissionais_qs) != len(set(ids_profissionais)):
            raise serializers.ValidationError(
                {"profissionais": "Um ou mais profissionais não existem."}
            )

        servico = Servico.objects.create(**validated_data)
        servico.profissionais.set(profissionais_qs)
        return servico

    def update(self, instance, validated_data):
        ids_profissionais = validated_data.pop("profissionais", None)

        servico = super().update(instance, validated_data)

        if ids_profissionais is not None:
            profissionais_qs = Profissional.objects.filter(id__in=ids_profissionais)

            if len(profissionais_qs) != len(set(ids_profissionais)):
                raise serializers.ValidationError(
                    {"profissionais": "Um ou mais profissionais não existem."}
                )

            servico.profissionais.set(profissionais_qs)

        return servico
