from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied

from .models import Profissional
from .serializers import ProfissionalSerializer
from salao.models import Salao


class ProfissionalListCreateView(generics.ListCreateAPIView):
    """
    GET  /api/profissional/       -> lista profissionais do salão do usuário logado
    POST /api/profissional/       -> cria profissional ligado ao salão do usuário logado
    """
    serializer_class = ProfissionalSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # só profissionais do salão do usuário logado
        return Profissional.objects.filter(salao__usuario=self.request.user)

    def _get_salao_do_usuario(self):
        try:
            return Salao.objects.get(usuario=self.request.user)
        except Salao.DoesNotExist:
            raise PermissionDenied("Você ainda não cadastrou um salão.")

    def perform_create(self, serializer):
        # Flutter/Thunder manda só {"nome": "..."}
        salao = self._get_salao_do_usuario()
        serializer.save(salao=salao)
