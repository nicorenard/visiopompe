Documentation Utilisateur
=========================

Introduction
************

l'application **Visiopompe** propose 6 panneaux de gestion pour gérer votre parcs de pompes à vide.

Menu :

+ Pompes
+ Pièces détachées
+ Huiles
+ Kits de maintenance
+ Documentations
+ Administration

Menu Pompes
***********

Le menu **pompes** permet de consulter les stocks de pompes répertoriés au sein de l'application, d'en créer ou
d'accéder à la gestion des inventaires.

1. Consulter stocks :
---------------------

Les informationx en consultation sont les suivantes :

+ Nom de la pompe
+ Modèle de la pompe
+ La marque ou le fabriquant
+ L'état actuel de la pompe
    + 4 états sont disponibles : En activité - En panne - En réparation - En stock
+ La localisation de la pompe qui par du bâtiment à son emplacement dans une pièce.
    + L'emplacement dans la pièce est le seul à être optionnel.
+ La date de prochaine vidange avec 3 colorations possible :

    + **Vert** = date non atteinte,
    + **Orange** = Jour même,
    + **Rouge** = date dépassée.
+ La date de mise en service de la pompe ( Si respectée, elle est la même date que celle introduite dans l'application)
+ Numéro de série de la pompe
+ Numéro d'inventaire : Ce numéro est à introduire depuis le menu de gestion des inventaires (cf : Pompes -> Inventaire Stocks)
+ La phase du moteur : Monophasé ou Triphasé
+ La puissance : 50Hz ou 60Hz
+ La technologie qu'utilise la pompe ( cf : Administration -> Modèle de pompe)
+ L'huile utilisée pour la dernière vidange (cf : Menu Huile)
+ Le vide théorique donné par le fabriquant
+ Le vide réel mesuré par un utilisateur
+ L'historique d'action sur la pompe ( dernière action en date affichée).

Il y a également d'autres informations disponible.

+ Un macaron **ATEX** permet de savoir si la pompe l'est ou pas.
+ 3 boutons sont disponibles également:
    1. Bouton édition avec l'icone du *feuille et stylo* pour éditer le stock
    2. Bouton suppression avec l'icone de la *poubelle* pour supprimer le stock
    3. Bouton carnet de recherche avec l'icône *loupe et feuille* pou voir son historique complet


2. Créer Stock :
-----------------

3. Inventaires Stocks :
-----------------------

Menu Pièces détachées
*********************

1. Consulter :
--------------

2. Créer Stock :
-----------------

Menu Kits maintenance
*********************

1. Consulter :
--------------

2. Créer Stock :
-----------------

Menu Huiles
***********

1. Consulter :
--------------

2. Créer Stock :
-----------------

Menu Documentations
*******************

1. Consulter :
--------------

2. Créer Manuel :
-----------------

Menu Administration
*******************

1. Dashboard :
--------------

2. Modèles de Pompes :
----------------------

3. Fabriquants :
----------------

Dans ce sous-panneau, vous pourrez créer et manager les fabriquants dont les stocks de pompes sont relatés.

> Il faut au moins un fabriquant pour créer un **Modèle de pompe**.

L' information suivante est obligatoire pour la création d'un fabriquant : 

+ Nom 


4. Equipes :
------------

Dans ce sous-panneau, vous pourrez créer et manager les équipes dont les stocks devront appartenir.

> Il faut au moins une équipe pour créer un **stock de pompe**.

Les informations suivantes sont obligatoires pour la création d'une équipe : 

+ Nom complet
+ Abbreviation
+ Localisation


5.Lieux : 
---------

Dans ce sous-panneau, vous pourrez effectuer une gestion des lieux pour désigner l'emplacement de chaque stocks et accessoires au sein de l'application.

Les différentes possibilitées sont les suivantes : 

+ Consultation 
+ Création via un formulaire dédiés présent sur le panneau de gestion.
+ Edition via l'icône *feuille et stylo*
+ Suppression via l'icône *poubelle*

Cela concerne les niveaux suivant de lieux : 

> Sites, 
    |_____Bâtiments, 
            |_______Etages, 
                        |____Pièces.

Ces lieux sont obligatoires à établir avant de créer tous **stocks quelconques** comme **d'équipes** !
