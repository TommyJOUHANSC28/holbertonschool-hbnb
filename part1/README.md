## HBnB-UML par Tommy JOUHANS et James ROUSSEL


# Introduction :

HBnB est une application inspirée d’Airbnb, mais dans une version simplifiée.

Elle vous permet de :

- Gérer les utilisateurs (inscription, profil, administrateur ou non-administrateur)

- Créer et consulter des annonces

- Ajouter des avis aux annonces

- Gérer les équipements associés aux annonces



# Architecture générale (High-Level Package Diagram) - "Task 2"


![HBNB UML Tâche 0](UML/Task0.jpg)

Le projet suit une architecture en couches :

Les 3 couches principales

<u> 1/ Couche de présentation </u>

Il s’agit du point d’entrée du système.

Il contient :

API de service, interface utilisateur Web, API REST

Rôle :

- Recevoir les requêtes utilisateur (HTTP/API)

- Ne pas contenir de logique métier

- Appeler la couche de logique métier

Exemple :

« Un utilisateur souhaite créer un lieu → la requête arrive ici »


<u> 2/ Couche de logique métier </u>

Il s’agit du cœur du projet.

Il contient :

Modèle de base, Utilisateur, Lieu, Avis, Équipement

Rôle :

Appliquer les règles métier, vérifier les données, décider des actions à effectuer avant l’enregistrement dans la base de données

Exemple :

« L’adresse e-mail existe-t-elle déjà ?

La note est-elle comprise entre 1 et 5 ?»


<u> 3/ Couche de persistance </u>

Il s’agit de la couche qui communique avec la base de données.

Il contient :

DatabaseAccess, UserRepository, PlaceRepository, ReviewRepository et AmenityRepository

Rôle :

Enregistrer, lire, modifier et supprimer les données des utilisateurs.

Important :

La logique métier ne communique jamais directement avec la base de données ; elle utilise cette couche.

Modèle de conception Façade (très important).

Le modèle de conception Façade permet de :

- Simplifier les appels entre les couches.

- Masquer la complexité interne.

La couche de présentation appelle une interface unique, sans connaître les détails internes.



# Diagramme de classes détaillé pour la couche de logique métier (Detailed Class Diagram for the Business Logic Layer ) - "Task 1"

![HBNB UML Tâche 1](UML/Task1.jpg)

Attributs:

+ UUID id
→ Identifiant unique de chaque objet (clé primaire).

+ DateTime created_at
→ Date et heure de création de l’objet.

+ DateTime updated_at
→ Date et heure de la dernière mise à jour.

Méthodes

+ void save()
→ Sauvegarde l’objet (en base de données par exemple).

+ void delete()
→ Supprime l’objet.

- Rôle :
BaseModel est une classe mère qui fournit des champs et comportements communs à toutes les autres classes.

<u> 2️/ Héritage (flèches vers BaseModel) </u>

Les flèches pointant vers BaseModel signifient que les classes suivantes héritent de cette classe :

User, Place,  and Review

- Elles possèdent donc automatiquement id, created_at, updated_at, save() et delete().

<u> 3️/ Classe User </u>

Attributs:

+ String name
→ Nom de l’utilisateur.

+ String email
→ Adresse email de l’utilisateur.

Méthodes:

+ void createPlace()
→ Permet à l’utilisateur de créer un lieu.

+ void writeReview()
→ Permet à l’utilisateur d’écrire un avis.


<u> 4️/ Relation User — Place (« Creates ») </u>

1 User → 0.. Place*

Libellé : Creates

Signification :

Un utilisateur peut créer zéro, un ou plusieurs lieux.

Chaque lieu est créé par un seul utilisateur.

<u> 5️/ Classe Place </u>

Attributs:

+ String name
→ Nom du lieu.

+ String location
→ Adresse ou localisation.

+int capacity
→ Capacité maximale du lieu.

Méthodes:

+void addAmenity(Amenity amenity)
→ Ajoute un équipement au lieu.

+void getReviews()
→ Récupère les avis associés au lieu.

<u>6️/ Relation Place — Amenity (« Includes »)</u>

Place → 0.. Amenity*

Libellé : Includes

Signification :

Un lieu peut inclure plusieurs équipements.

Un équipement appartient à un seul lieu (selon ce diagramme).


