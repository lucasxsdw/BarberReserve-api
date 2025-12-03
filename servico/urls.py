from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import ServicoViewSet

router = DefaultRouter()
router.register("servico", ServicoViewSet, basename="servico")

urlpatterns = [
    path("", include(router.urls)),
]
