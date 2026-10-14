### MODELWATCH 
![monitoring](/artifacts/monitoring.webp)

**ModelWatch** est une plateforme évolutive qui permet de surveiller les ***performances*** d'un modèle de machine learning, la ***qualité des données***, la ***dérive des distributions(Drift Concept)***



### 1 - Problème :

La plupart des Data scientists, ingénieurs machine learning, startups AI ou entreprises developpent des modèles d'IA ou ML au quotidien et surtout avec la montée en puissance de l'intelligence artificielle, une question se pose **après entrainement des modèles, qui se chargent de surveiller leur performances, d'identifier la dérive de concept ou meme la qualité des données ?**
Un modèle peut perdre en performance lorsque les données changent, sans que l'equipe s'en aperçoive immédiatement. 

 * **Comment vérifiez-vous la fiabilité d'un modèle ML en production ?**

 * **Comment identifier ou déterminer le conceft de dérive de données (Data Concept Drift) ?**


### 2 - Objectives & Developments

Avec **ModelWatch**, vous avez : 


-   **1 - Monitoring**   
-   **2-  Journalisation(logs)** 
-   **3-  Entrainement** 
-   **4-  Inference API** 
-   **5-  Alertes**  
-   **6-  Dashboard**  
-   **7-  Tests**  
-   **8-  Deployment** 
-   **9-  Metrics**



### 3. Conception détaillée de ModelWatch


Les équipes qui déploient des modèles ont besoin de répondre à quatre questions :

- Les données reçues ressemblent-elles encore aux données d'entraînement ?

- Les prédictions ont-elles changé de manière inhabituelle ?

- Les performances diminuent-elles lorsque les résultats réels deviennent disponibles ?

- Quelles variables contribuent le plus à la dérive observée ?

Hypothèse à valider : un outil léger, simple à installer et doté d'indicateurs interprétables pourrait aider une petite équipe ML à détecter plus tôt les problèmes de données et de performance.


### Pour qui ?

Les utilisateurs visés:

- Les ML Engineers qui déploient des modèles via une API.
- Les Data Scientists qui doivent suivre les modèles après leur mise en production.

- Les petites équipes IA qui n'ont pas encore de plateforme MLOps complète.

- Les étudiants qui veulent comprendre le monitoring des modèles.





Stack recommandée
Composant	Technologie
Langage	Python
Modèle et preprocessing	scikit-learn
API	FastAPI + Pydantic
Analyse des données	pandas, NumPy, SciPy
Monitoring	PSI, test de Kolmogorov-Smirnov et métriques scikit-learn
Interface	Streamlit
Tests	pytest
Stockage MVP	SQLite ou fichiers Parquet/CSV
Packaging	Docker
Automatisation	GitHub Actions
Cette stack évite les coûts d'infrastructure et rend le projet reproductible sur un ordinateur personnel.
Quelles données utiliser ?
Je te conseille de commencer avec un dataset de classification tabulaire public, comme le Bank Marketing de l'UCI Machine Learning Repository. Il permet de travailler sur des variables numériques et catégorielles, mais nécessite de télécharger les données et de vérifier leur licence et leurs modalités d'utilisation.
Le protocole expérimental serait le suivant :
1. Entraîner un modèle de référence sur un premier échantillon.
2. Conserver un échantillon de référence pour mesurer les distributions initiales.
3. Construire un lot de données de référence et un lot de données modifiées, en documentant exactement la transformation.
4. Mesurer si le monitoring détecte cette modification.
5. Lorsque les vraies étiquettes sont disponibles, comparer les performances du modèle sur les deux lots.
Tu peux commencer avec un échantillon et simuler la dérive sans dépendre d'un flux de données en direct.
Les métriques qui feront la différence
Mesure	Ce qu'elle permet d'observer
PSI	Écart entre les distributions de référence et récentes
Test KS	Différence entre deux distributions numériques
Dérive catégorielle	Évolution de la fréquence des modalités
F1, précision, rappel	Qualité des prédictions lorsque les labels sont connus
Latence p50/p95	Temps de réponse de l'API, si mesuré correctement
Taux de valeurs manquantes	Dégradation ou changement dans la qualité des données
Attention à un point important : la dérive des données ne prouve pas à elle seule une baisse des performances. Ton application doit distinguer clairement les alertes de dérive des alertes de performance. Le PSI et le test KS doivent aussi être accompagnés d'une interprétation, car leur seuil dépend du contexte.
4. Plan d'exécution sur 14 jours
J1–J2
Cadrage

