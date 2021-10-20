
from django.shortcuts import render, redirect, get_object_or_404
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

def suppression_pompe(request, pk):
    Pompes.objects.filter(id=id).delete()
    pass

def ajout_pompe(request):
    if request.method == "POST":
        form = Pompeform(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/pompe')

    else:
        form = Pompeform()

    return render(request, 'pompe/forms.html', {'form': form})

def modif_pompe(request, pk):
    pompe= get_object_or_404(Pompes, pk=pk)

    if request.method == "POST":
        form = ModifPompeForm(request.POST, instance=pompe)
        if form.is_valid():
            form.save()
            return redirect('/pompe')
    else:
        form = ModifPompeForm(instance=pompe)
    return render(request, 'pompe/pompe_edit.html', {'form': form})



# definir API pour appli bureau ?

