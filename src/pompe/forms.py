from django import forms
from .models import *

#stock pompes
class StockPompeform(forms.ModelForm):

    class Meta:
        model = StockPompe
        fields = '__all__'


class ModifStockPompeForm(forms.ModelForm):

    class Meta:
        model = StockPompe
        exclude = ['mise_en_service']


class Inventaireform(forms.ModelForm):

    class Meta:
        model = Inventaire
        fields = '__all__'


class ModifInventaireForm(forms.ModelForm):

    class Meta:
        model = Inventaire
        fields = '__all__'

#fiche pompes
class ModelPompeform(forms.ModelForm):

    class Meta:
        model = ModelePompe
        fields = '__all__'


class ModifModelPompeForm(forms.ModelForm):

    class Meta:
        model = ModelePompe
        fields = '__all__'

# documentations
class Docform(forms.ModelForm):

    class Meta:
        model = Doc
        fields = '__all__'


class ModifDocForm(forms.ModelForm):

    class Meta:
        model = Doc
        fields = '__all__'

# pieces detachées
class PiecePompeform(forms.ModelForm):
    class Meta:
        model = PiecesPompe
        fields = '__all__'


class ModifPiecePompeForm(forms.ModelForm):
    class Meta:
        model = PiecesPompe
        fields = '__all__'

# kit de maintenance
class Kitform(forms.ModelForm):
    class Meta:
        model = Kit
        fields = '__all__'


class ModifKitForm(forms.ModelForm):
    class Meta:
        model = Kit
        fields = '__all__'

# huile
class Huileform(forms.ModelForm):
    class Meta:
        model = Huile
        fields = '__all__'


class ModifHuileForm(forms.ModelForm):
    class Meta:
        model = Huile
        fields = '__all__'

#dashboard
## equipe
class Equipeform(forms.ModelForm):
    class Meta:
        model = ModelEquipe
        fields = '__all__'


class ModifEquipeForm(forms.ModelForm):
    class Meta:
        model = ModelEquipe
        fields = '__all__'

## Fabriquant
class Fabriquantform(forms.ModelForm):
    class Meta:
        model = Fabriquant
        fields = '__all__'


class ModifFabriquantForm(forms.ModelForm):
    class Meta:
        model = Fabriquant
        fields = '__all__'
## Lieux
class Siteform(forms.ModelForm):
    class Meta:
        model = Site
        fields = '__all__'

class ModifSiteForm(forms.ModelForm):
    class Meta:
        model = Site
        fields = '__all__'


class Batimentform(forms.ModelForm):
    class Meta:
        model = Batiment
        fields = '__all__'

class ModiBatimentForm(forms.ModelForm):
    class Meta:
        model = Batiment
        fields = '__all__'

class Etageform(forms.ModelForm):
    class Meta:
        model = Etage
        fields = '__all__'


class ModifEtageForm(forms.ModelForm):
    class Meta:
        model = Etage
        fields = '__all__'


class Pieceform(forms.ModelForm):
    class Meta:
        model = Piece
        fields = '__all__'

class ModifPieceForm(forms.ModelForm):
    class Meta:
        model = Piece
        fields = '__all__'