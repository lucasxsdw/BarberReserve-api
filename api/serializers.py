from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

#cria um serializer em ModelSerializer que mapeia campos do model user 
class RegisterSerializer(serializers.ModelSerializer):
   #class interna meta, como qual model usa e quais campos expor
   class Meta:
        model = User
        fields = ("id", "username", "email", "password")
        extra_kwargs = {"password": {"write_only": True}} #ele pode ser enviado na requisicao, mas nao sera exibido na resposta

    
   #define como o objeto User sera criado quando o serializer.save() for chamado apos is_valid()
   def create(self, validated_data):
       #substitui a senha em texto puro por swu hash usando make_password
       validated_data["password"] = make_password(validated_data["password"])
       return User.objects.create(**validated_data)
 
    