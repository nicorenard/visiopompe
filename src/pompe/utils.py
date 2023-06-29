"""
Fonctions utilitaires pour le module pompe
"""

import os
from datetime import datetime


def get_upload_path(instance, filename, directory):
    """
    Fonction pour récupérer le chemin réel d'un répertoire de téléversement créé avec la date du jour.
    Args:
        instance: l'instance de répertoire à créer en fonction de la table de la base de donnée
        filename: le nom du fichier
        directory: le repertoire
    """
    current_date = datetime.now()
    # formatage de la date au format 'YYMMDD'
    formatted_date = current_date.strftime('%y%m%d')
    return os.path.join(directory,formatted_date,filename)


def upload_to_pompe(instance, filename):
    """
    Fonction de création du dossier pour la table POMPE

    Args:
        instance: l'objet image à ajouter
        filename: le nom de l'objet

    Returns:
        le nouveau chemin avec le dossier créé
    """
    return get_upload_path(instance,filename,'pompe_img')


def upload_to_piecepompe(instance, filename):
    """
    Fonction de création du dossier pour la table PIECE

    Args:
        instance: l'objet image à ajouter
        filename: le nom de l'objet

    Returns:
        le nouveau chemin avec le dossier créé
    """
    return get_upload_path(instance, filename, 'piecepompe_img')


def upload_to_logoFabriquant(instance, filename):
    """
    Fonction de création du dossier logo pour la table FABRIQUANT

    Args:
        instance: l'objet image à ajouter
        filename: le nom de l'objet

    Returns:
        le nouveau chemin avec le dossier créé
    """
    return get_upload_path(instance, filename, 'logo_fabriquant')


def upload_to_logoMiniFabriquant(instance, filename):
    """
    Fonction de création du dossier logo miniature pour la table FABRIQUANT

    Args:
        instance: l'objet image à ajouter
        filename: le nom de l'objet

    Returns:
        le nouveau chemin avec le dossier créé
    """
    return get_upload_path(instance, filename, 'logo_fabriquant/miniature')


def upload_to_kit(instance, filename):
    """
    Fonction de création du dossier logo miniature pour la table KIT

    Args:
        instance: l'objet image à ajouter
        filename: le nom de l'objet

    Returns:
        le nouveau chemin avec le dossier créé
    """
    return get_upload_path(instance, filename, 'kit_img')


def upload_to_huile(instance, filename):
    """
    Fonction de création du dossier logo miniature pour la table HUILE

    Args:
        instance: l'objet image à ajouter
        filename: le nom de l'objet

    Returns:
        le nouveau chemin avec le dossier créé
    """
    return get_upload_path(instance, filename, 'huile_img')


def upload_to_documentation(instance, filename):
    """
    Fonction de création du dossier logo miniature pour la table DOC

    Args:
        instance: l'objet image à ajouter
        filename: le nom de l'objet

    Returns:
        le nouveau chemin avec le dossier créé
    """
    return get_upload_path(instance, filename, 'manuel')