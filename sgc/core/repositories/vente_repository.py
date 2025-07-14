class VenteRepository:
    def create_vente(self, cursor, magasin_id, date, total=0):
        cursor.execute(
            "INSERT INTO core_vente (date, magasin_id, total) VALUES (%s, %s, %s) RETURNING id",
            [date, magasin_id, total]
        )
        return cursor.fetchone()[0]

    def add_ligne_vente(self, cursor, vente_id, produit_id, quantite):
        cursor.execute(
            "INSERT INTO core_lignevente (vente_id, produit_id, quantite) VALUES (%s, %s, %s)",
            [vente_id, produit_id, quantite]
        )

    def update_total(self, cursor, vente_id, total):
        cursor.execute(
            "UPDATE core_vente SET total = %s WHERE id = %s",
            [total, vente_id]
        )
