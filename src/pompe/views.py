from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Pompes, PiecesPompe, Kit, Huile
from .forms import ModifPompeForm

def index(request):
    pompes = Pompes.objects.all().order_by('localisation_etage')
    return render(request, 'pompe/index.html', {'pompes': pompes})

def huile(request):
    huiles = Huile.objects.all().order_by('marque')
    return render(request, 'pompe/huile.html', {'huiles': huiles})

def kit(request):
    kits = Kit.objects.all().order_by('nom')
    return render(request, 'pompe/kit.html', {'kits': kits})

def piece(request):
    pieces = PiecesPompe.objects.all().order_by('nom')
    return render(request, 'pompe/pieces.html', {'pieces': pieces})




# definir API pour appli bureau ?

