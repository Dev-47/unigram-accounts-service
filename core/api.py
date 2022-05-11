from django.contrib.auth import logout
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from accounts.utils import BaseView
from core.serializers import UserSerializer


class UserRegisterAPI(BaseView):

    serializer_class = UserSerializer

    def post(self, request):
        user_register_data = request.data

        user_register_serializer = self.get_serializer(data=user_register_data)
        user_register_serializer.is_valid(raise_exception=True)
        user_register_serializer.save()

        return Response(user_register_serializer.data, status=status.HTTP_201_CREATED)


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
