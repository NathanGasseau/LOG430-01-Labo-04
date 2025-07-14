# ADR-01: Adoption de Django comme framework principal

## Statut  
Accepté – 7 juin 2025

## Contexte  
Le projet SGC est une application monolithique web/console qui nécessite un framework structurant pour :
- gérer les vues et les interactions avec l’utilisateur (UI interne maison mère),
- interagir avec une base de données relationnelle (PostgreSQL),
- structurer la logique métier en services (ex: `CaisseService`, `StockService`, etc.),
- permettre une intégration simple avec un ORM, du logging, et des tests.

## Décision  
L’architecture adopte **Django** comme framework principal côté serveur, notamment pour supporter la logique métier, la gestion de la base de données, l’encapsulation des services et la configuration du projet.

## Justification  
- Django fournit une **architecture MVC claire**, avec de puissants outils pour modéliser les entités, gérer les formulaires et sérialiser les données.
- Le **ORM Django** facilite l’implémentation des repositories tout en garantissant la compatibilité avec PostgreSQL.
- Le framework offre **une excellente documentation**, une communauté active et de nombreux outils intégrés (authentification, admin, migration, etc.).
- Il permet une **structuration propre** du code autour de modules métiers (`apps`) tout en gardant une logique monolithique.
- Compatible avec l’ajout de points d’entrée gRPC via des extensions ou serveurs complémentaires.

## Conséquences  
- Le projet sera organisé selon les conventions Django (fichiers `models.py`, `views.py`, `urls.py`, etc.).
- La configuration et la gestion du cycle de vie de l’application seront fortement influencées par Django.
- L’équipe doit maîtriser les concepts Django pour maintenir le projet efficacement.
- L’utilisation de Django admin peut accélérer le développement d’interfaces internes pour la maison mère.

