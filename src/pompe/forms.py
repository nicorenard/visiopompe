"""
Forms of the project Visiopompe
"""
from django import forms
from .models import *


# stock pompes
class StockPompeform(forms.ModelForm):
    """
    Formulaire de création d'un stock de pompe.
    Args:
        ModelForm : l'attribut basé sur Form de Django

    Returns:
        Le formulaire généré pour créer un stock de pompe
    """

    class Meta:
        model = StockPompe
        fields = '__all__'
        widgets = {
            'pompe': forms.Select(attrs={'class': 'w3-input w3-round w3-border'}),
            'mise_en_service': forms.DateInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'etage': forms.Select(attrs={'class': 'w3-input w3-round w3-border'}),
            'piece': forms.Select(attrs={'class': 'w3-input w3-round w3-border'}),
            'place': forms.TextInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'vide_user': forms.NumberInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'num_serie': forms.TextInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'inventaire': forms.Select(attrs={'class': 'w3-input w3-round w3-border'}),
            'statut': forms.Select(attrs={'class': 'w3-input w3-round w3-border'}),
            'atex': forms.NullBooleanSelect(attrs={'class': 'w3-input w3-round w3-border'}),
            'huile': forms.Select(attrs={'class': 'w3-input w3-round w3-border'}),
            'equipe': forms.Select(attrs={'class': 'w3-input w3-round w3-border'}),
            'vidange': forms.DateInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'historique': forms.Textarea(attrs={'class': 'w3-input w3-round w3-border'}),

        }


class ModifStockPompeForm(forms.ModelForm):
    """
    Classe de modification d'un formulaire d'un stock de pompe.
    Args:
        ModelForm : l'attribut basé sur Form de Django

    Returns:
        Le formulaire avec les informations pré-remplies
    """

    class Meta:
        model = StockPompe
        exclude = ['mise_en_service']
        widgets = {
            'pompe': forms.Select(attrs={'class': 'w3-input w3-round w3-border'}),
            'etage': forms.Select(attrs={'class': 'w3-input w3-round w3-border'}),
            'piece': forms.Select(attrs={'class': 'w3-input w3-round w3-border'}),
            'place': forms.TextInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'vide_user': forms.NumberInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'num_serie': forms.TextInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'inventaire': forms.Select(attrs={'class': 'w3-input w3-round w3-border'}),
            'statut': forms.Select(attrs={'class': 'w3-input w3-round w3-border'}),
            'atex': forms.NullBooleanSelect(attrs={'class': 'w3-input w3-round w3-border'}),
            'huile': forms.Select(attrs={'class': 'w3-input w3-round w3-border'}),
            'equipe': forms.Select(attrs={'class': 'w3-input w3-round w3-border'}),
            'vidange': forms.DateInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'historique': forms.Textarea(attrs={'class': 'w3-input w3-round w3-border'}),

        }


class Inventaireform(forms.ModelForm):
    """
    Formulaire de création d'un numéro d'inventaire.
    Args:
        ModelForm : l'attribut basé sur Form de Django

    Returns:
        Le formulaire généré pour créer un numéro d'inventaire
    """

    class Meta:
        model = Inventaire
        fields = '__all__'
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'numero': forms.TextInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'date_inventaire': forms.DateInput(attrs={'class': 'w3-input w3-round w3-border'}),
        }


class ModifInventaireForm(forms.ModelForm):
    """
    Classe de modification d'un formulaire d'un numéro d'inventaire.
    Args:
        ModelForm : l'attribut basé sur Form de Django

    Returns:
        Le formulaire avec les informations pré-remplies
    """

    class Meta:
        model = Inventaire
        fields = '__all__'
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'numero': forms.TextInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'date_inventaire': forms.DateInput(attrs={'class': 'w3-input w3-round w3-border'}),
        }


class Tutelleform(forms.ModelForm):
    """
    Formulaire de création d'une tutelle budgétaire.
    Args:
        ModelForm : l'attribut basé sur Form de Django

    Returns:
        Le formulaire généré pour créer une tutelle budgétaire
    """

    class Meta:
        model = Tutelle
        fields = '__all__'
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'w3-input w3-round w3-border'}),
        }


class ModifTutelleForm(forms.ModelForm):
    """
    Classe de modification d'un formulaire d'une tutelle budgétaire.
    Args:
        ModelForm : l'attribut basé sur Form de Django

    Returns:
        Le formulaire avec les informations pré-remplies
    """

    class Meta:
        model = Tutelle
        fields = '__all__'
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'w3-input w3-round w3-border'}),
        }


