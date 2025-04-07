# auth_core/oauth2.py
from oauth2_provider.scopes import BaseScopes
from .models import CustomApplication, Scope

class ScopeBackend(BaseScopes):
    def get_all_scopes(self):
        """
        Retorna todos os escopos válidos do sistema.
        """
        return {
            scope.name: scope.description
            for scope in Scope.objects.all()
        }

    def get_default_scopes(self, application=None, request=None, *args, **kwargs):
        """
        Retorna escopos padrão. Pode customizar por aplicação.
        """
        return [scope.name for scope in Scope.objects.all()]

    def get_available_scopes(self, application=None, request=None, *args, **kwargs):
        """
        Escopos disponíveis para a aplicação ou contexto do request.
        Aqui você pode restringir por aplicação, cliente, etc.
        """
        if isinstance(application, CustomApplication):
            return list(application.scopes.values_list("name", flat=True))
        # o retorono abaixo vai servir para chamadas que não são de client credentials
        return [scope.name for scope in Scope.objects.all()]
