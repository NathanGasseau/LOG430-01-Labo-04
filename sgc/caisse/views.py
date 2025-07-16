from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from sgc.service_factory import get_caisse_service
from sgc.core.models import LigneVente, Magasin
from django.conf import settings
import requests

def vue_rechercher_produit(request):
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
            headers = {
                "Authorization": f"Token {settings.API_TOKEN}"
            }
            response = requests.get(f"{settings.API_BASE_URL}/api/v1/produits/recherche/", params=criteria_filtrés, headers=headers)
            if response.status_code == 200:
                produits = response.json()
            else:
                print("🔴 API a retourné un statut non-200 :", response.status_code)
                print("📝 Contenu de la réponse :", response.text)
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
            api_url = f"{settings.API_BASE_URL}/api/v1/ventes/"
            headers = {
                "Authorization": f"Token {settings.API_TOKEN}"
            }
            response = requests.post(api_url, json={"produits": ids}, headers=headers)

            if response.status_code == 201:
                total = response.json().get("total", 0)
                return render(request, "caisse/confirmation_vente.html", {"total": total})
            else:
                print("🔴 API a retourné un statut non-200 :", response.status_code)
                print("📝 Contenu de la réponse :", response.text)

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
