# ADR-02: Accès à la base de données via un pool de connexions

## Statut  
Accepté – 7 juin 2025

## Contexte  
Le SGC repose sur une base de données PostgreSQL centralisée, partagée par plusieurs services internes (`CaisseService`, `MaisonMereService`, etc.). Ces services effectuent des opérations fréquentes et concurrentes sur les entités `Vente`, `Produit`, et `DemandeApprovisionnement`. Un accès efficace et fiable à la base est donc essentiel.

## Décision  
L’application utilise un **pool de connexions** pour centraliser et gérer efficacement l’accès concurrent à la base PostgreSQL depuis le serveur monolithique.

## Justification  
- Le **pooling** réduit les coûts de création et destruction des connexions SQL, ce qui améliore les **performances**.
- Il permet de **contrôler le nombre maximal de connexions** ouvertes vers la base, évitant une surcharge du SGBD.
- Il garantit une **réutilisation sécurisée des connexions** entre services (`StockService`, `VenteService`, etc.).
- Il est **nativement supporté** par Django via des outils comme `psycopg2` combiné à `connection pooling` (ex: `pgbouncer`, ou configuration interne de Django).

## Conséquences  
- Tous les **repositories** (`ProduitRepository`, `VenteRepository`, etc.) doivent passer par ce **pool partagé** pour effectuer leurs requêtes.
- La gestion des **transactions** doit respecter l’unité de travail associée à chaque connexion empruntée.
- Des outils de **monitoring de connexions** doivent être mis en place pour détecter des fuites ou surutilisation.
