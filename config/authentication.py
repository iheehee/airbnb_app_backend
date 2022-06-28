from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions


class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        username = request.META.get("HTTP_X_USERNAME")