<u> 7/ Classe Amenity </u>

Attributs:

+String name
→ Nom de l’équipement (ex. Wi-Fi, Parking, Climatisation).

- Pas de méthodes : c’est une classe simple de données.


<u> 8/ Classe Review </u>

Attributs:

+String text
→ Contenu textuel de l’avis.

+int rating
→ Note (par exemple de 1 à 5).

Méthodes

+void editReview(String text)
→ Modifier le texte de l’avis.

+void ratePlace(int rating)
→ Donner ou modifier la note du lieu.


<u> 9/ Relation User — Review (« Writes ») <u>

User → 0.. Review*

Libellé : Writes

Signification :

Un utilisateur peut écrire plusieurs avis.

Chaque avis est écrit par un seul utilisateur.

Relation Place — Review (« Has »)

Place → 0.. Review*

Libellé : Has

Signification :

Un lieu peut avoir plusieurs avis.

Chaque avis concerne un seul lieu.

<u> 10/ Résumé global </u>

BaseModel centralise les champs communs.

Un champ User :

- Crée des Place

- Ecrit des Reviews

Un champ Place :

- Il appartient à un utilisateur

- Il possède des Amenity

- Il reçoit des Review

Un Review relie User et Place


# Diagrammes de séquence pour les appels d'API(Sequence Diagrams for API Calls) - "Task 2"


![HBNB UML Tâche 1](UML/Task2.jpg)


<u> 1️/ Les acteurs du diagramme </u>

De gauche à droite :

User : l’utilisateur final (interface web/mobile)

API : point d’entrée backend (controllers / endpoints)

BusinessLogic : logique métier (règles, validations, traitements)

Database : base de données (stockage et requêtes)

Le temps s’écoule de haut en bas.

Flèches pleines → appel / requête

Flèches pointillées → réponse

Boucles → validations ou traitements internes


<u> 2️/ Inscription de l’utilisateur (Registration) <u>

Étapes :

User → API : envoie email + mot de passe

API → BusinessLogic : validation des données (format, règles)

BusinessLogic → Database : sauvegarde de l’utilisateur

Database → BusinessLogic : confirmation

BusinessLogic → API : succès ou échec

API → User : résultat final (inscription réussie ou erreur)

Objectif : créer un compte utilisateur de manière sécurisée.


<u> 3️/ Création d’un lieu (Place creation) <u>

Étapes :

User → API : demande de création d’un lieu

API → BusinessLogic : validation des données du lieu

BusinessLogic → Database : sauvegarde du lieu

Database → BusinessLogic : confirmation

BusinessLogic → API : lieu créé avec succès

API → User : confirmation de création

Objectif : permettre à un utilisateur d’ajouter un nouveau lieu.


<u> 4️/ Soumission d’un avis (Submit a review) </u>
Étapes :

User → API : soumet un avis

API → BusinessLogic : validation et traitement de l’avis

BusinessLogic → Database : sauvegarde de l’avis

Database → BusinessLogic : confirmation

BusinessLogic → API : avis soumis avec succès

API → User : confirmation

Objectif : enregistrer un avis utilisateur sur un lieu.

<u> 5️/ Recherche de lieux avec filtres (List of places) </u>

Étapes :

User → API : demande la liste des lieux (filtres : localisation, prix)

API : validation des paramètres (filtres, pagination)

API → BusinessLogic : transmet la requête filtrée.

BusinessLogic :

- Il valide les critères.

- Il prépare la requête.

BusinessLogic → Database : requête avec filtres

Database → BusinessLogic : résultats + pagination

BusinessLogic : vérifie et formate la réponse

BusinessLogic → API:

- API → User : liste des lieux ou message d’erreur.

- Objectif est d'afficher une liste de lieux filtrée et paginée.

<u> 6️/ Ce que montre le diagramme globalement</u>

- Séparation claire des responsabilités
- L’API ne contient pas de logique métier
- La BusinessLogic centralise les règles
- La base de données ne fait que stocker et retourner des données
- Gestion systématique des succès / erreurs


<u> Résumé: </u>

Ce diagramme décrit le flux complet d’une application backend bien structurée, depuis les actions utilisateur jusqu’à la base de données, pour l’inscription, la création de contenu, les avis et la recherche.
