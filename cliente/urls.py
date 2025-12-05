from django.urls import path
from .views import DefinirComoClienteView, MeuClienteView

urlpatterns = [
    path("definir/", DefinirComoClienteView.as_view(), name="cliente-definir"),
    path("meu/", MeuClienteView.as_view(), name="cliente-meu"),
]
