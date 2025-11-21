from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from api.serializers import RegisterSerializer


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()

            return Response(
                {
                    "id": user.id,
                    "name": user.first_name,
                    "email": user.email,
                },
                status=status.HTTP_200_OK
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        if not email or not password:
            return Response(
                {"success": False, "message": "Email e senha são obrigatórios"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Login usando email como username
        user = authenticate(username=email, password=password)

        if user is None:
            return Response(
                {"success": False, "message": "Credenciais inválidas"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        refresh = RefreshToken.for_user(user)

        return Response({
            "success": True,
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        })
