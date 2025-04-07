from rest_framework.permissions import BasePermission

class ScopePermission(BasePermission):
    def has_permission(self, request, view):
        list_request = request.path.split('/')
        list_user = request.auth.scope.split(' ')
        if bool(set(list_user) & set(list_request)):
            return True
        return False