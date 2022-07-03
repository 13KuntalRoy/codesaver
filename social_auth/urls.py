from django.urls import path

from social_auth.views.facebookview import FacebookSocialAuthView

from social_auth.views.googleview import GoogleSocialAuthView

urlpatterns = [
    path('google/', GoogleSocialAuthView.as_view()),
    path('facebook/', FacebookSocialAuthView.as_view()),



]