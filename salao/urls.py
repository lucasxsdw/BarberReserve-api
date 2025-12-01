from django.urls import path
from .views import SalaoListCreateView

urlpatterns = [
    path('', SalaoListCreateView.as_view(), name='salao-list-create'),
]
