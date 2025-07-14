from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('produits/', views.vue_rechercher_produit, name='rechercher_produit'),
    path('vente/nouvelle/', views.vue_enregistrer_vente, name='enregistrer_vente'),
    path('vente/retour/', views.vue_gestion_retour, name='gerer_retour'),
    path('stock/', views.vue_stock_magasin, name='consulter_stock_magasin'),
    path('stock-central/', views.vue_stock_central, name='consulter_stock_central'),
    path('approvisionnement/', views.vue_demande_approvisionnement, name='demande_approvisionnement'),
]
