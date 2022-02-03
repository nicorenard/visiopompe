from django import forms
from .models import *


class StockPompeform(forms.ModelForm):

    class Meta:
        model = StockPompe
        fields = '__all__'


class ModifStockPompeForm(forms.ModelForm):

    class Meta:
        model = StockPompe
        exclude = ['mise_en_service']

class ModelPompeform(forms.ModelForm):

    class Meta:
        model = ModelePompe
        fields = '__all__'


class ModifModelPompeForm(forms.ModelForm):

    class Meta:
        model = ModelePompe
        fields = '__all__'
