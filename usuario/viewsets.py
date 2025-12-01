from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from usuario.serializers import RegisterSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.db import IntegrityError


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        if not serializer.is_valid():
            # validação do serializer (campos obrigatórios, formato, etc.)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            # aqui pode estourar IntegrityError se o email/username já existir
            user = serializer.save()
        except IntegrityError:
            return Response(
                {
                    "detail": "Já existe um usuário com esse e-mail."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        # se deu tudo certo, devolve os dados do novo usuário
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
