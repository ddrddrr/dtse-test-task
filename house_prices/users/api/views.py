from knox.views import LoginView as KnoxLoginView
from knox.models import AuthToken
from rest_framework.authentication import BasicAuthentication
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from users.api.docs import login_schema, registration_schema
from users.api.serializers import RegistrationSerializer, LoginSerializer


class LoginView(KnoxLoginView):
    authentication_classes = []  # no BasicAuth
    permission_classes = [AllowAny]

    @login_schema
    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        request.user = serializer.validated_data["user"]
        return super().post(request, format)


class RegistrationView(APIView):
    permission_classes = [AllowAny]

    @registration_schema
    def post(self, request):
        ser = RegistrationSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(status=status.HTTP_201_CREATED)
