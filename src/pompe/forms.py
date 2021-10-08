from django import forms
from django.forms import ModelForm
from .models import Pompes

class AjoutPompe(ModelForm):
    class Meta:
        model = Pompes
        fields = '__all__'

class ModifPompeForm(forms.ModelForm):

    class Meta:
        model = Pompes
        fields = ("localisation_etage", "localisation_piece", "localisation_emplacement", "statut", "vide_teste", "date_derniere_vidange",
              "huile", "manuel", "information")

