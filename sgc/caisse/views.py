from django.shortcuts import render, redirect
from django.contrib import messages
from sgc.service_factory import get_caisse_service
from sgc.core.models import LigneVente, Magasin
import requests

def vue_rechercher_produit(request):
    print("Recherche de produit avec critères :", request.GET)

    critere_nom = request.GET.get('nom', '').strip()
    critere_cat = request.GET.get('categorie', '').strip()
    critere_id = request.GET.get('id', '').strip()

    criteria = {
        'nom': critere_nom,
        'categorie': critere_cat,
        'id': critere_id
    }
    criteria_filtrés = {k: v for k, v in criteria.items() if v}

    produits = []
    if criteria_filtrés:
        try:
            response = requests.get("http://localhost:8000/api/v1/produits/recherche/", params=criteria_filtrés)
            if response.status_code == 200:
                produits = response.json()
            else:
                print("🔴 API a retourné un statut non-200 :", response.status_code)
        except Exception as e:
            print("🔴 Erreur lors de l'appel à l'API :", e)

    return render(request, 'caisse/produits.html', {
        'produits': produits,
        'criteres': criteria
    })

def vue_enregistrer_vente(request):
    if request.method == "POST":
        try:
            # Lire les IDs envoyés via le formulaire
            ids_str = request.POST.get("produits", "")
            ids = [int(pid.strip()) for pid in ids_str.split(",") if pid.strip().isdigit()]

            if not ids:
                raise Exception("Aucun identifiant de produit valide fourni.")

            # Appeler l'API REST pour enregistrer la vente
            api_url = "http://localhost:8000//api/v1/ventes/"
            response = requests.post(api_url, json={"produits": ids})

            if response.status_code == 201:
                total = response.json().get("total", 0)
                return render(request, "caisse/confirmation_vente.html", {"total": total})
            else:
                raise Exception(response.json().get("detail", "Erreur inconnue de l'API"))

        except Exception as e:
            messages.error(request, str(e))

    return render(request, "caisse/vente.html")

def vue_gestion_retour(request):
    if request.method == 'POST':
        # Traiter le retour via VenteService
        pass
    return render(request, 'caisse/retour.html')

def vue_stock_magasin(request):
    # Appeler StockService pour afficher le stock local
    return render(request, 'caisse/stock_magasin.html')

def vue_stock_central(request):
    # Appeler StockService pour afficher le stock central
    return render(request, 'caisse/stock_central.html')

def vue_demande_approvisionnement(request):
    if request.method == 'POST':
        # Initier une demande via DemandeApprovisionnementService
        pass
    return render(request, 'caisse/demande_approvisionnement.html')
