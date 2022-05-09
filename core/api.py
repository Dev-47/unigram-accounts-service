from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from accounts.utils import BaseView
from core.serializers import UserSerializer, LoginSerializer


class UserRegisterAPI(BaseView):

    serializer_class = UserSerializer

    def post(self, request):
        user_register_data = request.data

        user_register_serializer = self.get_serializer(data=user_register_data)
        user_register_serializer.is_valid(raise_exception=True)
        user_register_serializer.save()

        return Response(user_register_serializer.data, status=status.HTTP_201_CREATED)


class UserLoginAPI(BaseView):

    serializer_class = LoginSerializer

    def post(self, request):
        user_login_data = request.data

        user_login_serializer = self.get_serializer(data=user_login_data)
        user_login_serializer.is_valid(raise_exception=True)

        user = authenticate(**user_login_serializer.validated_data)

        if not user:
            return Response(
                {"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
            )

        login(request, user)

        user_serializer = UserSerializer(user)

        return Response(user_serializer.data, status=status.HTTP_200_OK)


class UserLogoutAPI(BaseView):
    def get(self, request):
        logout(request)

        return Response(None, status=status.HTTP_204_NO_CONTENT)


class UserProfileAPI(BaseView):

    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        user_serializer = self.get_serializer(user)

        return Response(user_serializer.data, status=status.HTTP_200_OK)
