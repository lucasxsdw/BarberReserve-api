from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import SalaoViewSet

router = DefaultRouter()
router.register("", SalaoViewSet, basename="salao")

urlpatterns = [
    path("", include(router.urls)),
]
