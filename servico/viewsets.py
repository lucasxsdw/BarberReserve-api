from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import PermissionDenied

from .models import Servico
from .serializers import ServicoSerializer

class ServicoViewSet(ModelViewSet):  # <- IMPORTANTE: ModelViewSet
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ServicoSerializer

    def get_queryset(self):
        salao_id = self.request.query_params.get('salao_id', None)
        
        if salao_id is not None:
            return Servico.objects.filter(salao_id=salao_id)

        user = self.request.user
        if hasattr(user, "salao"):
            return Servico.objects.filter(salao=user.salao)

        return Servico.objects.none()

    def perform_create(self, serializer):
        user = self.request.user

        if not hasattr(user, "salao"):
            raise PermissionDenied("Somente salões podem cadastrar serviços.")

        serializer.save(salao=user.salao)
