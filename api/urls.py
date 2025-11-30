from django.urls import path, include
from .views import RegisterView, LoginView, UsuarioPerfilView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    #path("servico/", include("servico.urls"))
    path("usuario-perfil/", UsuarioPerfilView.as_view(), name="usuario-perfil"),
]