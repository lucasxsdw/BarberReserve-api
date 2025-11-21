from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

#cria um serializer em ModelSerializer que mapeia campos do model user 
class RegisterSerializer(serializers.ModelSerializer):
   full_name = serializers.CharField(required=True)

   #class interna meta, como qual model usa e quais campos expor
   class Meta:
        model = User
        fields = ("id", "full_name", "email","password")
        extra_kwargs = {"password": {"write_only": True}} #ele pode ser enviado na requisicao, mas nao sera exibido na resposta

    
   #define como o objeto User sera criado quando o serializer.save() for chamado apos is_valid()
   def create(self, validated_data):
       full_name = validated_data.pop('full_name')
       email = validated_data['email']
       password = validated_data['password']

       username = email

       user = User(
           username = username,
           email = email,
           first_name = full_name
       )

       user.set_password(password)
       user.save()
       
       return user