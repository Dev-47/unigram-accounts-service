from django.urls import path

from core.api import UserLoginAPI, UserLogoutAPI, UserProfileAPI, UserRegisterAPI

app_name = "core"

urlpatterns = [
    path("auth/register/", UserRegisterAPI.as_view(), name="auth_register"),
    path("auth/login/", UserLoginAPI.as_view(), name="auth_login"),
    path("auth/logout/", UserLogoutAPI.as_view(), name="auth_logout"),
    path("auth/profile/", UserProfileAPI.as_view(), name="auth_profile"),
]
