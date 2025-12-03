# profissional/urls.py
from rest_framework.routers import DefaultRouter
from .views import ProfissionalViewSet

router = DefaultRouter()
router.register("", ProfissionalViewSet, basename="profissional")

urlpatterns = router.urls
