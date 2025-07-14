# sgc/core/repositories/produit_repository.py

class ProduitRepository:
    def find(self, produit_id=None, categorie=None, nom=None):
        from sgc.core.models import Produit

        queryset = Produit.objects.all()

        if produit_id:
            queryset = queryset.filter(id=produit_id)
        if categorie:
            queryset = queryset.filter(categorie__nom__icontains=categorie)
        if nom:
            queryset = queryset.filter(nom__icontains=nom)

        return queryset

    def get_stock_by_produit_id(self, cursor, produit_id):
        cursor.execute("SELECT id, quantite FROM core_stockproduit WHERE produit_id = %s", [produit_id])
        return cursor.fetchone()

    def update_stock(self, cursor, produit_id, nouvelle_quantite):
        cursor.execute(
            "UPDATE core_stockproduit SET quantite = %s WHERE produit_id = %s",
            [nouvelle_quantite, produit_id]
        )
