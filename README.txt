# VISIOPOMPE
_(juste en dessous des badges sympatiques à placer)_

[![forthebadge][![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)


Visiopompe est un mini projet développé via python avec le Framework django.
Ce projet à pour but de centraliser et de mettre en place une gestion d'un parc de matériel de type pompes à membranes
et pompes à palettes au sein d'un laboratoire.
Le listing des pompes peut se faire sur plusieurs niveaux de localisations avec tous les détails techniques et historique
 de la vie de l'appareillage. Ce mini projet inclu également la gestion
des équipements de maintenance, de pièces détachées, d'huiles et la documentation pour le fonctionnement de ces appreillages.

## Pour commencer

### Pré-requis

- Installer un serveur linux avec un accès internet (prod testée : debian 11).
- Configurez le serveur pour recevoir python 3.9.
- Installez avant de commencer un environnement virtuel
>>>>> sudo apt-get install python3-virtualenv
- Installez les dépendances contenus dans le fichier "requierement.txt" contenu dans le dossier src
>>>>> pip install -r requirements.txt
- Créer un fichier .env avec cette structure dans /src avant de l'uploader sur votre serveur :
    SECRET_KEY = **Introduisez une clé secrète**
    DJANGO_DEBUG = False
    ALLOWED_HOSTS = **mettre l'adresse IP**
- Paramétrez l’accès à base de données via le fichier "setting.py" contenu dans /src/visiopompe.
Pour cela il est nécessaire de modifier la configuration de la base de donnée.
Par défaut la configuration est la suivante:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

Vous pourrez modifier et la configurer comme suit, par exemple pour PostgreSQL:

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

Note : le serveur de production de test a été utilisé avec MySQL.

### Installation

-Changez dans le fichier HTML : "pompe/templates/index.html" l'adresse mail du support et indiquez celui de l'administrateur en charge
du projet.

Ensuite vous pouvez montrer ce que vous obtenez au final...
- Si vous souhaitez faire un import massif ou un export de votre fichier pompe, un compte administrateur est necessaire.
Pour le créer faite :
>>> python manage.py createsuperuser
Entrez un login puis un mot de passe.
/!\ Le mot de passe n'est pas visible.
vous pouvez accéder à l'administration en faisant :
>>> adresse_du_site_web/pompe/admin
Il faut ensuite aller dans l'onglet "pompess" puis cliquez sur les boutons correspondant.
l'import se fait via le template délivrée dans le dossier "import_template_xlsx"
Ce dossier est a supprimer dès que vous avez récupérer le template.

## Démarrage

Lorsque le site web est en place ainsi que l'accès établit. Il convient de créer un superuser qui aura
accès en cas de problème au schéma complet des élements affichés dans le site web.
Il pourra également supprimer massivement ou importer massivement dans la base de données, les parc de pompes.

Par la suite, la navigation au sein du site web se fait grâce au menu.


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






