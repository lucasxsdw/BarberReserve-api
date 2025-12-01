from rest_framework import routers
from .viewsets import ProfissionalViewSet

router = routers.DefaultRouter()
router.register("profissional", ProfissionalViewSet)

urlpatterns = router.urls
