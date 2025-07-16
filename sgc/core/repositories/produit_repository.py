# sgc/core/repositories/produit_repository.py

import hashlib
import json
from django.core.cache import cache

class ProduitRepository:
    def find(self, produit_id=None, categorie=None, nom=None):
        from sgc.core.models import Produit

        # Clé de cache basée sur les critères
        criteria = {
            "produit_id": produit_id,
            "categorie": categorie,
            "nom": nom
        }
        cache_key = "produit_search_" + hashlib.md5(json.dumps(criteria, sort_keys=True).encode()).hexdigest()

        # Vérifier le cache
        produits = cache.get(cache_key)
        if produits is not None:
            return produits

        # Sinon, faire la requête
        queryset = Produit.objects.all()
        if produit_id:
            queryset = queryset.filter(id=produit_id)
        if categorie:
            queryset = queryset.filter(categorie__nom__icontains=categorie)
        if nom:
            queryset = queryset.filter(nom__icontains=nom)

        produits = list(queryset)
        cache.set(cache_key, produits, timeout=60)
        return produits

    def get_stock_by_produit_id(self, cursor, produit_id):
        cache_key = f"stock_produit_{produit_id}"
        stock = cache.get(cache_key)
        if stock is not None:
            return stock

        cursor.execute("SELECT id, quantite FROM core_stockproduit WHERE produit_id = %s", [produit_id])
        stock = cursor.fetchone()
        if stock:
            cache.set(cache_key, stock, timeout=60)
        return stock

    def update_stock(self, cursor, produit_id, nouvelle_quantite):
        # Invalider la cache avant mise à jour
        cache_key = f"stock_produit_{produit_id}"
        cache.delete(cache_key)

        cursor.execute(
            "UPDATE core_stockproduit SET quantite = %s WHERE produit_id = %s",
            [nouvelle_quantite, produit_id]
        )
