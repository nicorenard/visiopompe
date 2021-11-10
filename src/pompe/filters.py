import django_filters
from .models import *

class PompeFilter(django_filters.FilterSet):
    class Meta:
        model = Pompes
        fields = ['marque','localisation_etage','localisation_piece','localisation_emplacement']
