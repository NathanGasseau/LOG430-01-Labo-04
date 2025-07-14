from django.urls import path
from . import views
from django.shortcuts import render, redirect
from django.contrib import messages
from sgc.caisse.services.caisse_service import CaisseService
from sgc.core.models import Produit, LigneVente, Magasin  # modèles nécessaires


def vue_accueil_caisse(request):
    print("Accès à la vue d'accueil de la caisse")
    return render(request, 'accueil.html')