Cadrage, données et baseline
- Créer le dépôt GitHub et un environnement Python propre.
- Télécharger et inspecter le dataset.
- Définir le protocole de référence et entraîner le premier modèle.
- Sauvegarder les métriques initiales.
Livrable : notebook d'exploration et baseline reproductible.



J3–J4
API

Développer le service de prédiction
- Construire le pipeline scikit-learn.
- Ajouter les endpoints de prédiction et de santé.
- Valider les entrées avec Pydantic.
- Enregistrer les prédictions et les informations nécessaires au suivi.
Livrable : API fonctionnelle avec documentation OpenAPI.



J5–J6
Monitoring

Implémenter les détecteurs de dérive
- Calculer les statistiques de référence.
- Développer PSI et le test KS pour les variables numériques.
- Ajouter le suivi des catégories et des valeurs manquantes.
- Définir des seuils configurables et expliquer leurs limites.
Livrable : rapport de dérive calculé automatiquement.



J7–J8
Évaluation

Tester le système sur des scénarios contrôlés
- Simuler plusieurs types de changements.
- Mesurer les alertes déclenchées.
- Comparer les performances lorsqu'on dispose des labels.
- Vérifier les faux positifs et les cas où la dérive passe inaperçue.
Livrable : résultats expérimentaux et limites documentées.



J9–J10
Interface

Construire le dashboard
- Afficher la baseline et les données récentes.
- Visualiser les variables les plus affectées.
- Afficher les métriques de performance et les alertes.
- Préparer un scénario de démonstration de bout en bout.
Livrable : dashboard utilisable en local.



J11–J12
Qualité

Tests, Docker et intégration continue
- Ajouter les tests unitaires et d'intégration.
- Vérifier les entrées invalides et les cas limites.
- Conteneuriser le service.
- Exécuter les tests automatiquement avec GitHub Actions.
Livrable : installation reproductible et tests automatisés.



J13–J14
Portfolio

Finaliser et présenter le projet
- Écrire un README avec architecture, installation et résultats.
- Ajouter un schéma technique et un exemple d'API.
- Enregistrer une courte démonstration.
- Déployer si le temps et les ressources le permettent ; sinon fournir une démo Docker locale reproductible.
Livrable : dépôt public prêt à être présenté à un recruteur.

Je viserais ces résultats avant de considérer le projet terminé :
- Une commande permet de reproduire l'entraînement et l'évaluation.
- L'API fonctionne et possède des tests.
- Le monitoring détecte correctement au moins quelques scénarios de dérive documentés.
- Le tableau de bord distingue dérive des données et baisse de performance.
- Le README explique les limites, les résultats et les choix techniques.
- Une démonstration montre un scénario normal puis un scénario dégradé.

### Squelette du projet
















Prépare le squelette complet et concret de ModelWatch pour 14 jours : arborescence du dépôt, dépendances, schémas des modules, dataset, contrats API, tests initiaux et commandes de lancement. Avançons étape par étape, sans générer inutilement tout le code d'un coup.



### Étape 1 — Architecture et initialisation
1. Architecture cible
Dataset de référence
Données d'entraînement · Prétraitement · Modèle scikit-learn

API FastAPI
Validation des entrées · Prédictions · Journalisation

Monitoring Engine
Dérive des données · Qualité · Performance


Streamlit Dashboard
Indicateurs · Graphiques · Alertes



Qualité transverse : tests pytest, CI GitHub Actions, Docker et documentation.

Le principe important : l'API sert à prédire, tandis que le moteur de monitoring analyse les observations. Les deux ne doivent pas être confondus.
2. Stack technique
Besoin	Choix
Langage	Python 3.11
Manipulation des données	pandas, NumPy
Modèle ML	scikit-learn
API REST	FastAPI, Uvicorn, Pydantic
Tests	pytest, HTTPX
Visualisation	Streamlit, Plotly
Stockage initial	SQLite
Packaging	Docker
CI	GitHub Actions


5. Contrats de l'API
Nous définirons les contrats maintenant, puis nous les implémenterons lorsque le modèle sera disponible.
Méthode	Endpoint	Rôle
GET	/health	Vérifier que l'API fonctionne
GET	/model/info	Consulter la version du modèle et ses métadonnées
POST	/predict	Obtenir des prédictions et probabilités
POST	/monitor/batches	Enregistrer un lot d'observations pour le monitoring
GET	/monitor/report/latest	Consulter le dernier rapport de dérive et de qualité