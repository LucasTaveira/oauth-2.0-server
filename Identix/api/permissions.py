from rest_framework.permissions import BasePermission
from oauth2_provider.models import AccessToken

class IsAuthenticatedClientCredentials(BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            return True
        
        if isinstance(request.auth, AccessToken):
            return True

        return False
