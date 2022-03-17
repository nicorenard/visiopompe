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
- Configurez le serveur pour recevoir python 3.9.
- Installez avant de commencer un environnement virtuel:

>>>>> sudo apt install python3-venv
>>>>> # Créez un nouveau 'virtualenv' dédié au projet visiopompe dans
>>>>> # eg. /opt/local/virtualenvs/visiopompe
>>>>> sudo mkdir -p /opt/local/virtualenvs/
>>>>> python3 -m venv /opt/local/virtualenvs/visiopompe

- Installez les dépendances Python tierces, décrites dans le fichier "requirements.txt"
  du projet, dans ce nouveau virtualenv, à l'aide du logiciel 'pip' fourni dans ce virtualenv:

>>>>> /opt/local/virtualenvs/visiopompe/bin/pip install -r path/to/visiopompe/requirements.txt
>>>>> # NB: Si vous développez sous Windows, vous pourriez également avoir besoin
>>>>> # des dépendances additionnelles listées dans "requirements-win32.txt"!

- Placez les sources Python du projet 'visiopompe' dans un répertoire dédié,
  par ex. /opt/local/visiopompe/0.1:

>>>>> sudo mkdir -p /opt/local/visiopompe/0.1
>>>>> sudo cp -R path/to/visiopompe/src/* /opt/local/visiopompe/0.1/

Vous pouvez maintenant créer un nouveau "projet" 'visiopompe', une nouvelle instance,
avec ses propres configuration, base de données, fichiers uploadés, etc.!

- Créer un fichier .env et placez le dans le dossier "src" avant de l'uploader sur votre serveur :
>>>>> Structure du fichier.:

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

- Cas de la Dashboard. [Nécessite de l'aide d'un dev **Evaluez selon votre besoin**]
L'application propose aux administrateurs locaux d'avoir la possibilité de voir un menu dashboard
qui reprend les informations de suivis des stocks, accesoires et pompes présents.
La format qui est proposé en prévu pour une utilisation "standard".
Si vous souhaitez agrémenter la dashboard en fonction par exemple des stocks de pompes par étages, batiment, un site
Vous devez pour cela modifier le fichier suivant : dashboard.html situé dans ".src/pompe/templates/pompe".
Voici les codes pour rajouter en fonction des étages et qu'il faut rajouter si vous avez plusieurs étages.
>>>>
Encart pour les sites :
>>>>
Encart pour les batiments:
>>>>
Encart pour les étages:
>>>>
Encart pour les pièces:
>>>>
Encart par équipes :
>>>>
Encart par fabriquants :
>>>>

La dashboard est un élement modulable. A vous de voir si vous souhaitez ou non l'agrémenter.

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

Lorsque le site web est en place ainsi que l'accès établit.
Il convient de créer un compte sysadmin qui aura accès en cas de problème au schéma complet des élements affichés
dans le site web. (pour le créer voir plus haut : rubrique >>[ADMIN]
Il pourra également supprimer massivement ou importer massivement dans la base de données, les fiches ou stocks de
parc de pompes ou les autres éléments necessaires au fonctionnement de l'application.

Par la suite, la navigation au sein du site web se fait grâce au menu à gauche.

Il est également recommandé de créer un compte user pour avoir accès à la dashboard et aux fonctions d'ajouts.
L'application est sans compte accessible en lecture seule (= consultation, recherche mais pas d'ajout/modification).

## Projet fabriqué avec :

* [Python 3] - [W3.css] - [Django] - [Pycharm]

## Changelog


**Dernière version stable :** V.1.0

VO - 2021/11

## Features

>> BDD : Ajouter une ou des tables "images" pour éviter les redondances d'images pour les duplications de stocks, accessoires,
kits etc... => optimisation de la place mémoire.
>> HTML : Ajouter un bouton "duplication" pour dupliquer un objet en base de données => gain de temps users
>> HTML : Modifier le formulaire pour ajouter des stocks pas qu'avec des pieces mais également, un site/batiment.


## Auteurs

* Nicolas Renard _ (nicolas.renard[arobase]univ-brest.fr)
*!* L'auteur remercie chaleureusement V.Férotin (http://vincent-ferotin.info/) pour ses conseils avisés.


## License

Ce projet est sous licence ```` -  pour plus d'informations






