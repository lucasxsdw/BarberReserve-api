# servico/urls.py
from rest_framework.routers import DefaultRouter
from .viewsets import ServicoViewSet

router = DefaultRouter()
router.register("", ServicoViewSet, basename="servico")

urlpatterns = router.urls
