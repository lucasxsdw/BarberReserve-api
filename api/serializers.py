from rest_framework import serializers
from usuario.models import CustomUser  # 👈 usa o seu modelo novo

class RegisterSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(required=True)
    telefone = serializers.CharField(required=True)

    class Meta:
        model = CustomUser
        fields = ("id", "full_name", "email", "password", "telefone")
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
