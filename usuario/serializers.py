from rest_framework import serializers
from .models import CustomUser

# 1. Usado no cadastro
class RegisterSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(required=True)
    telefone = serializers.CharField(required=True)

    class Meta:
        model = CustomUser
        fields = ("id", "full_name", "email", "password", "telefone", "tipo_perfil")
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        nome = validated_data.pop("full_name")
        telefone = validated_data.pop("telefone")
        email = validated_data["email"]
        senha = validated_data["password"]

        user = CustomUser(
            username=email,
            email=email,
            first_name=nome,
            telefone=telefone,
        )
        user.set_password(senha)
        user.save()
        return user


# 2. Usado para /api/me/, atualizar tipo_perfil, preencher telas
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'email', 'telefone', 'tipo_perfil']
        read_only_fields = ['id', 'email', 'tipo_perfil']
