from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Agendamento

class AgendamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agendamento
        fields = [
            "id", "cliente", "profissional", "servico",
            "data_agendada", "hora_inicio", "hora_fim"
        ]
        read_only_fields = ("id", "data_criacao",)

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
