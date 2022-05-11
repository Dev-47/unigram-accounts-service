from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from core.api import UserLogoutAPI, UserProfileAPI, UserRegisterAPI

app_name = "core"

urlpatterns = [
    path("auth/register/", UserRegisterAPI.as_view(), name="auth_register"),
    path("auth/login/", TokenObtainPairView.as_view(), name="auth_login"),
    path("auth/token/refresh/", TokenRefreshView.as_view(), name="auth_refresh_token"),
    path("auth/token/verify/", TokenVerifyView.as_view(), name="auth_token_verify"),
    path("auth/logout/", UserLogoutAPI.as_view(), name="auth_logout"),
    path("auth/profile/", UserProfileAPI.as_view(), name="auth_profile"),
]
