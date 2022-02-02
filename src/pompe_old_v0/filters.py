import django_filters
from .models import *
from django_filters import CharFilter


class PompeFilter(django_filters.FilterSet):
    #### If you need to search inside a bigger place, take off the # in front of Site.nom and Batiment.nom####
    #### Add also in the fields [], 'Site.nom' and 'Batiment.nom'#######

    # Site.nom = CharFilter(field_name="nom", lookup_expr='icontains', label='Site')
    # Batiment.nom = CharFilter(field_name="nom", lookup_expr='icontains', label='Batiment')

    Etage.nom= CharFilter(field_name="nom", lookup_expr='icontains', label='Etage')
    Piece.nom = CharFilter(field_name="nom", lookup_expr='icontains', label='Piece')
    statut = CharFilter(field_name="status", lookup_expr='icontains', label='Statut')
    num_inventaire = CharFilter(field_name="num_inventaire", lookup_expr='icontains', label='Inventaire UMR')

    class Meta:
        model = StockPompe
        fields = ['Piece.nom', 'Etage.nom', 'statut', 'num_inventaire']
