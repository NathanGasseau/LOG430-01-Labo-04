from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.conf import settings

class StaticTokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.headers.get('Authorization')
        expected = f"Token {settings.API_TOKEN}"

        if token != expected:
            raise AuthenticationFailed("Token invalide ou manquant")

        return (None, None)  # On ne gère pas d’utilisateur Django ici
