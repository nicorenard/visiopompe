Documentation Utilisateur
=========================

Version : 1.0

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

Le menu **pompes** permet de consulter les stocks de pompes et d'en effectuer la gestion (création, édition, suppression). 
Il permet aussi d'accéder à la gestion des numéros d'inventaires.

1. Consulter stocks :
---------------------

Les informations en consultation sont les suivantes :

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
    3. Bouton carnet de recherche avec l'icône *loupe et feuille* pour voir l'historique complet du stock


2. Créer Stock :
-----------------

Ce formulaire permet la création d'un stock de pompe.

Voici les informations obligatoires pour en créer : 

+ Modèle de pompe
+ Etage
+ Pièce
+ Numéro de série

Par validation, la mise en service, la puissance, la technologie, la date de la prochaine vidange seront enregistrées et le statut "en activité" sera inclu.

-- Il est à noter que **sans** *numéro d'inventaire* , *d'équipe* ou d'autres informations comme *l'historique*, amoindri le suivi et la gestion du stock créé dans le temps.



3. Inventaires Stocks :
-----------------------

Ce sous panneau permet la gestion des numéros d'inventaires pour les stocks de pompes.

Deux formulaires sont présents : 

+ L'ajout d'une tutelle budgétaire
+ L'ajout d'un numéro d'inventoriat

> L'ajout d'une tutelle est obligatoire avant de pouvoir créer un numéro.

Il y a également un tableau de consultation des numéros créés triés par tutelle budgétaire.

L'édition et la suppression des différents numéros sont possibles.

Pour effectuer ces actions, différentes icônes sont présentes : 

+ Icône *page avec crayon* : permet l'édition complète du numéro d'inventaire.
+ Icône *poubelle* : permet la suppression d'un numéro.


Menu Pièces détachées
*********************

Le panneau de gestion des pièces détachées permet d'indiquer des stocks de pièces réutilisables avec d'autres pompes.


1. Consulter :
--------------

Ce sous-panneau permet la consultation, l'édition et la suppression des stocks de pièces détachées.
L'édition et la suppression des différents stocks sont possibles.

Pour effectuer ces actions, différentes icônes sont présentes : 

+ Icône *page avec crayon* : permet l'édition complète du stock.
+ Icône *poubelle* : permet la suppression d'un stock.

2. Créer Stock :
-----------------

Ce formulaire de création permet d'ajouter une nouvelle pièce détachées.

> Seul le champ de saisie **informations complémentaires** n'est pas obligatoire.



Menu Kits maintenance
*********************

Les kits de réparation et de maintenance des pompes sont disposés dans ce panneau de gestion. 

1. Consulter :
--------------

Ce sous-panneau permet de consulter les stocks disponibles de kit de réparations pour les pompes.
Des informations sur le kit et à quel type de famille de pompe il est utilisable sont présentes.
L'édition et la suppression des différents kits sont possibles.

Pour effectuer ces actions, différentes icônes sont présentes : 

+ Icône *page avec crayon* : permet l'édition complète du kit.
+ Icône *poubelle* : permet la suppression d'un kit.

2. Créer Stock :
----------------

Ce formulaire de création permet d'ajouter un nouveau kit.

Voici les informations obligatoires pour un nouvel ajout : 

+ Nom
+ Un fabriquant

> Il est possible d'ajouter une référence *vide* d'un kit.


Menu Huiles
***********

La gestion des huiles pour pompe se font par ce panneau. Il y a également la possibilité d'éditer un stocks ou de le supprimer.

1. Consulter :
--------------

Ce sous-panneau permet de consulter les stocks disponibles d'huiles et leur emplacement au niveau des pièces.
Des informations complémentaires sur la mise à jour du stocks ou le cas d'utilisation de l'huile peuvent y figurer.
L'édition et la suppression des différents stocks sont possibles.

Pour effectuer ces actions, différentes icônes sont présentes : 

+ Icône *page avec crayon* : permet l'édition complète du stock d'huile.
+ Icône *poubelle* : permet la suppression d'un stock.

2. Créer Stock :
----------------

Ce formulaire de création permet d'ajouter un nouveau stock d'huile.

Voici les informations obligatoires pour un nouvel ajout : 

+ Nom
+ Un fabriquant
+ Une pièce

> Il est possible d'ajouter une référence *vide* d'un stock d'huile.


Menu Documentations
*******************

Les documentations technique des accessoires et des pompes figurent dans ce panneau de gestion. 

1. Consulter :
--------------

Ce sous-panneau permet la consultation, le téléchargement, l'édition et la suppression des différentes documentations techniques de fabriquant.
Pour effectuer ces actions, différentes icônes sont présentes : 

+ Icône *flèche vers le bas dans un carré* : Permet de télécharger une copie de la documentation en PDF sur votre pc.
+ Icône *page avec crayon* : permet l'édition complète de la documentation.
+ Icône *poubelle* : permet la suppression d'une documentation.

2. Créer Manuel :
-----------------

Ce formulaire permet de créer une nouvelle documentation technique.

> Le champs de saisie "Version de la doc technique" est le seul élément non obligatoire.


Menu Administration
*******************

1. Dashboard :
--------------

La dashboard est une récapitulatif généralisées sous forme de compteurs, des pompes en stocks référencées avec leur état actuel, leur localisation générale, leur rattachement aux équipes et également le type présent. 

> D'autres possibilités de compteurs sont envisageable, ce panneau est modulable mais demande l'intervention d'un développeur. 

2. Modèles de Pompes :
----------------------

Dans ce sous-panneau, vous pouvez créer, éditer et consulter les modèles de pompes suivant les fabriquants. Un modèle de pompe permet de définir des stocks de pompe qui y sont relatifs.

Egalement, vous pouvez effectuer la gestion des technologies du vide inhérente à ces modèles de pompes.

> Pour créer un modèle de pompe, il faut obligatoirement un **technologie** associée !

La technologie de pompe ne demande que l'information suivante obligatoire : 

+ type de technologie

Pour un modèle de pompe, voici les informations obligatoires : 

+ Nom du modèle : Cela peut être un code parfois comme *1005 SD* pour la série *Pascal* de chez *Pfeiffer Vacuum*
+ Série ou famille de pompe
+ Une technologie de vide
+ Un fabriquant


3. Fabriquants :
----------------

Dans ce sous-panneau, vous pourrez créer et manager les fabriquants dont les stocks de pompes et accessoires sont relatés.

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

+ Consultation des lieux enregistrés
+ Création d'un lieu via un formulaire dédié présent sur le panneau de gestion.
+ Edition d'un lieu via l'icône *feuille et stylo*
+ Suppression d'un lieu via l'icône *poubelle*

Cela concerne les niveaux suivant de lieux : 

> Sites, 
    |_____Bâtiments, 
            |_______Etages, 
                        |____Pièces.

> Ces lieux sont obligatoires à établir avant de créer tous **stocks quelconques** comme une **équipe** !
