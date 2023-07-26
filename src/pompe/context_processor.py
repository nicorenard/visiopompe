"""
Fonctions de contexte personnalisée ajouté au processeur de Django pour affichage dans les Gabarits.
"""
from .models import VersionApp

# https://stackoverflow.com/questions/72977293/how-to-show-list-of-categories-in-navbar-using-django-framework?rq=3
def version_app(request):
    """
    Fonction d'affichage de la version de l'application en cours.
    Args:
        request: la requête d'affichage de la version de l'application

    Returns:
        version: la version de l'application en cours.
    """
    return {
        "versions": VersionApp.objects.all()
    }