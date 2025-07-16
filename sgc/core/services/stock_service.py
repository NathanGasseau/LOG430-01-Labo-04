class StockService:
    def __init__(self, produit_repository):
        self.produit_repository = produit_repository

    def rechercher_produits(self, criteria):
        return list(self.produit_repository.find(
            produit_id=criteria.get('id'),
            categorie=criteria.get('categorie'),
            nom=criteria.get('nom')
        ))

    def reserver_stock(self, cursor, produit_id, quantite):
        row = self.produit_repository.get_stock_by_produit_id(cursor, produit_id)

        if not row:
            raise Exception(f"Produit {produit_id} introuvable dans le stock.")
        if row[1] < quantite:
            raise Exception(
                f"Stock insuffisant pour le produit {produit_id} "
                f"(stock actuel : {row[1]}, requis : {quantite})"
            )

        nouveau_stock = row[1] - quantite
        self.produit_repository.update_stock(cursor, produit_id, nouveau_stock)

        return {"id": row[0], "stock": nouveau_stock}
