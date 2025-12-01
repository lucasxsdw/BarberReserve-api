from rest_framework import generics, permissions
from .models import Salao
from .serializers import SalaoSerializer


class SalaoListCreateView(generics.ListCreateAPIView):
    """
    GET  /api/salao/  -> lista salões do usuário logado
    POST /api/salao/  -> cria/atualiza salão do usuário logado
    """
    serializer_class = SalaoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # só os salões do usuário logado
        return Salao.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        # garante que o salão fica vinculado ao usuário logado
        serializer.save(usuario=self.request.user)
