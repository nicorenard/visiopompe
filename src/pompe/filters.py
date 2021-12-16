import django_filters
from .models import *
from django_filters import CharFilter


class PompeFilter(django_filters.FilterSet):
    localisation_piece = CharFilter(field_name="localisation_piece", lookup_expr='icontains', label='Pièce')
    localisation_emplacement = CharFilter(field_name="localisation_emplacement", lookup_expr='icontains', label='Place')
    code_umr = CharFilter(field_name="code_umr", lookup_expr='icontains', label='Inventaire UMR')

    class Meta:
        model = Pompes
        fields = ['marque', 'statut', 'localisation_etage', 'localisation_piece', 'localisation_emplacement', 'code_umr']
