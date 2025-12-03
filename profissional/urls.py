# profissional/urls.py
from rest_framework.routers import DefaultRouter
from .views import ProfissionalViewSet

router = routers.DefaultRouter()
router.register("profissional", ProfissionalViewSet)

urlpatterns = router.urls
