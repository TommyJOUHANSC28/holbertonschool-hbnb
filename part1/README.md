# HBnB – Documentation Technique UML

##  Présentation du projet

HBnB est une application backend de location de logements inspirée d’Airbnb.
Elle permet aux utilisateurs de :
- créer un compte,
- publier des logements,
- consulter des logements disponibles,
- laisser des avis,
- gérer les équipements associés aux logements.

Ce dépôt contient la **documentation technique UML** du projet.
Elle décrit l’architecture, les entités métier et les flux d’interaction de l’API.

---

## Objectifs de la documentation

Cette documentation a pour but de :
- expliquer clairement l’architecture du projet,
- décrire les responsabilités de chaque couche,
- présenter les entités principales et leurs relations,
- illustrer le fonctionnement de l’API à travers des diagrammes de séquence.

Elle est destinée aux :
- développeurs,
- architectes logiciels,
- testeurs,
- mainteneurs du projet.

---

## Architecture générale

Le projet HBnB utilise une **architecture à trois couches**.
Chaque couche a un rôle précis et communique uniquement avec la couche voisine.

### Couche Présentation (Presentation Layer)

La couche présentation est le **point d’entrée de l’application**.

Elle est responsable de :
- recevoir les requêtes HTTP du client,
- valider les données de base (formats, champs obligatoires),
- appeler la logique métier appropriée,
- retourner une réponse HTTP au client.

Elle contient principalement :
- des endpoints REST (`/users`, `/places`, `/reviews`, `/amenities`),
- des contrôleurs

Cette couche ne contient **aucune logique métier complexe**.

---

### Couche Métier (Business Logic Layer)

La couche métier contient **l’intelligence de l’application**.

Elle est responsable de :
- appliquer les règles métier,
- vérifier la cohérence des données,
- coordonner les opérations entre la présentation et la persistance.

Elle utilise le **pattern Facade** via une interface centrale :
- `HBnBFacade`

Exemples de règles métier :
- un email utilisateur doit être unique,
- un utilisateur ne peut pas laisser deux avis sur le même logement,
- le prix d’un logement doit être positif.

Cette couche décide **quoi faire** et **comment le faire**.

---

### Couche Persistance (Persistence Layer)

La couche persistance est responsable de la **gestion des données**.

Elle contient :
- des repositories (`UserRepository`, `PlaceRepository`, etc.),
- la logique d’accès à la base de données,
- les opérations CRUD (Create, Read, Update, Delete).

Ses responsabilités :
- sauvegarder les objets métier,
- récupérer les données depuis la base,
- mettre à jour ou supprimer les données.

La logique métier **ne communique jamais directement** avec la base de données.

---

## Pattern de conception utilisé

### Pattern Facade

Le **Facade Pattern** est utilisé pour :
- simplifier les échanges entre les couches,
- réduire le couplage,
- offrir une interface unique à la couche présentation.

La couche présentation appelle uniquement le **Facade**, sans connaître
les détails internes de la logique métier.

---

##  Diagrammes UML

### Diagramme de Paquets (Tâche 0)

Il montre :
- les trois couches de l’architecture,
- le sens de circulation des données,
- la position centrale du Facade.

Les données circulent toujours :

![HBNB UML Tâche 0](UML/task0.png)


---

### Diagramme de Classes (Tâche 1)

[HBNB UML Tâche 1](UML/task1.png)

#### Entités principales

##### User
Représente un utilisateur de l’application.

Attributs :
- id
- email
- password
- first_name
- last_name

Responsabilités :
- gestion du profil utilisateur,
- authentification,
- publication d’avis.

---

##### Place
Représente un logement mis en location.

Attributs :
- id
- owner_id
- name
- description
- price
- location

Responsabilités :
- gestion des informations du logement,
- association avec les équipements,
- réception des avis.

---

##### Review
Représente un avis laissé par un utilisateur.

Attributs :
- id
- place_id
- user_id
- rating
- comment

Responsabilités :
- création et gestion des avis,
- contribution à la note moyenne d’un logement.

---

##### Amenity
Représente un équipement ou service.

Attributs :
- id
- name
- description

Responsabilités :
- gestion du catalogue d’équipements,
- association avec les logements.

---

#### Relations entre les entités

- Un **User** peut posséder plusieurs **Place** (1:N)
- Une **Place** peut avoir plusieurs **Review** (1:N)
- Un **User** peut écrire plusieurs **Review** (1:N)
- Une **Place** peut avoir plusieurs **Amenity** (N:N via table intermédiaire)

---

##  Diagrammes de Séquence (Tâche 2)

Les diagrammes de séquence décrivent le **flux complet d’une requête API**.

### Création d’un utilisateur

[HBNB UML Tâche 2](UML/task2.1.inscription.png)

1. Requête POST `/users`
2. Validation des données par la RestAPI
3. Application des règles métier
4. Vérification de l’unicité de l’email
5. Sauvegarde en base
6. Réponse HTTP `201 Created`

---

### Création d’une propriété

[HBNB UML Tâche 2](UML/task2.1.creation.png)

1. Requête POST `/places`
2. Vérification de l’utilisateur
3. Validation métier (prix, données)
4. Sauvegarde de la propriété
5. Association des équipements
6. Réponse HTTP `201 Created`

---

### Création d’un avis

[HBNB UML Tâche 2](UML/task2.1.review.png)

1. Requête POST `/reviews`
2. Vérification utilisateur et propriété
3. Validation métier (pas de doublon)
4. Sauvegarde de l’avis
5. Mise à jour de la note moyenne
6. Réponse HTTP `201 Created`

---

### Récupération des propriétés

[HBNB UML Tâche 2](UML/task2.1.liste.png)

1. Requête GET `/places`
2. Validation des filtres
3. Application des règles métier
4. Récupération paginée
5. Réponse HTTP `200 OK`

---

##  Qualités techniques du projet

- Séparation claire des responsabilités
- Architecture modulaire et maintenable
- Facilité de test unitaire
- Évolutivité du système
- Respect des bonnes pratiques backend

---

##  Auteurs

- **James Roussel**
- **Tommy Jouhans**

---

##  Projet académique

HBnB – Holberton School  
Documentation technique UML 

[HBNB UML Tâche 3](UML/task3.pdf) 


## Outils utilisés

Pour les diagrammes:

Lucid (https://lucid.app/documents/) pour la simplicité et finition des diagrammes
Mermaid (https://mermaid.live/) pour coder les diagrammes de bases avant finition sur Lucid
Gamma.app (https://gamma.app/docs/HBnB-Documentation-Technique-UML-qv4bnh7yitrwnh9?mode=doc) pour preparer la documentation
