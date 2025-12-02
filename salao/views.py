from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import Salao
from .serializers import SalaoSerializer


class SalaoListCreateView(generics.ListCreateAPIView):
    """
    GET  /api/salao/        -> lista salões do usuário logado
    POST /api/salao/        -> cria salão vinculado ao usuário logado
    """
    serializer_class = SalaoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Apenas salões pertencentes ao usuário logado
        return Salao.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        # Salva o salão relacionado ao usuário logado
        serializer.save(usuario=self.request.user)


class MeuSalaoView(generics.RetrieveAPIView):
    """
    GET /api/salao/meu-salao/  -> retorna o salão do usuário logado
    """
    serializer_class = SalaoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        try:
            return Salao.objects.get(usuario=self.request.user)
        except Salao.DoesNotExist:
            raise NotFound("Nenhum salão cadastrado.")
