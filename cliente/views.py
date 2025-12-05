from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework import generics

from usuario.models import CustomUser
from .models import Cliente
from .serializers import ClienteSerializer


class DefinirComoClienteView(APIView):
    """
    POST /api/cliente/definir/
    - Marca o usuário logado como 'cliente'
    - Cria (ou retorna) o registro Cliente correspondente
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        user: CustomUser = request.user

        # atualiza o tipo_perfil
        user.tipo_perfil = 'cliente'
        user.save()

        # garante que exista um Cliente pra esse usuário
        cliente, created = Cliente.objects.get_or_create(usuario=user)

        serializer = ClienteSerializer(cliente)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MeuClienteView(generics.RetrieveUpdateAPIView):
    """
    GET/PUT /api/cliente/meu/
    - Retorna/atualiza os dados de cliente do usuário logado
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ClienteSerializer

    def get_object(self):
        cliente, _ = Cliente.objects.get_or_create(usuario=self.request.user)
        return cliente
