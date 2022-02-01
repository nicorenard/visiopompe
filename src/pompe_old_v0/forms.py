from django import forms
from .models import *


class Pompeform(forms.ModelForm):

    class Meta:
        model = Pompes
        fields = '__all__'


class ModifPompeForm(forms.ModelForm):

    class Meta:
        model = Pompes
        fields = ("localisation_etage", "localisation_piece", "localisation_emplacement", "statut", "vide_teste",
                  "date_vidange", "huile", "information")


class HuileForm(forms.ModelForm):

    class Meta:
        model = Huile
        fields = '__all__'


class ModifHuileForm(forms.ModelForm):

    class Meta:
        model = Huile
        fields = ("localisation", "quantite", "information")


class PieceForm(forms.ModelForm):

    class Meta:
        model = PiecesPompe
        fields = '__all__'


class ModifPieceForm(forms.ModelForm):

    class Meta:
        model = PiecesPompe
        fields = ("localisation", "quantite", "information")


class KitForm(forms.ModelForm):

    class Meta:
        model = Kit
        fields = '__all__'


class ModifKitForm(forms.ModelForm):

    class Meta:
        model = Kit
        fields = ("localisation", "quantite", "information")


class DocForm(forms.ModelForm):

    class Meta:
        model = Doc
        fields = '__all__'