# Projet VISIOPOMPE

Visiopompe est un mini projet développé sous python.

Ce projet à pour but de centraliser et de mettre en place un systeme de gestion d'un parc de matériels mécaniques de type
pompes avec technologies de vide (pompes à membranes, pompes à palettes, à vis etc...) au sein d'un laboratoire par exemple.
Le listing des pompes peut se faire sur plusieurs niveaux de localisations ( Site -> emplacements dans une pièce) avec
tous les détails techniques et historique de la vie de l'appareillage.

Ce systeme inclut également la gestion d'équipements de maintenance: pièces détachées, kit de maintenances, huiles et documentations
lié au fonctionnement de ces appareillages.

## Spécification :

- Langage : Python 3.10
- Framework front-end : W3.css 
- Framework back-end : Django

## Avant propos

L'application est testé et en production sur un serveur **DEBIAN 11** avec une configuration **Apache 2** + module **WSGI**.

La version de python utilisée est la version **3.10**.

La base de données utilisée est **MariaDB**.

## Installation du projet

- Télécharger les sources du projet dans le dossier /var/html/www par example:  
<code> git clone http....</code>
- Télécharger et installez un environnement virtuel:
<code> sudo apt install python3-venv</code>
- Créez un nouveau 'virtualenv' dédié au projet visiopompe :
<code> python3 -m venv /chemin/vers/visiopompe</code>
- Activez le virtualenv :
source chemin/vers/visiopompe/bin/activate

- Installez les dépendances Python tierces, décrites dans le fichier "requierements-prod.txt"
du projet, dans ce nouveau virtualenv, à l'aide du logiciel 'pip' fourni dans ce virtualenv:

<code> pip install -r chemin/vers/visiopompe/requirements-prod.txt</code>

Note : des dépendances additionnelles listées dans "requirements-dev.txt" sont disponible sur la branche v1.2 si vous voulez forker le projet.

- Créer un fichier **.env** basé sur le fichier _.env-example_ et placez le à racine du projet :

Structure du fichier:

[ ] clef secrète à générer : https://codinggear.blog/django-generate-secret-key

> 
    SECRET_KEY = **Introduisez une clé secrète** 
    DJANGO_DEBUG = False
    ALLOWED_HOSTS = **mettre l'adresse IP/nom du serveur**

- Paramétrez l’accès à base de données via le fichier "setting.py" contenu dans le dossier "/src/config".
Pour cela il est nécessaire de modifier la configuration de la base de données si vous ne souhaitez pas utiliser
la base de données par défault : SQLite.
Note : les dépendances fournis inclus les librairies pour MySql/MariaDB.

Par défaut la configuration est la suivante:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