# fiche pompes
class ModelPompeform(forms.ModelForm):
    """
    Formulaire de création d'un modèle de pompe.
    Args:
        ModelForm : l'attribut basé sur Form de Django

    Returns:
        Le formulaire généré pour créer un modèle
    """

    class Meta:
        model = ModelePompe
        fields = '__all__'
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'nom': forms.TextInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'modele': forms.TextInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'phasage': forms.Select(attrs={'class': 'w3-input w3-round w3-border'}),
            'puissance': forms.Select(attrs={'class': 'w3-input w3-round w3-border'}),
            'technologie': forms.Select(attrs={'class': 'w3-input w3-round w3-border'}),
            'vide_theo': forms.NumberInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'fabriquant': forms.Select(attrs={'class': 'w3-input w3-round w3-border'}),
            'documentation': forms.Select(attrs={'class': 'w3-input w3-round w3-border'}),
        }


class ModifModelPompeForm(forms.ModelForm):
    """
    Classe de modification d'un modèle de pompe.
    Args:
        ModelForm : l'attribut basé sur Form de Django

    Returns:
        Le formulaire avec les informations pré-remplies
    """

    class Meta:
        model = ModelePompe
        fields = '__all__'
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'nom': forms.TextInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'modele': forms.TextInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'phasage': forms.Select(attrs={'class': 'w3-input w3-round w3-border'}),
            'puissance': forms.Select(attrs={'class': 'w3-input w3-round w3-border'}),
            'technologie': forms.Select(attrs={'class': 'w3-input w3-round w3-border'}),
            'vide_theo': forms.NumberInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'fabriquant': forms.Select(attrs={'class': 'w3-input w3-round w3-border'}),
            'documentation': forms.Select(attrs={'class': 'w3-input w3-round w3-border'}),
        }


class Technologieform(forms.ModelForm):
    """
    Formulaire de création d'une technologie du vide.
    Args:
        ModelForm : l'attribut basé sur Form de Django

    Returns:
        Le formulaire généré pour créer une technologie
    """

    class Meta:
        model = TechnologiePompe
        fields = '__all__'
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'info': forms.TextInput(attrs={'class': 'w3-input w3-round w3-border'}),
        }


class ModifTechnoForm(forms.ModelForm):
    """
    Classe de modification d'un formulaire d'une technologie du vide.
    Args:
        ModelForm : l'attribut basé sur Form de Django

    Returns:
        Le formulaire avec les informations pré-remplies
    """

    class Meta:
        model = TechnologiePompe
        fields = '__all__'
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'info': forms.TextInput(attrs={'class': 'w3-input w3-round w3-border'}),
        }


# documentations
class Docform(forms.ModelForm):
    """
    Formulaire de création d'une documentation technique.
    Args:
        ModelForm : l'attribut basé sur Form de Django

    Returns:
        Le formulaire généré pour créer une documentation
    """

    class Meta:
        model = Document
        fields = '__all__'
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'fabriquant': forms.Select(attrs={'class': 'w3-input w3-round w3-border'}),
            'manuel': forms.ClearableFileInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'version': forms.TextInput(attrs={'class': 'w3-input w3-round w3-border'}),
        }


class ModifDocForm(forms.ModelForm):
    """
    Classe de modification d'un formulaire d'une documentation technique.
    Args:
        ModelForm : l'attribut basé sur Form de Django

    Returns:
          Le formulaire avec les informations pré-remplies
    """

    class Meta:
        model = Document
        fields = '__all__'
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'fabriquant': forms.Select(attrs={'class': 'w3-input w3-round w3-border'}),
            'manuel': forms.ClearableFileInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'version': forms.TextInput(attrs={'class': 'w3-input w3-round w3-border'}),
        }


# pieces detachées
class PiecePompeform(forms.ModelForm):
    """
       Formulaire de création d'une pièce détaché.
       Args:
           ModelForm : l'attribut basé sur Form de Django

       Returns:
           Le formulaire généré pour créer une pièce détachée
       """

    class Meta:
        model = PiecesPompe
        fields = '__all__'
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'nom': forms.TextInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'date_maj': forms.DateInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'fabriquant': forms.Select(attrs={'class': 'w3-input w3-round w3-border'}),
            'piece': forms.Select(attrs={'class': 'w3-input w3-round w3-border'}),
            'quantite': forms.NumberInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'information': forms.TextInput(attrs={'class': 'w3-input w3-round w3-border'}),
        }


