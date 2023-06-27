"""
Classes de filtres pour les recherches de stocks de pompes
"""
import django_filters
from .models import StockPompe, Batiment, Inventaire, ModelePompe


class PompeStockFilter(django_filters.FilterSet):

    etage__batiment = django_filters.ModelChoiceFilter(queryset=Batiment.objects.all(), label='Bâtiment')
    pompe = django_filters.ModelChoiceFilter(queryset=ModelePompe.objects.all(), label='Pompe')
    inventaire = django_filters.ModelChoiceFilter(queryset=Inventaire.objects.all(), label='N° d\'inventaire')

    class Meta:
        model = StockPompe
        fields = [
              'equipe',
              'etage__batiment',
              'etage',
              'piece',
              'pompe',
              'inventaire',
              'statut'
              ]
