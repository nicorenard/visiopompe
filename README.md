#### VISIOPOMPE PROJECT #####

Visiopompe est un mini projet développé via python 3 avec le Framework django.
Ce projet à pour but de centraliser et de mettre en place un systeme de gestion d'un parc de matériel mécanique de type
pompes à membranes et pompes à palettes au sein d'un laboratoire.
Le listing des pompes peut se faire sur plusieurs niveaux de localisations ( Site -> emplacements dans une pièce) avec
tous les détails techniques et historique de la vie de l'appareillage.
Ce systeme inclut également la gestion d'équipements de maintenance: pièces détachées, huiles et documentations
lié au fonctionnement de ces appareillages.

## Pour commencer

### Pré-requis

- Installez un serveur linux avec un accès internet (prod testée : debian 11).
- Configurez le serveur pour recevoir python 3.10.
- Installez avant de commencer un environnement virtuel:

> sudo apt install python3-venv
- Créez un nouveau 'virtualenv' dédié au projet visiopompe dans
- eg. /opt/local/virtualenvs/visiopompe
> sudo mkdir -p /opt/local/virtualenvs/
> python3 -m venv /opt/local/virtualenvs/visiopompe

- Installez les dépendances Python tierces, décrites dans le fichier "requierements-prod.txt"
  du projet, dans ce nouveau virtualenv, à l'aide du logiciel 'pip' fourni dans ce virtualenv:

<code> /opt/local/virtualenvs/visiopompe/bin/pip install -r path/to/visiopompe/requirements-prod.txt</code>
# des dépendances additionnelles listées dans "requirements-dev.txt" si vous voulez participer au projet.

- Placez les sources Python du projet 'visiopompe' dans un répertoire dédié,
  par ex. /opt/local/visiopompe/v1.0:

