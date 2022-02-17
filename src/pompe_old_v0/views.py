import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Pompes, PiecesPompe, Kit, Huile, Doc
from src.pompe.forms import ModifPompeForm, Pompeform, PieceForm, ModifPieceForm, HuileForm, ModifHuileForm, KitForm, \
    ModifKitForm, DocForm
from src.pompe.filters import PompeFilter
from .resource import PompeRessource


def index(request):
    pompes = Pompes.objects.all().order_by('mise_en_service')
    filterpompe = PompeFilter(request.GET, queryset=pompes)
    pompes = filterpompe.qs
    current_date = datetime.date.today()
    warning_date = current_date + datetime.timedelta(days=7)
    #pour la dashboard
    pompe_ok = pompes.filter(statut='A').count()
    pompe_stock = pompes.filter(statut='S').count()
    pompe_hs = pompes.filter(statut='P').count()
    pompe_rep = pompes.filter(statut='R').count()
    pompe_e1 = pompes.filter(localisation_etage='1er étage').count()
    pompe_e2 = pompes.filter(localisation_etage='2ème étage').count()
    pompe_e3 = pompes.filter(localisation_etage='3ème étage').count()
    pompe_all = pompes.count()


    context = {'pompes': pompes, 'filterpompe': filterpompe, 'current_date': current_date,
               'pompe_ok': pompe_ok, 'pompe_stock': pompe_stock, 'pompe_hs': pompe_hs, 'pompe_rep': pompe_rep,
               'pompe_all': pompe_all, 'pompe_e1': pompe_e1, 'pompe_e2': pompe_e2, 'pompe_e3': pompe_e3, 'warning_date': warning_date
               }
    return render(request, 'pompe/index.html', context)

def export(request):
    pompe_resource = PompeRessource()
    datapompe = pompe_resource.export()
    response = HttpResponse(datapompe.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="datapompe.csv"'
    return response

def ajout_pompe(request):
    if request.method == "POST":
        form = Pompeform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/pompe/pompe')

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
    return render(request, 'pompe/forms_suppression.html', context)


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
