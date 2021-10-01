from django import forms
from .models import Pompes

class AjoutPompe(forms.ModelForm):
    pass

class ModifPompeForm(forms.ModelForm):

    class Meta:
        model = Pompes
        fields = ("localisation_etage", "localisation_piece", "localisation_emplacement", "statut", "vide_teste", "date_derniere_vidange",
              "huile", "manuel", "information")

