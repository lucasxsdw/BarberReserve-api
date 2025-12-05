from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Agendamento
from .serializers import AgendamentoSerializer

from rest_framework.response import Response
from rest_framework import status

class AgendamentoViewSet(viewsets.ModelViewSet):
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        perfil = getattr(user, "tipo_perfil", None)

        if perfil == "cliente":
            try:
                return self.queryset.filter(cliente=user.cliente)
            except:
                return Agendamento.objects.none()

        if perfil == "salao":
            try:
                return self.queryset.filter(servico__salao=user.salao)
            except:
                return Agendamento.objects.none()

        return Agendamento.objects.none()

    def create(self, request, *args, **kwargs):
        user = self.request.user
        cliente = getattr(user, "cliente", None)

        if cliente is None:
            return Response(
                {"detail": "Usuário logado não é um cliente válido."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Cria uma cópia mutável do request.data
        data = request.data.copy()
        data['cliente'] = cliente.id

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
