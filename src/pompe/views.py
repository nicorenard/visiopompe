
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Pompes, PiecesPompe, Kit, Huile
from .forms import ModifPompeForm, Pompeform


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

def ajout_pompe(request):
    if request.method == "POST":
        form = Pompeform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/index')
    else:
        form = Pompeform()
    return render(request, 'pompe/forms.html', {'form': form})

def modif_pompe(request):
    if request.method == "POST":
        form = ModifPompeForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'pompe/index.html')
    else:
        form = ModifPompeForm()
    return



# definir API pour appli bureau ?

