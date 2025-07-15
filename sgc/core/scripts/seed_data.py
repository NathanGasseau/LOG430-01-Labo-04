from sgc.core.models import (
    Categorie, Produit, Magasin, StockProduit
)

def run():
    if Categorie.objects.exists() or Produit.objects.exists() or Magasin.objects.exists():
        print("✅ Données déjà présentes, aucun seed nécessaire.")
        return

    print("🌱 Insertion des données de départ...")
    if Categorie.objects.exists() or Produit.objects.exists() or Magasin.objects.exists():
        return  # Évite de dupliquer les données à chaque démarrage

    # Création de catégories
    cat_elec = Categorie.objects.create(nom="Électronique", description="Produits électroniques")
    cat_bureau = Categorie.objects.create(nom="Bureau", description="Fournitures de bureau")

    # Création de produits
    clavier = Produit.objects.create(nom="Clavier mécanique", categorie=cat_elec, prix=120)
    souris = Produit.objects.create(nom="Souris sans fil", categorie=cat_elec, prix=45)
    ecran = Produit.objects.create(nom="Écran 24 pouces", categorie=cat_elec, prix=190)
    agrafeuse = Produit.objects.create(nom="Agrafeuse", categorie=cat_bureau, prix=15)
    bloc_notes = Produit.objects.create(nom="Bloc-notes", categorie=cat_bureau, prix=5)

    # Création de magasins
    magasin_montreal = Magasin.objects.create(nom="Magasin Montréal", adresse="123 rue Ste-Catherine, Montréal")
    magasin_quebec = Magasin.objects.create(nom="Magasin Québec", adresse="456 rue St-Jean, Québec")

    # Création de stock pour chaque produit dans chaque magasin
    for magasin in [magasin_montreal, magasin_quebec]:
        StockProduit.objects.create(produit=clavier, magasin=magasin, quantite=999999999)
        StockProduit.objects.create(produit=souris, magasin=magasin, quantite=999999999)
        StockProduit.objects.create(produit=ecran, magasin=magasin, quantite=999999999)
        StockProduit.objects.create(produit=agrafeuse, magasin=magasin, quantite=15)
        StockProduit.objects.create(produit=bloc_notes, magasin=magasin, quantite=50)
    
