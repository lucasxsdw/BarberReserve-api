from django.urls import path
from .views import ProfissionalListCreateView

urlpatterns = [
    # /api/profissional/
    path('', ProfissionalListCreateView.as_view(), name='profissional-list-create'),
]
