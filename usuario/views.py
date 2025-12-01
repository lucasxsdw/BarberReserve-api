from rest_framework import generics, permissions
from .models import CustomUser
from .serializers import UserSerializer

class MeView(generics.RetrieveUpdateAPIView):
    """
    /api/me/  -> GET: dados do usuário logado
                 PATCH: atualizar tipo_perfil, telefone, first_name etc.
    """
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
