from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Profissional
from .serializers import ProfissionalSerializer


class ProfissionalViewSet(viewsets.ModelViewSet):
    queryset = Profissional.objects.all()
    serializer_class = ProfissionalSerializer
    permission_classes = [AllowAny]
