from django.urls import include, path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.http import JsonResponse
import socket

from api.controllers import ProduitRechercheView, VenteEnregistrementView

# Config Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="SGC API",
        default_version='v1',
        description="Documentation de l'API REST du SGC",
        terms_of_service="https://www.etsmtl.ca",
        contact=openapi.Contact(email="support@sgc.local"),
        license=openapi.License(name="MIT"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

def ping(request):
    return JsonResponse({"pong": True, "host": socket.gethostname()})

urlpatterns = [
    path('ping/', ping, name='ping'),

    # Endpoints REST
    path('produits/recherche/', ProduitRechercheView.as_view(), name='produit-recherche'),
    path('ventes/', VenteEnregistrementView.as_view(), name='enregistrement_vente'),

  # Documentation Swagger
    path('docs/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('docs/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('', include('django_prometheus.urls')),

]
