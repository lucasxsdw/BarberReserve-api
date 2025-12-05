from rest_framework import viewsets, permissions
from rest_framework.exceptions import PermissionDenied
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Profissional
from .serializers import ProfissionalSerializer
from salao.models import Salao


class ProfissionalViewSet(viewsets.ModelViewSet):
    """
    GET    /api/profissional/       -> lista profissionais do salão do usuário logado (perfil salao)
    POST   /api/profissional/       -> cria profissional ligado ao salão do usuário logado
    GET    /api/profissional/<id>/  -> detalhe de um profissional do salão do usuário
    PUT    /api/profissional/<id>/  -> atualiza profissional do salão do usuário
    PATCH  /api/profissional/<id>/  -> atualiza parcial
    DELETE /api/profissional/<id>/  -> exclui profissional do salão do usuário
    """
    serializer_class = ProfissionalSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def _assert_is_salao(self):
        user = self.request.user
        if getattr(user, "tipo_perfil", None) != "salao":
            # se quiser, pode devolver queryset vazio ao invés de exception
            raise PermissionDenied("Apenas usuários com perfil 'salao' podem gerenciar profissionais.")

    def get_queryset(self):
        # só profissionais do salão do usuário logado
        self._assert_is_salao()
        user = self.request.user
        return Profissional.objects.filter(salao__usuario=user)

    def _get_salao_do_usuario(self):
        self._assert_is_salao()
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