class ModifPiecePompeForm(forms.ModelForm):
    """
    Classe de modification d'un formulaire d'une documentation technique.
    Args:
        ModelForm : l'attribut basé sur Form de Django

    Returns:
          Le formulaire avec les informations pré-remplies
    """

    class Meta:
        model = PiecesPompe
        fields = '__all__'
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'nom': forms.TextInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'date_maj': forms.DateInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'fabriquant': forms.Select(attrs={'class': 'w3-input w3-round w3-border'}),
            'piece': forms.Select(attrs={'class': 'w3-input w3-round w3-border'}),
            'quantite': forms.NumberInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'information': forms.TextInput(attrs={'class': 'w3-input w3-round w3-border'}),
        }


# kit de maintenance
class Kitform(forms.ModelForm):
    """
    Formulaire de création d'un kit de maintenance de pompe à vide.
    Args:
        ModelForm : l'attribut basé sur Form de Django

    Returns:
        Le formulaire généré pour créer un kit de maintenance
    """

    class Meta:
        model = Kit
        fields = '__all__'
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'nom': forms.TextInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'fabriquant': forms.Select(attrs={'class': 'w3-input w3-round w3-border'}),
            'date_maj': forms.DateInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'ref_fab': forms.TextInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'revendeur': forms.Select(attrs={'class': 'w3-input w3-round w3-border'}),
            'ref_rev': forms.TextInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'quantite': forms.NumberInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'piece': forms.Select(attrs={'class': 'w3-input w3-round w3-border'}),
            'information': forms.TextInput(attrs={'class': 'w3-input w3-round w3-border'}),
        }


class ModifKitForm(forms.ModelForm):
    """
    Classe de modification d'un formulaire d'un kit de maintenance de pompe à vide.
    Args:
        ModelForm : l'attribut basé sur Form de Django

    Returns:
          Le formulaire avec les informations pré-remplies
    """

    class Meta:
        model = Kit
        fields = '__all__'
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'nom': forms.TextInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'fabriquant': forms.Select(attrs={'class': 'w3-input w3-round w3-border'}),
            'date_maj': forms.DateInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'ref_fab': forms.TextInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'revendeur': forms.Select(attrs={'class': 'w3-input w3-round w3-border'}),
            'ref_rev': forms.TextInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'quantite': forms.NumberInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'piece': forms.Select(attrs={'class': 'w3-input w3-round w3-border'}),
            'information': forms.TextInput(attrs={'class': 'w3-input w3-round w3-border'}),
        }


# huile
class Huileform(forms.ModelForm):
    """
    Formulaire de création d'un lot d'huile.
    Args:
        ModelForm : l'attribut basé sur Form de Django

    Returns:
        Le formulaire généré pour créer un lot d'huile
    """

    class Meta:
        model = Huile
        fields = '__all__'
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'image': forms.ClearableFileInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'fabriquant': forms.Select(attrs={'class': 'w3-input w3-round w3-border'}),
            'ref_fab': forms.TextInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'piece': forms.Select(attrs={'class': 'w3-input w3-round w3-border'}),
            'quantite': forms.NumberInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'date_maj': forms.DateInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'information': forms.TextInput(attrs={'class': 'w3-input w3-round w3-border'}),
        }


class ModifHuileForm(forms.ModelForm):
    """
    Classe de modification d'un formulaire de lot d'huile.
    Args:
        ModelForm : l'attribut basé sur Form de Django

    Returns:
          Le formulaire avec les informations pré-remplies
    """

    class Meta:
        model = Huile
        fields = '__all__'
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'image': forms.ClearableFileInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'fabriquant': forms.Select(attrs={'class': 'w3-input w3-round w3-border'}),
            'ref_fab': forms.TextInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'piece': forms.Select(attrs={'class': 'w3-input w3-round w3-border'}),
            'quantite': forms.NumberInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'date_maj': forms.DateInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'information': forms.TextInput(attrs={'class': 'w3-input w3-round w3-border'}),
        }


class Equipeform(forms.ModelForm):
    """
    Formulaire de création d'une équipe.
    Args:
        ModelForm : l'attribut basé sur Form de Django

    Returns:
        Le formulaire généré pour créer une équipe
    """

    class Meta:
        model = ModelEquipe
        fields = '__all__'
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'sigle': forms.TextInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'nom_responsable': forms.TextInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'email_responsable': forms.EmailInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'date': forms.DateInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'localisation': forms.Select(attrs={'class': 'w3-input w3-round w3-border'}),
        }


class ModifEquipeForm(forms.ModelForm):
    """
    Classe de modification d'un formulaire d'une équipe.
    Args:
        ModelForm : l'attribut basé sur Form de Django

    Returns:
          Le formulaire avec les informations pré-remplies
    """

    class Meta:
        model = ModelEquipe
        fields = '__all__'
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'sigle': forms.TextInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'nom_responsable': forms.TextInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'email_responsable': forms.EmailInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'date': forms.DateInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'localisation': forms.Select(attrs={'class': 'w3-input w3-round w3-border'}),
        }


