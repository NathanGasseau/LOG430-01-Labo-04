from datetime import datetime

class VenteService:
    def __init__(self, vente_repository, stock_service):
        self.vente_repository = vente_repository
        self.stock_service = stock_service

    def enregistrer_vente(self, cursor, lignes: list, magasin):
        now = datetime.now()
        vente_id = self.vente_repository.create_vente(cursor, magasin.id, now)
        total = 0

        for ligne in lignes:
            produit = ligne.produit
            quantite = ligne.quantite

            self.stock_service.reserver_stock(cursor, produit.id, quantite)
            self.vente_repository.add_ligne_vente(cursor, vente_id, produit.id, quantite)
            total += produit.prix * quantite

        self.vente_repository.update_total(cursor, vente_id, total)

        return {
            "id": vente_id,
            "total": total,
            "date": now,
            "magasin": magasin.nom,
        }
