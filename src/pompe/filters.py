"""
Filter function for pump search
"""
import django_filters
from .models import *


class PompeStockFilter(django_filters.FilterSet):

   class Meta:
        model = StockPompe
        fields = ['pompe', 'equipe', 'etage__batiment','etage', 'piece', 'inventaire', 'statut']
