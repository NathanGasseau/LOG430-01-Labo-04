# ADR-04: Séparation entre `CaisseService` et `MaisonMereService`

## Statut  
Accepté – 7 juin 2025

## Contexte  
Les cas d’utilisation du système sont destinés à deux types d’utilisateurs :
- Les **employés de magasin**, qui effectuent des opérations de caisse
- Les **gestionnaires** de la maison mère, qui supervisent et analysent les opérations

## Décision  
Création de deux **façades distinctes** :
- `CaisseService` : opérations locales (vente, retour, consultation stock)
- `MaisonMereService` : opérations stratégiques (rapports, statistiques multi-magasins)

## Justification  
- Clarifie la **responsabilité fonctionnelle** de chaque service
- Facilite la **sécurisation des accès** (droits différenciés)
- Permet une **meilleure lisibilité du code** et une évolution modulaire

## Conséquences  
- Deux interfaces gRPC différentes doivent être exposées
- Les services métiers communs (stock, vente) sont partagés par les deux