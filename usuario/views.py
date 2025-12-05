# usuario/views.py
from django.contrib.auth import authenticate
from django.db import IntegrityError

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, permissions
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

from .models import CustomUser
from .serializers import RegisterSerializer, UserSerializer


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = serializer.save()
        except IntegrityError:
            return Response(
                {"detail": "Já existe um usuário com esse e-mail."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(
            {
                "id": user.id,
                "name": user.first_name,
                "email": user.email,
                "telefone": user.telefone,
            },
            status=status.HTTP_201_CREATED,
        )


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        if not email or not password:
            return Response(
                {"success": False, "message": "Email e senha são obrigatórios"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = authenticate(username=email, password=password)

        if user is None:
            return Response(
                {"success": False, "message": "Credenciais inválidas"},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        refresh = RefreshToken.for_user(user)

        return Response(
            {
                "success": True,
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }
        )


class UsuarioPerfilView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        return Response(
            {
                "id": user.id,
                "nome": user.first_name or user.username,
                "email": user.email,
                "telefone": user.telefone,
            },
            status=status.HTTP_200_OK,
        )


class MeView(generics.RetrieveUpdateAPIView):
    """
    /api/usuario/me/  -> GET: dados do usuário logado
                         PATCH: atualizar tipo_perfil, telefone, first_name etc.
    """
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


class AtualizarTipoPerfilView(APIView):
    """
    POST /api/usuario/tipo-perfil/
    body: { "tipo_perfil": "cliente" ou "salao" }
    Usado quando o usuário escolhe "PROFISSIONAL/SALÃO" na RoleSelectionScreen.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        tipo = request.data.get("tipo_perfil")

        if tipo not in ["cliente", "salao"]:
            return Response(
                {"detail": "tipo_perfil inválido. Use 'cliente' ou 'salao'."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user: CustomUser = request.user
        user.tipo_perfil = tipo
        user.save()

        return Response(UserSerializer(user).data, status=status.HTTP_200_OK)
