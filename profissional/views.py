from rest_framework import viewsets, permissions
from rest_framework.exceptions import PermissionDenied

from .models import Profissional
from .serializers import ProfissionalSerializer
from salao.models import Salao


class ProfissionalViewSet(viewsets.ModelViewSet):
    """
    GET    /api/profissional/       -> lista profissionais do salão do usuário logado
    POST   /api/profissional/       -> cria profissional ligado ao salão do usuário logado
    GET    /api/profissional/<id>/  -> detalhe de um profissional do salão do usuário
    PUT    /api/profissional/<id>/  -> atualiza profissional do salão do usuário
    PATCH  /api/profissional/<id>/  -> atualiza parcial
    DELETE /api/profissional/<id>/  -> exclui profissional do salão do usuário
    """
    serializer_class = ProfissionalSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # só profissionais do salão do usuário logado
        user = self.request.user
        return Profissional.objects.filter(salao__usuario=user)

    def _get_salao_do_usuario(self):
        try:
            return Salao.objects.get(usuario=self.request.user)
        except Salao.DoesNotExist:
            raise PermissionDenied("Você ainda não cadastrou um salão.")

    def perform_create(self, serializer):
        # Flutter manda só {"nome": "..."} → aqui a gente injeta o salão correto
        salao = self._get_salao_do_usuario()
        serializer.save(salao=salao)

    def perform_update(self, serializer):
        # garante que ninguém consiga “roubar” profissional de outro salão via payload
        salao = self._get_salao_do_usuario()
        serializer.save(salao=salao)
