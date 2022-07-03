
from django.contrib.auth import authenticate
from accounts.models import USER
import os
import random
from rest_framework.response import Response
from rest_framework import status


def generate_username(name):

    username = "".join(name.split(' ')).lower()
    if not USER.objects.filter(username=username).exists():
        return username
    else:
        random_username = username + str(random.randint(0, 1000))
        return generate_username(random_username)


def register_social_user(provider, user_id, email, name):
    filtered_user_by_email = USER.objects.filter(email=email)
    print('here')
    if filtered_user_by_email.exists():
        print('here1')

        if provider is filtered_user_by_email[0].auth_provider:

            registered_user = authenticate(
                email=email, password=os.environ.get('SOCIAL_SECRET'))

            return {
                'username': registered_user.username,
                'email': registered_user.email,
                'tokens': registered_user.tokens()}

        else:
            print('why')
            return {'details': 'Please continue your login using ' + filtered_user_by_email[0].auth_provider}
          

    else:
        print('here2')
        user = {
            'username': generate_username(name), 
            'email': email,
            'password': os.environ.get('SOCIAL_SECRET')}
      
        user = USER.objects.create_user(**user)
        user.is_verified = True
        user.auth_provider = provider
        user.save()
        print('done')

        new_user = authenticate(
            email=email, password=os.environ.get('SOCIAL_SECRET'))
        return {
            'email': new_user.email,
            'username': new_user.username,
            'tokens': new_user.tokens()
        }