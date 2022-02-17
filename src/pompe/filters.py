import django_filters
from .models import *
from django_filters import CharFilter


class PompeStockFilter(django_filters.FilterSet):

    piece = CharFilter(field_name="piece", lookup_expr='icontains', label='Piece')
    statut = CharFilter(field_name="statut", lookup_expr='icontains', label='Statut')
    inventaire = CharFilter(field_name="inventaire", lookup_expr='icontains', label='Inventaire UMR')

    class Meta:
        model = StockPompe
        fields = ['pompe','equipe','etage','piece','inventaire']
