from rest_framework import serializers
from .models import Cliente
from usuario.models import CustomUser


class UserSimplesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("id", "username", "email", "tipo_perfil")


class ClienteSerializer(serializers.ModelSerializer):
    usuario = UserSimplesSerializer(read_only=True)

    class Meta:
        model = Cliente
        fields = ("id", "usuario")
        # depois você adiciona outros campos aqui se criar no model
