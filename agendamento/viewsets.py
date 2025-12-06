from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from .models import Agendamento
from .serializers import AgendamentoSerializer

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
                return self.queryset.filter(cliente=user)
            except:
                return Agendamento.objects.none()

        if perfil == "salao":
            try:
                return self.queryset.filter(servico__salao=user.salao)
            except:
                return Agendamento.objects.none()

        return Agendamento.objects.none()

    def create(self, request, *args, **kwargs):
        user = request.user
        perfil = getattr(user, "tipo_perfil", None)

        if perfil != "cliente":
            return Response(
                {"detail": "Somente clientes podem criar agendamentos."},
                status=status.HTTP_403_FORBIDDEN
            )

        serializer = self.get_serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
