from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import AgendamentoViewSet

router = DefaultRouter()
router.register("agendamento", AgendamentoViewSet, basename="agendamento")


urlpatterns = [
    path("", include(router.urls))
]
