# sgc/caisse/services/caisse_service.py

class CaisseService:
    def __init__(self, transaction_manager, stock_service, vente_service):
        self.transaction_manager = transaction_manager
        self.stock_service = stock_service
        self.vente_service = vente_service

    def rechercher_produits(self, criteria):
        print(f"Recherche de produits avec critères : {criteria}")
        return self.stock_service.rechercher_produits(criteria)

    def enregistrer_vente(self, lignes: list, magasin):
        with self.transaction_manager.atomic() as cursor:
            for ligne in lignes:
                success = self.stock_service.reserver_stock(cursor,ligne.produit.id, 1)
                if not success:
                    raise Exception(f"Produit {ligne.produit.nom} en rupture de stock.")
            vente = self.vente_service.enregistrer_vente(cursor, lignes, magasin)
            return vente
