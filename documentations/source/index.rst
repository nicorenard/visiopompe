.. visiopompe documentation master file, created by
   sphinx-quickstart on Mon Jun 19 15:34:58 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Bienvenue sur la documentation de Visiopompe.
#############################################

Introduction
************
``Visiopompe`` est un mini projet développé via python 3 avec le Framework ``Django``.
Ce projet à pour but de centraliser et de mettre en place un systeme de gestion d'un parc de matériel mécanique de type
pompes à membranes et pompes à palettes au sein d'un laboratoire.

Le listing des **pompes** peut se faire sur plusieurs niveaux de localisation.

( Site -> Batiment -> Etage -> Pièce -> emplacements dans une pièce) avec
tous les détails techniques et historique de la vie de l'appareillage.

Gestion Bonus
=============
Ce systeme inclut également la gestion d'équipements de maintenance lié au fonctionnement de ces appareillages:
 - pièces détachées,
 - huiles,
 - documentations fabriquants.


Sommaire
========

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. toctree::
   :maxdepth: 2
   :numbered:
   :caption: Menu:

   tutoriel
   users
   modules