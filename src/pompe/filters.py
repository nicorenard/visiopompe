import django_filters
from .models import *
from django_filters import CharFilter

class PompeFilter(django_filters.FilterSet):
    localisation_piece = CharFilter(field_name="Pièce", lookup_expr='icontains', label='Pièce')

    class Meta:
        model = Pompes
        fields = ['marque', 'statut','localisation_etage','localisation_piece','localisation_emplacement']
