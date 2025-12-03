from rest_framework import viewsets, permissions
from rest_framework.exceptions import NotFound
from .models import Salao
from .serializers import SalaoSerializer


class SalaoViewSet(viewsets.ModelViewSet):
    """
    /api/salao/           -> GET (lista) / POST (cria)
    /api/salao/<id>/      -> GET / PUT / PATCH / DELETE
    """
    serializer_class = SalaoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # só salões do usuário logado
        return Salao.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)
