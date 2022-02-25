from import_export import resources
from .models import *

## pompes
class ModelePompeRessource(resources.ModelResource):
    class Meta:
        model = ModelePompe

class StockPompeRessource(resources.ModelResource):
    class Meta:
        model = StockPompe

class FabriquantRessource(resources.ModelResource):
    class Meta:
        model = Fabriquant

class TechnologieRessource(resources.ModelResource):
    class Meta:
        model = TechnologiePompe

##Accessoire pompes

class HuileRessource(resources.ModelResource):
    class Meta:
        model = Huile

class PiecePompeRessource(resources.ModelResource):
    class Meta:
        model = PiecesPompe

class KitRessource(resources.ModelResource):
    class Meta:
        model = Kit

class DocRessource(resources.ModelResource):
    class Meta:
        model = Doc

class EquipeResource(resources.ModelResource):
    class Meta:
        model = ModelEquipe

## Lieux
class SiteResource(resources.ModelResource):
    class Meta:
        model = Site

class BatimentResource(resources.ModelResource):
    class Meta:
        model = Batiment

class EtageResource(resources.ModelResource):
    class Meta:
        model = Etage

class PieceResource(resources.ModelResource):
    class Meta:
        model = Piece

class TutelleRessource(resources.ModelResource):
    class Meta:
        model = Tutelle

class InventaireRessource(resources.ModelResource):
    class Meta:
        model = Inventaire


