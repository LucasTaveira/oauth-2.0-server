from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WalletPL

router = DefaultRouter()

router.register(r'wallet', WalletPL, basename='wallet')

urlpatterns = [
    path("", include(router.urls))
]