"""
Fonctions utilitaires pour le module pompe
"""

import os
from datetime import datetime
from django.core.files import File
from pathlib import Path
from PIL import Image
from io import BytesIO


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


# https://stackoverflow.com/questions/71918006/django-resize-image-before-saving
image_types = {
    "jpg": "JPEG",
    "jpeg": "JPEG",
    "png": "PNG",
    "gif": "GIF",
    "tif": "TIFF",
    "tiff": "TIFF",
}


def image_resize(image, width, height):
    """
    Fonction pour retailler les images importé dans le serveur.

    Args:
        image : le nom du fichier image téléversé
        width: la longueur du fichier image
        height: la hauteur du fichier image

    Returns:
          l'image retaillée avant sauvegarde
    """
    # Open the image using Pillow
    img = Image.open(image)
    # verification de la taille
    if img.width > width or img.height > height:
        output_size = (width, height)
        # Creation d'une image de type thumbail
        img.thumbnail(output_size)
        # Pour récupérer le path de l'image
        img_filename = Path(image.file.name).name
        # Pour récupérer l'extension
        img_suffix = Path(image.file.name).name.split(".")[-1]
        # Pour récupérer le format image_types dictionary
        img_format = image_types[img_suffix]
        # Sauvegarde de l'image retaillée dans le buffer et en fonction du format
        buffer = BytesIO()
        img.save(buffer, format=img_format)
        # Englobage de l'image dans un buffer
        file_object = File(buffer)
        # Sauvegarde en utilisant django-storages
        image.save(img_filename, file_object)
