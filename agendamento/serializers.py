# agendamento/serializers.py
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Agendamento
from profissional.models import Profissional
from servico.models import Servico

class AgendamentoSerializer(serializers.ModelSerializer):
    # Escrita: recebe só o ID
    profissional = serializers.PrimaryKeyRelatedField(
        queryset=Profissional.objects.all()
    )
    servico = serializers.PrimaryKeyRelatedField(
        queryset=Servico.objects.all()
    )

    class Meta:
        model = Agendamento
        fields = [
            "id", "cliente", "profissional", "servico",
            "data_agendada", "hora_inicio", "hora_fim"
        ]
        read_only_fields = ("id", "cliente")
        # ⚠️ TIRA o depth, vamos montar manualmente abaixo
        # depth = 1

    def create(self, validated_data):
        # cliente = usuário logado SEMPRE
        user = self.context['request'].user
        validated_data['cliente'] = user
        return super().create(validated_data)

    def to_representation(self, instance):
        """
        Leitura: devolve objetos completos de profissional e serviço,
        pra você ter nome, preço, etc, no Flutter.
        """
        data = super().to_representation(instance)

        data['profissional'] = {
            "id": instance.profissional.id,
            "nome": instance.profissional.nome,
            "salao": instance.profissional.salao_id,
        }

        data['servico'] = {
            "id": instance.servico.id,
            "nome": instance.servico.nome,
            "descricao": instance.servico.descricao,
            "preco": str(instance.servico.preco),
            "duracao_minutos": instance.servico.duracao_minutos,
            "salao": instance.servico.salao_id,
        }

        return data

    def validate(self, attrs):
        hora_inicio = attrs.get("hora_inicio")
        hora_fim = attrs.get("hora_fim")
        data_agendada = attrs.get("data_agendada")
        profissional = attrs.get("profissional")
        servico = attrs.get("servico")

        if hora_inicio and hora_fim and hora_inicio >= hora_fim:
            raise ValidationError({"hora_inicio": "hora_inicio deve ser anterior a hora_fim."})

        if not data_agendada:
            raise ValidationError({"data_agendada": "data_agendada é obrigatória."})

        if profissional and data_agendada and hora_inicio and hora_fim:
            conflitos = Agendamento.objects.filter(
                profissional=profissional,
                data_agendada=data_agendada,
            ).filter(
                hora_inicio__lt=hora_fim,
                hora_fim__gt=hora_inicio,
            )

            instance = getattr(self, "instance", None)
            if instance:
                conflitos = conflitos.exclude(pk=instance.pk)

            if conflitos.exists():
                raise ValidationError("Horário indisponível para esse profissional (conflito de agendamento).")

        return attrs
