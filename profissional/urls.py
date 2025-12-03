from rest_framework import routers
from .views import ProfissionalViewSet

router = routers.DefaultRouter()
router.register("", ProfissionalViewSet, basename="profissional")

urlpatterns = router.urls
