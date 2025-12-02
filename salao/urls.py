from django.urls import path
from .views import SalaoListCreateView, MeuSalaoView

urlpatterns = [
    # /api/salao/
    path('', SalaoListCreateView.as_view(), name='salao-list-create'),

    # /api/salao/meu-salao/
    path('meu-salao/', MeuSalaoView.as_view(), name='meu-salao'),
]
