from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import ServicoViewSet

router = DefaultRouter()
router.register("servicos", ServicoViewSet, basename="servico")

urlpatterns = [
    path("", include(router.urls)),
]