> sudo mkdir -p /opt/local/visiopompe/v1.0
> sudo cp -R path/to/visiopompe/src/* /opt/local/visiopompe/v1.0/

Vous pouvez maintenant créer un nouveau "projet" 'visiopompe', une nouvelle instance,
avec ses propres configuration, base de données, fichiers uploadés, etc.!

- Créer un fichier .env basé sur le fochier .env-example et placez le dans le dossier racine du projet :

Structure du fichier:
>   clef_secrete : https://codinggear.blog/django-generate-secret-key
> 
    SECRET_KEY = **Introduisez une clé secrète** 
    DJANGO_DEBUG = False
    ALLOWED_HOSTS = **mettre l'adresse IP**

- Paramétrez l’accès à base de données via le fichier "setting.py" contenu dans "/src/config".
Pour cela il est nécessaire de modifier la configuration de la base de données si vous ne souhaitez pas
la base de données par défault : SQLite.

Par défaut la configuration est la suivante:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

Vous pourrez la modifier et la configurer comme suit, par exemple pour PostgreSQL:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydatabase',
        'USER': 'mydatabaseuser',
        'PASSWORD': 'mypassword',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

### Installation

[ HTML ]
-Changez dans le fichier HTML : "pompe/templates/navbar.html" l'adresse mail du support et indiquez celui de
l'administrateur en charge du projet.



[ ADMIN ]
- Si vous souhaitez faire un import massif ou un export . il existe cette option dans la partie administration du site.
L'import/export est possible pour les fiches suivantes :
--"modèles de pompes","stocks"
--"huiles","pièces détachées","documentations techniques"
--"tutelles","les codes inventaires"
--"les équipes","les fabriquants de pompes"
--"sites", "bâtiments", "étages", "pièces"

Pour accéder à la partie administration, faite la commande suivante:

>>> python manage.py createsuperuser

Entrez un login puis un mot de passe. /!\ Le mot de passe n'est pas visible.

Vous pouvez accéder à l'administration de la sorte :

>>> adresse_du_site_web/admin  (ex : http://localhost/admin)

Il faut ensuite aller dans l'onglet "ModelePompe" par exemple puis cliquer sur les boutons correspondant.
l'import se fait via le template délivré dans le dossier "importation".
Il est conseillé d'importer au format CSV.
Note : Ce fichier csv et le dossier "importation" ne sont pas à laisser sur votre serveur.

[ DIVERS ]
- Le dossier "documentations" est informatif et concernera un developpeur et sysadmin.
Il ne doit pas être laissé sur le serveur de production (inutile).

## Démarrage

Lorsque le site web est en place ainsi que l'accès établit, il convient de créer un compte "sysadmin" qui aura accès
en cas de problème au schéma complet des élements affichés dans le site web.
>>>>(pour le créer voir plus haut : rubrique >>[ADMIN]
Il pourra également supprimer massivement ou importer massivement dans la base de données, les fiches ou stocks de
parc de pompes ou les autres éléments necessaires au fonctionnement de l'application.

/!\ Pour débuter, commencez par remplir dans l'ordre suivant les différentes rubriques AVANT de compléter un modèle de
pompe et un stock.

1- [Menu] Administration / Lieux
1.1 - Sites
1.2 - Bâtiments
1.3 - Etages
1.4 - Pièces
2 - [Menu] Administration / Fabriquants
3 - [Menu] Administration / Modèles des pompes
3.1 - Technologie de pompe
3.2 - Fiches de pompe
4 - [Menu] Pompes / Créer un stock

/!\ Un stock a besoin pour être créé, à minima, de ces informations là.
Il est rudement conseillé de compléter les autres élements pour un meilleur suivi de vos machines.
Se référer à la documentation utilisateur pour plus de détail.


Par la suite, la navigation au sein du site web se fait grâce au menu à gauche.

[BONUS]
- Cas de la Dashboard.

****[Nécessite de l'aide d'un dev **Evaluez selon votre besoin**]****

L'application propose d'avoir la possibilité de voir un menu dashboard
qui reprend les informations de suivis des stocks, accessoires et pompes présentes.
Le format qui est proposé en prévu pour une utilisation "standard".
Si vous souhaitez agrémenter la dashboard en fonction de vos besoins par exemple des stocks de pompes par étages, batiments, un site,
vous devez pour cela modifier le fichier suivant : dashboard.html situé dans ".src/pompe/templates/pompe".
Vous devez aussi modifier le fichier de l'application : views.py.

# VIEW.py
>>ligne  28 : ajoutez ces codes en fonction des besoins

Encart pour les sites :
>>>>variable = dash_pompes.filter(etage__batiment__site='x').count()
x = valeur en base de données en référence à l'id du site en BDD.
Encart pour les batiments:
>>>> variable = dash_pompes.filter(etage__batiment='x').count()
x = valeur en base de données en référence à l'id du batiment en BDD.
Encart pour les étages:
>>>> variable = dash_pompes.filter(etage='x').count()
x = valeur en base de données en référence à l'id de l'étage en BDD.
Encart pour les pièces:
>>>> variable = dash_pompes.filter(piece='x').count()
x = valeur en base de données en référence à l'id de la pièce en BDD .
Encart par équipes :
>>>> variable = dash_pompes.filter(equipe='x').count()
x = valeur en base de données en référence à l'id de l'équipe' en BDD .
(ex : equipe__sigle__icontains='CEMCA')
Encart par fabriquants :
>>>> var = dash_pompes.filter(pompe__fabriquant='x').count()
Encart par pompes et technologie associée :
>>>> var = dash_pompes.filter(pompe__technologie='x').count()
x = valeur en base de données en référence à la technologie créée.

Pour une valeur autre via le nom ou le sigle pour l'équipe 
-> utiliser le parametre "icontains" qui case-insensitive. 
Plus d'infos voir la django doc.

Lorsque vous avez créé une variable et un filtre, il faut l'ajouter à la variable "context" pour la déclarer
et l'utiliser dans le template dashboard.html.
par exemple : 'variable_fabriquant':variable_fabriquant

# DASHBOARD.HTML

La dashboard fonctionne sous un systeme de container divisé en 4 parties.
Pour créer un block de 4 nouveaux encarts, il faut copier ce code à la suite entre une balise
<div class="w3-col m3 s3">**code**</div>

                    <div class="w3-card-2 w3-center w3-text-blue-gray">
                        <header class="w3-container w3-pale-blue">
                            <h4>**TITRE DE L'ENCART**</h4>
                        </header>
                        <div class="w3-container w3-xlarge">
                            <p><strong>{{**VARIABLE DANS view.py/context**}}</strong></p>
                        </div>
                    </div>

La dashboard est un élement modulable. A vous de voir si vous souhaitez ou non l'agrémenter.
Pour plus d'info sur les couleurs disponible à mettre dans la balise <header> à l'emplacement
>> <header class="w3-couleur"></header>
 Allez sur ce site : https://www.w3schools.com/w3css/w3css_colors.asp

## Projet fabriqué avec :

* [Python 3] - [W3.css] - [Django]

## Changelog


**Dernière version stable :** V.1.0

V1.0 - 2022/04
VO - 2021/11

## Features V1.2

>> BDD : Ajouter une ou des tables "images" pour éviter les redondances d'images pour les duplications de stocks, accessoires,
kits etc... => optimisation de la place mémoire.
>> HTML : Ajouter un bouton "duplication" pour dupliquer un objet en base de données => gain de temps users
>> SESSION : Création de compte utilisateurs type "equipe" pour les droits sur l'application.


## Auteurs

* Nicolas Renard _ (nicolas.renard[arobase]univ-brest.fr)
*!* L'auteur remercie chaleureusement V.Férotin (http://vincent-ferotin.info/) pour ses conseils avisés.


## License

Ce projet est sous licence [EN COURS] -  pour plus d'informations






