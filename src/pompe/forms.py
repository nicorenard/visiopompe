"""
Forms of the project Visiopompe
"""
from django import forms
from .models import *


# stock pompes
class StockPompeform(forms.ModelForm):
    class Meta:
        model = StockPompe
        fields = '__all__'


class ModifStockPompeForm(forms.ModelForm):
    class Meta:
        model = StockPompe
        exclude = ['mise_en_service']


class Inventaireform(forms.ModelForm):
    class Meta:
        model = Inventaire
        fields = '__all__'


class ModifInventaireForm(forms.ModelForm):
    class Meta:
        model = Inventaire
        fields = '__all__'


class Tutelleform(forms.ModelForm):
    class Meta:
        model = Tutelle
        fields = '__all__'


class ModifTutelleForm(forms.ModelForm):
    class Meta:
        model = Tutelle
        fields = '__all__'


# fiche pompes
class ModelPompeform(forms.ModelForm):
    class Meta:
        model = ModelePompe
        fields = '__all__'


class ModifModelPompeForm(forms.ModelForm):
    class Meta:
        model = ModelePompe
        fields = '__all__'


class Technologieform(forms.ModelForm):
    class Meta:
        model = TechnologiePompe
        fields = '__all__'


class ModifTechnoForm(forms.ModelForm):
    class Meta:
        model = TechnologiePompe
        fields = '__all__'


# documentations
class Docform(forms.ModelForm):
    class Meta:
        model = Document
        fields = '__all__'


class ModifDocForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = '__all__'


# pieces detachées
class PiecePompeform(forms.ModelForm):
    class Meta:
        model = PiecesPompe
        fields = '__all__'


class ModifPiecePompeForm(forms.ModelForm):
    class Meta:
        model = PiecesPompe
        fields = '__all__'


# kit de maintenance
class Kitform(forms.ModelForm):
    class Meta:
        model = Kit
        fields = '__all__'


class ModifKitForm(forms.ModelForm):
    class Meta:
        model = Kit
        fields = '__all__'


# huile
class Huileform(forms.ModelForm):
    class Meta:
        model = Huile
        fields = '__all__'


class ModifHuileForm(forms.ModelForm):
    class Meta:
        model = Huile
        fields = '__all__'


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
    Classe de modification d'une formulaire d'une équipe.
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
    class Meta:
        model = Site
        fields = '__all__'


class ModifSiteForm(forms.ModelForm):
    class Meta:
        model = Site
        fields = '__all__'


class Batimentform(forms.ModelForm):
    class Meta:
        model = Batiment
        fields = '__all__'


class ModifBatimentForm(forms.ModelForm):
    class Meta:
        model = Batiment
        fields = '__all__'


class Etageform(forms.ModelForm):
    class Meta:
        model = Etage
        fields = '__all__'


class ModifEtageForm(forms.ModelForm):
    class Meta:
        model = Etage
        fields = '__all__'


class Pieceform(forms.ModelForm):
    class Meta:
        model = Piece
        fields = '__all__'


class ModifPieceForm(forms.ModelForm):
    class Meta:
        model = Piece
        fields = '__all__'
