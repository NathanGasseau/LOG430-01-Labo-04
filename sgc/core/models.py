# Create your models here.
from django.db import models

class Categorie(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.nom


class Produit(models.Model):
    nom = models.CharField(max_length=100)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    prix = models.FloatField()

    def __str__(self):
        return self.nom


class Magasin(models.Model):
    nom = models.CharField(max_length=100)
    adresse = models.TextField()

    def __str__(self):
        return self.nom


class Vente(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    total = models.FloatField()
    magasin = models.ForeignKey(Magasin, on_delete=models.CASCADE)

    def __str__(self):
        return f"Vente #{self.id} - {self.date}"


class LigneVente(models.Model):
    vente = models.ForeignKey(Vente, related_name="lignes", on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField()


class Retour(models.Model):
    vente = models.ForeignKey(Vente, on_delete=models.CASCADE)
    date_retour = models.DateTimeField(auto_now_add=True)


class ResponsableLogistique(models.Model):
    nom = models.CharField(max_length=100)


class LigneApprovisionnement(models.Model):
    demande = models.ForeignKey('DemandeApprovisionnement', related_name='lignes', on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField()

class DemandeApprovisionnement(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    statut = models.CharField(max_length=50)
    magasinDemandeur = models.ForeignKey(Magasin, on_delete=models.CASCADE)


class MaisonMere(models.Model):
    nom = models.CharField(max_length=100)
    adresse = models.TextField()


class Gestionnaire(models.Model):
    nom = models.CharField(max_length=105)


class StockProduit(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    magasin = models.ForeignKey(Magasin, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField()
