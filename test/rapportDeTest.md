#  Rapport de Tests de Performance

Ce rapport présente les résultats des tests de charge et de performance effectués sur les différentes configurations d’API REST du Système de Gestion de Caisse (SGC). Chaque test inclut des mesures sur la latence, les erreurs, le trafic et un rapport complet généré par K6.

---

##  Test 0 – 1 API Sans Cache

**But** : Évaluer les performances d'une instance unique d’API sans mécanisme de cache.

###  testConsultationSimultanée
- **Observation** : Très forte latence (>7s) et saturation dès peu de requêtes.
- **Conclusion** : Le cache semble essentiel pour les lectures concurrentes.

![Latence et Trafic](0-resultats1APISansCache/testConsultationSimultanée/LatenceEtTrafic.png)
![Erreurs et Saturation](0-resultats1APISansCache/testConsultationSimultanée/ErreursEtSaturation.png)
![Rapport K6](0-resultats1APISansCache/testConsultationSimultanée/RapportK6.png)

###  testEnregistrementVentes
- **Observation** : Latence critique, performances dégradées, erreurs en forte montée.
- **Conclusion** : Inadapté pour un environnement réel sans optimisation.

![Latence et Trafic](0-resultats1APISansCache/testEnregistrementVentes/LatenceEtTrafic.png)
![Erreurs et Saturation](0-resultats1APISansCache/testEnregistrementVentes/ErreursEtSaturation.png)
![Rapport K6](0-resultats1APISansCache/testEnregistrementVentes/RapportK6.png)

---

##  Test 1 – 1 API

**But** : Tester une instance d’API avec cache activé.

###  testConsultationSimultanée
- **Observation** : Gain significatif en latence (~1s), meilleure stabilité.
- **Conclusion** : Le cache améliore clairement la scalabilité lecture seule.

![Latence et Trafic](1-resultats1API/testConsultationSimultanée/LatenceEtTrafic.png)
![Erreurs et Saturation](1-resultats1API/testConsultationSimultanée/ErreursEtSaturation.png)
![Rapport K6](1-resultats1API/testConsultationSimultanée/RapportK6.png)

###  testEnregistrementVentes
- **Observation** : Latence divisée par plus de 10 vs sans cache, trafic acceptable.
- **Conclusion** : Système utilisable avec une seule API si le cache est activé.

![Latence et Trafic](1-resultats1API/testEnregistrementVentes/LatenceEtTrafic.png)
![Erreurs et Saturation](1-resultats1API/testEnregistrementVentes/ErreursEtSaturation.png)
![Rapport K6](1-resultats1API/testEnregistrementVentes/RapportK6.png)

---

##  Test 2 – 2 APIs

###  testConsultationSimultanée
- **Observation** : Latence réduite à ~900 ms, bien plus de requêtes servies.
- **Conclusion** : Bonne amélioration, mais le CPU monte significativement.

![Latence et Trafic](2-resultats2API/testConsultationSimultanée/LatenceEtTrafic.png)
![Erreurs et Saturation](2-resultats2API/testConsultationSimultanée/ErreursEtSaturation.png)
![Rapport K6](2-resultats2API/testConsultationSimultanée/RapportK6.png)

###  testEnregistrementVentes
- **Observation** : Comportement stable, quelques erreurs en pointe.
- **Conclusion** : Suffisant pour une charge modérée, mais à surveiller.

![Latence et Trafic](2-resultats2API/testEnregistrementVentes/LatenceEtTrafic.png)
![Erreurs et Saturation](2-resultats2API/testEnregistrementVentes/ErreursEtSaturation.png)
![Rapport K6](2-resultats2API/testEnregistrementVentes/RapportK6.png)

---

##  Test 3 – 3 APIs

###  testConsultationSimultanée
- **Observation** : Amélioration continue, latence stable autour de 880 ms.
- **Conclusion** : Bon équilibre pour des charges moyennes.

![Latence et Trafic](3-resultats3API/testConsultationSimultanée/LatenceEtTrafic.png)
![Erreurs et Saturation](3-resultats3API/testConsultationSimultanée/ErreursEtSaturation.png)
![Rapport K6](3-resultats3API/testConsultationSimultanée/RapportK6.png)

###  testEnregistrementVentes
- **Observation** : CPU utilisé plus intensément, mais sans saturation.
- **Conclusion** : Performant sans erreur, un bon seuil de base.

![Latence et Trafic](3-resultats3API/testEnregistrementVentes/LatenceEtTrafic.png)
![Erreurs et Saturation](3-resultats3API/testEnregistrementVentes/ErreursEtSaturation.png)
![Rapport K6](3-resultats3API/testEnregistrementVentes/RapportK6.png)

---

##  Test 4 – 4 APIs

###  testConsultationSimultanée
- **Observation** : Usage mémoire élevé, mais latence stable.
- **Conclusion** : Permet un volume élevé sans erreurs.

![Latence et Trafic](4-resultats4API/testConsultationSimultanée/LatenceEtTrafic.png)
![Erreurs et Saturation](4-resultats4API/testConsultationSimultanée/ErreursEtSaturation.png)
![Rapport K6](4-resultats4API/testConsultationSimultanée/RapportK6.png)

###  testEnregistrementVentes
- **Observation** : Résultats comparables à 3 APIs, mais plus stable.
- **Conclusion** : Idéal pour la haute disponibilité.

![Latence et Trafic](4-resultats4API/testEnregistrementVentes/LatenceEtTrafic.png)
![Erreurs et Saturation](4-resultats4API/testEnregistrementVentes/ErreursEtSaturation.png)
![Rapport K6](4-resultats4API/testEnregistrementVentes/RapportK6.png)

---

##  Test 5 – 5 APIs

###  testConsultationSimultanée
- **Observation** : Diminution du CPU par instance, mais latence peu améliorée.
- **Conclusion** : Rendement marginal décroissant.

![Latence et Trafic](5-resultats5API/testConsultationSimultanée/LatenceEtTrafic.png)
![Erreurs et Saturation](5-resultats5API/testConsultationSimultanée/ErreursEtSaturation.png)
![Rapport K6](5-resultats5API/testConsultationSimultanée/RapportK6.png)

###  testEnregistrementVentes
- **Observation** : Même comportement que 4 APIs, voire légère régression.
- **Conclusion** : Ne vaut pas le coût supplémentaire sans pic extrême.

![Latence et Trafic](5-resultats5API/testEnregistrementVentes/LatenceEtTrafic.png)
![Erreurs et Saturation](5-resultats5API/testEnregistrementVentes/ErreursEtSaturation.png)
![Rapport K6](5-resultats5API/testEnregistrementVentes/RapportK6.png)

---

###  Conclusion Générale

- Le cache est **indispensable** dès une seule API.
- La montée en charge avec plusieurs instances **augmente bien le débit**, mais les **gains s’atténuent** à partir de 4.
- Le système reste **fiable jusqu'à 4 APIs** avec une utilisation mémoire stable.
- L'intégration de NGINX et du load balancing a été cruciale pour l'efficacité globale.