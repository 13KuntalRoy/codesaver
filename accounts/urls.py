
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from accounts.views.login import LoginAPIView
from accounts.views.logout import APILogoutView
from accounts.views.PasswordTokenCheck import PasswordTokenCheckAPI
from accounts.views.register import UserRegisterView
from accounts.views.request_password_resetEmail import \
    RequestPasswordResetEmail
from accounts.views.SetNewPassword import SetNewPasswordAPIView
from accounts.views.verify_email import VerifyEmail

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name="register"),
    path('login/', LoginAPIView.as_view(), name="login"),
    path('logout/', APILogoutView.as_view(), name="logout"),
    path('email-verify/', VerifyEmail.as_view(), name="email-verify"),
    path("login/token/refresh/",
         TokenRefreshView.as_view(), name="token_refresh"),
    path("login/token/verify/",
         TokenVerifyView.as_view(), name="token_verify"),
    path('request-reset-email/', RequestPasswordResetEmail.as_view(),
         name="request-reset-email"),
    path('password-reset/<uidb64>/<token>/',
         PasswordTokenCheckAPI.as_view(), name='password-reset-confirm'),
    path('password-reset-complete', SetNewPasswordAPIView.as_view(),
         name='password-reset-complete')
]