## Fabriquant
class Fabriquantform(forms.ModelForm):
    """
    Formulaire de création d'un fabriquant.
    Args:
        ModelForm : l'attribut basé sur Form de Django

    Returns:
        Le formulaire généré pour créer un fabriquant
    """

    class Meta:
        model = Fabriquant
        fields = '__all__'
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'logo_max': forms.ClearableFileInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'logo_mini': forms.ClearableFileInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'adresse': forms.TextInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'code_postal': forms.TextInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'ville': forms.TextInput(attrs={'class': 'w3-input w3-round w3-border'}),
        }


class ModifFabriquantForm(forms.ModelForm):
    """
    Classe de modification d'un formulaire d'un fabriquant.
    Args:
        ModelForm : l'attribut basé sur Form de Django

    Returns:
            Le formulaire avec les informations pré-remplies
    """

    class Meta:
        model = Fabriquant
        fields = '__all__'
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'logo_max': forms.ClearableFileInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'logo_mini': forms.ClearableFileInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'adresse': forms.TextInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'code_postal': forms.TextInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'ville': forms.TextInput(attrs={'class': 'w3-input w3-round w3-border'}),
        }


## Lieux

class Siteform(forms.ModelForm):
    """
    Formulaire de création d'un site.
    Args:
        ModelForm : l'attribut basé sur Form de Django

    Returns:
        Le formulaire généré pour créer un site
    """

    class Meta:
        model = Site
        fields = '__all__'
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'w3-input w3-round w3-border'}),
        }


class ModifSiteForm(forms.ModelForm):
    """
    Classe de modification d'un formulaire d'un site.
    Args:
        ModelForm : l'attribut basé sur Form de Django

     Returns:
            Le formulaire avec les informations pré-remplies
    """

    class Meta:
        model = Site
        fields = '__all__'
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'w3-input w3-round w3-border'}),
        }


class Batimentform(forms.ModelForm):
    """
    Formulaire de création d'un bâtiment sur un site.
    Args:
        ModelForm : l'attribut basé sur Form de Django

    Returns:
        Le formulaire généré pour créer un bâtiment
    """

    class Meta:
        model = Batiment
        fields = '__all__'
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'site': forms.Select(attrs={'class': 'w3-input w3-round w3-border'}),

        }


class ModifBatimentForm(forms.ModelForm):
    """
    Classe de modification d'un formulaire d'un bâtiment.
    Args:
        ModelForm : l'attribut basé sur Form de Django

     Returns:
            Le formulaire avec les informations pré-remplies
    """

    class Meta:
        model = Batiment
        fields = '__all__'
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'site': forms.Select(attrs={'class': 'w3-input w3-round w3-border'}),

        }


class Etageform(forms.ModelForm):
    """
    Formulaire de création d'un étage dans un bâtiment.
    Args:
        ModelForm : l'attribut basé sur Form de Django

    Returns:
        Le formulaire généré pour créer un étage
    """

    class Meta:
        model = Etage
        fields = '__all__'
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'batiment': forms.Select(attrs={'class': 'w3-input w3-round w3-border'}),

        }


class ModifEtageForm(forms.ModelForm):
    """
    Classe de modification d'un formulaire d'un étage.
    Args:
        ModelForm : l'attribut basé sur Form de Django

     Returns:
            Le formulaire avec les informations pré-remplies
    """

    class Meta:
        model = Etage
        fields = '__all__'
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'batiment': forms.Select(attrs={'class': 'w3-input w3-round w3-border'}),

        }


class Pieceform(forms.ModelForm):
    """
    Formulaire de création d'une pièce ou salle.
    Args:
        ModelForm : l'attribut basé sur Form de Django

    Returns:
        Le formulaire généré pour créer une pièce
    """

    class Meta:
        model = Piece
        fields = '__all__'
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'etage': forms.Select(attrs={'class': 'w3-input w3-round w3-border'}),

        }


class ModifPieceForm(forms.ModelForm):
    """
    Classe de modification d'un formulaire d'une pièce ou salle.
    Args:
        ModelForm : l'attribut basé sur Form de Django

     Returns:
            Le formulaire avec les informations pré-remplies
    """

    class Meta:
        model = Piece
        fields = '__all__'
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'w3-input w3-round w3-border'}),
            'etage': forms.Select(attrs={'class': 'w3-input w3-round w3-border'}),

        }
