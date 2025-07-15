from django.forms.models import model_to_dict
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from sgc.core.repositories.produit_repository import ProduitRepository
from sgc.core.services.stock_service import StockService
from sgc.service_factory import get_caisse_service
from sgc.core.models import LigneVente, Magasin
from api.authentication import StaticTokenAuthentication
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import serializers
import logging

logger = logging.getLogger(__name__)

# === SCHEMAS ===

class ProduitResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    nom = serializers.CharField()
    prix = serializers.FloatField()
    categorie = serializers.IntegerField()

class VenteRequestSerializer(serializers.Serializer):
    produits = serializers.ListField(child=serializers.IntegerField(), help_text="Liste des IDs de produits à vendre.")

class VenteResponseSerializer(serializers.Serializer):
    message = serializers.CharField()
    total = serializers.FloatField()

# === CONTROLLERS ===

class ProduitRechercheView(APIView):
    authentication_classes = [StaticTokenAuthentication]

    @swagger_auto_schema(
        operation_summary="Recherche de produits",
        manual_parameters=[
            openapi.Parameter('id', openapi.IN_QUERY, type=openapi.TYPE_STRING, required=False, description="ID du produit"),
            openapi.Parameter('nom', openapi.IN_QUERY, type=openapi.TYPE_STRING, required=False, description="Nom du produit"),
            openapi.Parameter('categorie', openapi.IN_QUERY, type=openapi.TYPE_STRING, required=False, description="Nom ou ID de la catégorie"),
        ],
        responses={
            200: ProduitResponseSerializer(many=True),
            400: "Critère de recherche manquant",
            401: openapi.Response("Non authentifié (Token manquant ou invalide)"),
            403: openapi.Response("Accès refusé (Permission insuffisante)"),
            500: "Erreur serveur"
        }
    )
    def get(self, request):
        produit_id = request.query_params.get('id')
        nom = request.query_params.get('nom')
        categorie = request.query_params.get('categorie')

        criteria = {k: v for k, v in {
            'id': produit_id,
            'nom': nom,
            'categorie': categorie
        }.items() if v is not None}

        logger.info(f"🔍 Requête API: recherche de produits avec critères {criteria}")

        if not criteria:
            logger.warning("❗ Requête invalide: aucun critère fourni")
            return Response(
                {"detail": "Vous devez fournir au moins un critère : id, nom ou categorie."},
                status=status.HTTP_400_BAD_REQUEST
            )

        stock_service = StockService(ProduitRepository())

        try:
            produits = stock_service.rechercher_produits(criteria)
            produits_dict = [model_to_dict(p) for p in produits]
            logger.info(f"✅ Recherche réussie : {len(produits_dict)} produits trouvés.")
            return Response(produits_dict)
        except Exception as e:
            logger.error(f"❌ Erreur lors de la recherche de produits: {str(e)}")
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class VenteEnregistrementView(APIView):
    authentication_classes = [StaticTokenAuthentication]

    @swagger_auto_schema(
        operation_summary="Enregistrement d'une vente",
        request_body=VenteRequestSerializer,
        responses={
            201: VenteResponseSerializer,
            400: "Aucun produit fourni",
            401: openapi.Response("Non authentifié (Token manquant ou invalide)"),
            403: openapi.Response("Accès refusé (Permission insuffisante)"),
            500: "Erreur serveur"
        }
    )
    def post(self, request):
        logger.info(f"🛒 Requête API: enregistrement d'une vente avec payload {request.data}")

        try:
            ids = request.data.get("produits", [])
            if not ids:
                logger.warning("❗ Aucune liste de produits reçue pour la vente.")
                return Response({"detail": "Aucun produit fourni."}, status=status.HTTP_400_BAD_REQUEST)

            caisse_service = get_caisse_service()

            lignes = []
            for pid in ids:
                produits = caisse_service.rechercher_produits({'id': pid})
                if not produits:
                    raise Exception(f"Produit avec ID {pid} introuvable.")
                lignes.append(LigneVente(produit=produits[0], quantite=1))

            magasin = Magasin.objects.first()
            vente = caisse_service.enregistrer_vente(lignes, magasin)

            logger.info(f"✅ Vente enregistrée : total = {vente['total']}, produits = {ids}")
            return Response({"message": "Vente enregistrée", "total": vente["total"]}, status=status.HTTP_201_CREATED)

        except Exception as e:
            logger.error(f"❌ Erreur lors de l'enregistrement de la vente: {str(e)}")
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
