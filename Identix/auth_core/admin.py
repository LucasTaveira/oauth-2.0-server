from django.contrib import admin
from oauth2_provider.admin import ApplicationAdmin
from oauth2_provider.models import get_application_model
from .models import Scope
CustomApplication = get_application_model()

# Verifica se já está registrado, se sim, remove
if CustomApplication in admin.site._registry:
    admin.site.unregister(CustomApplication)

# Registra novamente com o seu admin customizado
@admin.register(CustomApplication)
class CustomApplicationAdmin(ApplicationAdmin):  # herda do original para evitar conflitos
    list_display = ("name", "client_id", "user", "client_type", "authorization_grant_type")
    search_fields = ("name", "client_id", "scopes__name")

@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')
