import datetime
from django.shortcuts import render, redirect, get_object_or_404
from field_history.models import FieldHistory
from .models import Pompes, PiecesPompe, Kit, Huile, Doc, VersionApp
from .forms import ModifPompeForm, Pompeform, PieceForm, ModifPieceForm, HuileForm, ModifHuileForm, KitForm, \
    ModifKitForm, DocForm
from .filters import PompeFilter


def index(request):
    pompes = Pompes.objects.all().order_by('localisation_etage')
    filterpompe = PompeFilter(request.GET, queryset=pompes)
    pompes = filterpompe.qs
    current_date = datetime.date.today()
    history = list(FieldHistory.objects.all())

    context = {'pompes': pompes, 'filterpompe': filterpompe, 'current_date': current_date, 'history':history}
    return render(request, 'pompe/index.html', context)


def ajout_pompe(request):
    if request.method == "POST":
        form = Pompeform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/pompe')

    else:
        form = Pompeform()
    return render(request, 'pompe/forms.html', {'form': form})


def modif_pompe(request, pk):
    pompe = get_object_or_404(Pompes, pk=pk)

    if request.method == "POST":
        form = ModifPompeForm(request.POST, instance=pompe)
        if form.is_valid():
            form.save()
            return redirect('/pompe')
    else:
        form = ModifPompeForm(instance=pompe)
    return render(request, 'pompe/forms.html', {'form': form})


def suppression_pompe(request, pk):
    pompe = Pompes.objects.get(pk=pk)
    if request.method == "POST":
        pompe.delete()
        return redirect('/pompe')

    context = {'item': pompe}
    return render(request, 'pompe/suppression.html', context)


def piece(request):
    pieces = PiecesPompe.objects.all().order_by('nom')
    return render(request, 'pompe/pieces.html', {'pieces': pieces})


def ajout_piece(request):
    if request.method == "POST":
        form = PieceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect("/pompe/pieces")
    else:
        form = PieceForm()
    return render(request, 'pompe/forms2.html', {'form': form})


def modif_piece(request, pk):
    pieces = get_object_or_404(PiecesPompe, pk=pk)

    if request.method == "POST":
        form = ModifPieceForm(request.POST, instance=pieces)
        if form.is_valid():
            form.save()
            return redirect("/pompe/pieces")
    else:
        form = ModifPieceForm(instance=pieces)
    return render(request, 'pompe/forms2.html', {'form': form})


def suppression_piece(request, pk):
    pieces = PiecesPompe.objects.get(pk=pk)
    if request.method == "POST":
        pieces.delete()
        return redirect("/pompe/pieces")

    context = {'item': pieces}
    return render(request, 'pompe/suppression_piece.html', context)


def huile(request):
    huiles = Huile.objects.all().order_by('marque')

    return render(request, 'pompe/huile.html', {'huiles': huiles})


def ajout_huile(request):
    if request.method == "POST":
        form = HuileForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/pompe/huiles")
    else:
        form = HuileForm()

    return render(request, 'pompe/forms3.html', {'form': form})


def modif_huile(request, pk):
    huiles = get_object_or_404(Huile, pk=pk)

    if request.method == "POST":
        form = ModifHuileForm(request.POST, instance=huiles)
        if form.is_valid():
            form.save()
            return redirect("/pompe/huiles")
    else:
        form = ModifHuileForm(instance=huiles)
    return render(request, 'pompe/forms3.html', {'form': form})


def suppression_huile(request, pk):
    huiles = Huile.objects.get(pk=pk)
    if request.method == "POST":
        huiles.delete()
        return redirect("/pompe/huiles")

    context = {'item': huiles}
    return render(request, 'pompe/suppression_huile.html', context)


def kit(request):
    kits = Kit.objects.all().order_by('nom')
    return render(request, 'pompe/kit.html', {'kits': kits})


def ajout_kit(request):
    if request.method == "POST":
        form = KitForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect("/pompe/kit")
    else:
        form = KitForm()

    return render(request, 'pompe/forms4.html', {'form': form})


def modif_kit(request, pk):
    kits = get_object_or_404(Kit, pk=pk)

    if request.method == "POST":
        form = ModifKitForm(request.POST, instance=kits)
        if form.is_valid():
            form.save()
            return redirect("/pompe/kit")
    else:
        form = ModifKitForm(instance=kits)
    return render(request, 'pompe/forms4.html', {'form': form})


def suppression_kit(request, pk):
    kits = Kit.objects.get(pk=pk)
    if request.method == "POST":
        kits.delete()
        return redirect("/pompe/kit")

    context = {'item': kits}
    return render(request, 'pompe/suppression_kit.html', context)

def doc(request):
    docs = Doc.objects.all().order_by('fabriquant')

    context = {'docs': docs}
    return render(request, 'pompe/doc.html', context)

def ajout_doc(request):
    if request.method == "POST":
        form = DocForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/pompe/doc')

    else:
        form = DocForm()
    return render(request, 'pompe/forms5.html', {'form': form})


def version(request):
    versions = VersionApp.objects.all().order_by('-version')
    return render(request, 'pompe/versionapp.html', {'versions': versions})


# definir API pour appli bureau ?
