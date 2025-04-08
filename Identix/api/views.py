from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action

from .permissions import IsAuthenticatedClientCredentials
from auth_core.permissions import ScopePermission

# Create your views here.
class WalletPL(ViewSet):
    permission_classes = [
        IsAuthenticatedClientCredentials, 
        ScopePermission
    ]

    @action(detail=False, methods=['get'], url_path="info-user")#em produção será details=True
    def info_user(self, request):
        sn = request.query_params.get('sn')
        return Response({"message": f"retorno busca user Wallet: {sn}"})
