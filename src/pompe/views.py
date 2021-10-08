from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from .models import Pompes, PiecesPompe, Kit, Huile
from .forms import ModifPompeForm, AjoutPompe


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

def modifpompes(request):
    form = ModifPompeForm()
    return render(request, 'pompe/index.html', {'form': form})

class PompeAjout(View):
    def get(self, request):
        form = AjoutPompe()
        ctx = {'form': form}
        return render(request, 'pompe/index.html', ctx)

    def post(self, request):
        form = AjoutPompe(request.POST)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, 'pompe/index.html', ctx)

        nouvellepompe = form.save()
        x = reverse('form:main') + '#' + str(nouvellepompe.id)
        return redirect(x)

class PompeUpdate(View):
    def get(self, request, pk):
        oldpompe = get_object_or_404(Pompes, pk=pk)
        form = AjoutPompe(instance=oldpompe)
        ctx = {'form': form}
        return render(request, 'pompe/index.html', ctx)

    def post(self, request, pk):
        oldpompe = get_object_or_404(Pompes, pk=pk)
        form = AjoutPompe(request.POST, instance=oldpompe)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, 'pompe/index.html', ctx)

        editpompe = form.save()
        x = reverse('form:main')
        return redirect(x)

# definir API pour appli bureau ?

