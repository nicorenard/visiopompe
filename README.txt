#### VISIOPOMPE PROJECT #####


[![forthebadge][![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)


Visiopompe est un mini projet développé via python avec le Framework django.
Ce projet à pour but de centraliser et de mettre en place un systeme de gestion d'un parc de matériel mécanique de type
pompes à membranes et pompes à palettes au sein d'un laboratoire.
Le listing des pompes peut se faire sur plusieurs niveaux de localisations ( Site -> emplacements dans une pièce) avec
tous les détails techniques et historique  de la vie de l'appareillage.
Ce systeme inclut également la gestion d'équipements de maintenance, de pièces détachées, d'huiles et la documentation
lié au fonctionnement de ces appareillages.

## Pour commencer

### Pré-requis

- Le projet est developpé pour fonctionner avec un serveur linux avec un accès internet.
>>>> Le serveur de production test est sous : debian 11 avec une base de donnée de type MySQl.
- Configurez ensuite le serveur pour recevoir python 3.9.
- Puis installez avant de commencer un environnement virtuel qui contiendra les dépendances de l'application.

>>>>> sudo apt-get install python3-virtualenv

- Installez les dépendances contenus dans le fichier "requierement.txt" contenu dans le dossier source "src"

>>>>> pip install -r requirements.txt

- Créer un fichier .env et palcez le dans le dossier "src" avant de l'uploader sur votre serveur :
>>>>> Structure du fichier.:

    SECRET_KEY = **Introduisez une clé secrète**
    DJANGO_DEBUG = False
    ALLOWED_HOSTS = **mettre l'adresse IP**

- Paramétrez l’accès à base de données via le fichier "setting.py" contenu dans ""/src/visiopompe".
Pour cela il est nécessaire de modifier la configuration de la base de données si vous ne souhaitez pas
la base de données par défault : SQLlite.

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

-Changez dans le fichier HTML : "pompe/templates/navbar.html" l'adresse mail du support et indiquez celui de
l'administrateur en charge du projet.

- Si vous souhaitez faire un import massif ou un export des fiches "pompes" ou "stocks", un compte administrateur est
nécessaire.

Pour le créer faite :

>>> python manage.py createsuperuser

Entrez un login puis un mot de passe. /!\ Le mot de passe n'est pas visible.

Vous pouvez accéder à l'administration en faisant :

>>> adresse_du_site_web/admin  (ex : http://localhost/admin)

Il faut ensuite aller dans l'onglet "ModelePompe" puis cliquez sur les boutons correspondant.
l'import se fait via le template délivré dans le dossier "importation"
Ce fichier n'est pas à laisser sur votre serveur.

- Le dossier "documentations" est informatif et concernera plus un dev.
Il ne doit pas être laissé sur le serveur de production (inutile).

- Cas de la Dashboard. [Nécessite de l'aide d'un dev si besoin]
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
Encart par fabriquant :
>>>>

La dashboard est un élement modulable. A vous de voir si vous osuhaitez ou non l'agrémenter.


## Démarrage

Lorsque le site web est en place ainsi que l'accès établit. Il convient de créer un superuser qui aura
accès en cas de problème au schéma complet des élements affichés dans le site web.
Il pourra également supprimer massivement ou importer massivement dans la base de données, les fiches ou stocks de
parc de pompes ou les autres éléments necessaires au fonctionnement de l'application.

Par la suite, la navigation au sein du site web se fait grâce au menu à gauche.

Il est également recommandé de créer un compte user pour avoir accès à la dashboard et aux fonctions d'ajouts.
L'application est sans compte accessible en lecture seule (= consultation, recherche mais pas d'ajout/modification).


## Projet fabriqué avec

* [Python 3] - langage de programmation
* [W3.css] - Framework front-end
* [Django] - Framework Back-end
* [Pycharm]- IDE

## Versions

**Dernière version stable :** V.0.1



## Auteurs

* Nicolas Renard _ [nicolas.renard[arobase]univ-brest.fr)


## License

Ce projet est sous licence ```` -  pour plus d'informations






