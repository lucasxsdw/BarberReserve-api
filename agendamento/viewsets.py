# agendamento/views.py
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
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
                return self.queryset.filter(cliente=user.cliente)
            except:
                return Agendamento.objects.none()

        if perfil == "salao":
            try:
                return self.queryset.filter(servico__salao=user.salao)
            except:
                return Agendamento.objects.none()

        return Agendamento.objects.none()

    def perform_create(self, serializer):
        user = self.request.user
        cliente = getattr(user, "cliente", None)
        serializer.save(cliente=cliente)
