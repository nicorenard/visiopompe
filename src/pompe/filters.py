import django_filters
from django.forms import CheckboxSelectMultiple
from .models import *


class PompeStockFilter(django_filters.FilterSet):
    pompe = django_filters.ModelMultipleChoiceFilter(
        queryset=ModelePompe.objects.all(),
        widget=CheckboxSelectMultiple(),
        label="Pompe",
        label_suffix="",
    )

    equipe = django_filters.ModelMultipleChoiceFilter(
        queryset=ModelEquipe.objects.all(),
        widget=CheckboxSelectMultiple(),
        label="Equipe",
        label_suffix="",
    )

    etage = django_filters.ModelMultipleChoiceFilter(
        queryset=Etage.objects.all(),
        widget=CheckboxSelectMultiple(),
        label="Etage",
        label_suffix="",
    )

    piece = django_filters.ModelMultipleChoiceFilter(
        queryset=Piece.objects.all(),
        widget=CheckboxSelectMultiple(),
        label="Piece",
        label_suffix="",
    )

    inventaire = django_filters.ModelMultipleChoiceFilter(
        queryset=Inventaire.objects.all(),
        widget=CheckboxSelectMultiple(),
        label="Pompe",
        label_suffix="",
    )

    class Meta:
        model = StockPompe
        fields = ['pompe', 'equipe', 'etage', 'piece', 'inventaire']
