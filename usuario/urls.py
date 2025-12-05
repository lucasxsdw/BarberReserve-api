# usuario/urls.py
from django.urls import path
from .views import (
    RegisterView,
    LoginView,
    UsuarioPerfilView,
    MeView,
    AtualizarTipoPerfilView,
)

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("usuario-perfil/", UsuarioPerfilView.as_view(), name="usuario-perfil"),
    path("me/", MeView.as_view(), name="me"),
    path("tipo-perfil/", AtualizarTipoPerfilView.as_view(), name="usuario-tipo-perfil"),
]
