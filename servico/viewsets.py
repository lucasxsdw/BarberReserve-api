from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Servico
from .serializers import ServicoSerializer

class ServicoViewSet(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ServicoSerializer

    def get_queryset(self):
        empresa_id = self.kwargs.get("empresa_id")

        if empresa_id:
            return Servico.objects.filter(empresa_id=empresa_id, ativo=True)

        user = self.request.user
        if hasattr(user, "empresa"):
            return Servico.objects.filter(empresa=user.empresa)

        return Servico.objects.none()

    def perform_create(self, serializer):
        user = self.request.user

        if not hasattr(user, "empresa"):
            raise PermissionError("Somente empresas podem cadastrar serviços.")

        serializer.save(empresa=user.empresa)

   