Vous pourrez la modifier et la configurer comme suit, par exemple pour MariaDB:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysqlsql',
        'NAME': 'my_database',
        'USER': 'my_database_user',
        'PASSWORD': 'my_password',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```


## Paramétrage d'Apache 2 + module wsgi

Succintement : 

- `sudo apt-get install libapache2-mod-wsgi-py3`
- `cd /etc/apache2/sites-available/` 
puis créer un fichier "visiopompe.conf"

- Structure du fichier 'visiopompe.conf' : 
https://docs.djangoproject.com/fr/4.2/howto/deployment/wsgi/modwsgi/


- `sudo systemctl restart apache2` 
Puis donner les droits d'accès en écriture et en lecture à Apache sur le dossier static et média :
- `chmod 755 /chemin/vers/dossier/visiopompe/media`
- `chmod 644 /chemin/vers/fichier/visiopompe.conf`
- `chown -R www-data:www-data /chemin/vers/dossier/visiopompe/media`
- `systemctl restart apache2`

### Configuration supplémentaire

[ HTML ]
Changez dans le fichier HTML "pompe/templates/navbar.html",  
l'adresse mail du support et indiquez celui de l'administrateur en charge du projet.

[ ADMIN ]
Si vous souhaitez faire un import massif ou un export . il existe cette option dans la partie administration du site.
L'import/export est possible pour les fiches suivantes :
- "modèles de pompes","stocks"
- "huiles","pièces détachées","documentations techniques"
- "tutelles","les codes inventaires"
- "les équipes","les fabriquants de pompes"
- "sites", "bâtiments", "étages", "pièces"

Pour accéder à la partie administration, faite la commande suivante:

`python manage.py createsuperuser`

Entrez un login puis un mot de passe. /!\ Le mot de passe n'est pas visible.

Vous pouvez accéder à l'administration de la sorte :

`adresse_du_site_web/admin  (ex : http://localhost/admin)`

Il faut ensuite aller dans l'onglet "ModelePompe" par exemple puis cliquer sur les boutons correspondant.
Il est conseillé d'importer au format CSV.

[ DIVERS ]
Le dossier "documentations" contient la documentation de l'application sous forme de site web standalone :
- Tutoriel rapide utilisateur
- documentation complète utilisateur
- documentation developpeur.

Vous pouvez la rendre accessible depuis votre serveur en modifiant votre fichier _.conf_ d'Apache et en créant un lien url supplémentaire dans le menu de l'application par exemple.

## Démarrage

Lorsque le site web est en place ainsi que l'accès établit, il convient de créer un compte "sysadmin" qui aura accès
en cas de problème au schéma complet des élements affichés dans le site web.
>
    pour le créer voir plus haut : rubrique >[ADMIN]

Il pourra également supprimer massivement ou importer massivement dans la base de données, les fiches ou stocks de
parc de pompes ou les autres éléments necessaires au fonctionnement de l'application.

/!\ Pour débuter, commencez par remplir dans l'ordre suivant les différentes rubriques **AVANT** de compléter un modèle de
pompe et un stock.

1. [Menu] Administration > Lieux
    2. Sites
    3. Bâtiments
    4. Etages
    5. Pièces
6. [Menu] Administration > Fabriquants
7. [Menu] Administration > Modèles des pompes
    8. Technologie de vide
    9. Fiches de pompe
10. [Menu] Pompes > Créer un stock


/!\ Un stock a besoin pour être créé, à minima, de ces informations ci dessus.

Il est rudement conseillé de compléter les autres élements pour un meilleur suivi de vos appareils.
> Se référer à la documentation utilisateur pour plus de détail.

Par la suite, la navigation au sein du site web se fait grâce au menu à gauche.

## BONUS DASHBOARD

****[Nécessite de l'aide d'un développeur]****
L'application propose d'avoir la possibilité de voir un menu _dashboard_ qui représente des compteurs des stocks, accessoires et pompes présentes.

Le format qui est proposé était prévu pour une utilisation standard.
<details><summary>
Cliquer pour en savoir plus...
</summary>


Si vous souhaitez agrémenter la dashboard en fonction de vos besoins par exemple des stocks de pompes par étages, batiments, un site,
vous devez pour cela modifier le fichier suivant : 

-  dashboard.html situé dans ".src/pompe/templates/pompe".
-  views.py situé dans ".src/pompe".

### views.py
> ligne  28 : ajoutez ces codes en fonction des besoins. Ce sont des exemples non exaustif.

- Encart pour les sites :
`variable = dash_pompes.filter(etage__batiment__site='x').count()`
x = valeur en base de données en référence à l'id du site en BDD.

- Encart pour les batiments:
`variable = dash_pompes.filter(etage__batiment='x').count()`
x = valeur en base de données en référence à l'id du batiment en BDD.

- Encart pour les étages:
`variable = dash_pompes.filter(etage='x').count()`
x = valeur en base de données en référence à l'id de l'étage en BDD.

- Encart pour les pièces:
`variable = dash_pompes.filter(piece='x').count()`
x = valeur en base de données en référence à l'id de la pièce en BDD.

- Encart par équipes :
`variable = dash_pompes.filter(equipe='x').count()`
x = valeur en base de données en référence à l'id de l'équipe' en BDD ou une référence à une équipe particulière.
(ex : equipe__sigle__icontains='nom_d_equipe)

Pour une valeur autre via le nom ou le sigle pour l'équipe, 
-> utiliser le parametre "icontains" qui _case-insensitive_. 
Plus d'infos voir la documentation django.

- Encart par fabriquants :
`var = dash_pompes.filter(pompe__fabriquant='x').count()`

- Encart par pompes et technologie associée :
 `var = dash_pompes.filter(pompe__technologie='x').count()`
x = valeur en base de données en référence à la technologie créée.

etc....

Lorsque vous avez créé une variable et un filtre, il faut l'ajouter à la variable "context" pour la déclarer
et l'utiliser dans le template "dashboard.html".
par exemple : 
```
context = {

    ..code précédent.. 
    'votre_variable': votre variable
}
```

### dashboard.html

La dashboard fonctionne sous un systeme de _container_ divisé en 4 parties.
Pour créer un block de 4 nouveaux encarts, il faut copier ce code à la suite entre une balise
```
<div class="w3-col m3 s3">** autre code**

                    <div class="w3-card-2 w3-center w3-text-blue-gray">
                        <header class="w3-container w3-pale-blue">
                            <h4>**TITRE DE L'ENCART**</h4>
                        </header>
                        <div class="w3-container w3-xlarge">
                            <p><strong>{{**VARIABLE DANS views.py/context**}}</strong></p>
                        </div>
                    </div>
</div>                    
```

La dashboard est un élement modulable. A vous de voir si vous souhaitez ou non l'agrémenter.
Pour plus d'informations sur les couleurs disponible à mettre dans la balise <header> à l'emplacement
`<header class="w3-couleur"></header>`
 
Allez sur ce site : https://www.w3schools.com/w3css/w3css_colors.asp
</details>

## Changelog

**Dernière version stable :** V.1.2

V1.2 - 2023/07/25
- Ajout de recherches filtrées sur les parties accessoires (pièces détachées, huiles, kits de maintenances)
- Ajout de messages d'erreurs, succès, informations
- Documentations technique, utilisateur et tutoriel utilisateur
- Bouton d'exportation des numéros d'inventaires et tutelles budgétaires.

V1.1 - 2023/07/15
- Filtre par bâtiment dans le menu de recherche des stocks de pompes. 
- Suppression automatique des documents et images lors de l'update ou suppression sur le serveur.
- Refactoring affichage MODELE POMPE, des Fabriquants, des équipes, des lieux. 
- Refactoring des formulaires.
- Amélioration du stockage des images sur serveur par date.
- Redimensionnage des images.
- Refactoring  des noms de tables de la base de données : convention de nommage appliquée.

V1.0 - 2022/
VO - 2021/11

## Features possible

- HTML : Ajouter un bouton "duplication" pour dupliquer un objet en base de données => gain de temps users
- SESSION : Création de compte utilisateurs type "equipe" pour les droits sur l'application.
- Version mobile de l'application
- Dockerisation de l'application


## Auteurs

Nicolas Renard _ (nicolas.renard[arobase]univ-brest.fr)

*!* L'auteur remercie chaleureusement V.Férotin (http://vincent-ferotin.info/) pour ses conseils avisés.


## License

Ce projet est sous licence MIT -  pour plus d'informations






