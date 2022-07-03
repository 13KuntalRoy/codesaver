from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from rest_framework import generics
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from accounts.models import USER
from accounts.renderers import UserRenderer
from accounts.serializers import UserRegisterSerializer
from accounts.utils import Util


class UserRegisterView(generics.GenericAPIView):

    # queryset = USER.objects.all()

    serializer_class = UserRegisterSerializer
    renderer_classes = (UserRenderer,)

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            user_data = serializer.data
            user = USER.objects.get(email=user_data['email'])
            token = RefreshToken.for_user(user).access_token
            current_site = get_current_site(request).domain
            relativeLink = reverse('email-verify')
            absurl = 'http://'+current_site+relativeLink+"?token="+str(token)
            email_body = 'Hi '+user.username + \
                ' Use the link below to verify your email \n' + absurl
            data = {'email_body': email_body, 'to_email': user.email,
                    'email_subject': 'Verify your email'}

            Util.send_email(data)
            return Response(
                {
                    "user": UserRegisterSerializer(
                        user, context=self.get_serializer_context()
                    ).data,
                    "status": "Successfully created ngo account",
                }
            )
        else:
            return Response(
                {
                    "status": "couldn't create donner account",
                }
            )
