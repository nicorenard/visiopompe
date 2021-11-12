
from django.shortcuts import render, redirect, get_object_or_404
from .models import Pompes, PiecesPompe, Kit, Huile
from .forms import ModifPompeForm, Pompeform, PieceForm, ModifPieceForm, HuileForm, ModifHuileForm, KitForm, \
    ModifKitForm
from .filters import PompeFilter


def index(request):
    pompes = Pompes.objects.all().order_by('localisation_etage')
    filterpompe = PompeFilter(request.GET, queryset=pompes)
    pompes = filterpompe.qs

    context = {'pompes': pompes, 'filterpompe' : filterpompe}
    return render(request, 'pompe/index.html', context)


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
    return render(request, 'pompe/forms.html', {'form': form})


def suppression_pompe(request, pk):
    pompe = Pompes.objects.get(pk=pk)
    if request.method =="POST":
        pompe.delete()
        return redirect('/pompe')

    context = {'item': pompe}
    return render(request, 'pompe/suppression.html', context)


def piece(request):
    pieces = PiecesPompe.objects.all().order_by('nom')
    return render(request, 'pompe/pieces.html', {'pieces': pieces})


def ajout_piece(request):
    if request.method == "POST":
        form = PieceForm(request.POST)
        if form.is_valid():
        #    handle_uploaded_file(request.FILES['file'])
            form.save()
        return redirect("/pompe/pieces")

    else:
        form = PieceForm()

    return render(request, 'pompe/forms2.html', {'form': form})


def modif_piece(request, pk):
    piece= get_object_or_404(PiecesPompe, pk=pk)

    if request.method == "POST":
        form = ModifPieceForm(request.POST, instance=piece)
        if form.is_valid():
            form.save()
            return redirect("/pompe/pieces")
    else:
        form = ModifPieceForm(instance=piece)
    return render(request, 'pompe/forms2.html', {'form': form})


def suppression_piece(request, pk):
    piece = PiecesPompe.objects.get(pk=pk)
    if request.method =="POST":
        piece.delete()
        return redirect("/pompe/pieces")

    context = {'item': piece}
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
    huile= get_object_or_404(Huile, pk=pk)

    if request.method == "POST":
        form = ModifHuileForm(request.POST, instance=huile)
        if form.is_valid():
            form.save()
            return redirect("/pompe/huiles")
    else:
        form = ModifHuileForm(instance=huile)
    return render(request, 'pompe/forms3.html', {'form': form})


def suppression_huile(request, pk):
    huile = Huile.objects.get(pk=pk)
    if request.method =="POST":
        huile.delete()
        return redirect("/pompe/huiles")

    context = {'item': huile}
    return render(request, 'pompe/suppression_huile.html', context)


def kit(request):
    kits = Kit.objects.all().order_by('nom')
    return render(request, 'pompe/kit.html', {'kits': kits})


def ajout_kit(request):
    if request.method == "POST":
        form = KitForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/pompe/kit")
    else:
        form = KitForm()

    return render(request, 'pompe/forms4.html', {'form': form})


def modif_kit(request, pk):
    kit= get_object_or_404(Kit, pk=pk)

    if request.method == "POST":
        form = ModifKitForm(request.POST, instance=kit)
        if form.is_valid():
            form.save()
            return redirect("/pompe/kit")
    else:
        form = ModifKitForm(instance=kit)
    return render(request, 'pompe/forms4.html', {'form': form})


def suppression_kit(request, pk):
    kit = Kit.objects.get(pk=pk)
    if request.method =="POST":
        kit.delete()
        return redirect("/pompe/kit")

    context = {'item': kit}
    return render(request, 'pompe/suppression_kit.html', context)

# definir API pour appli bureau ?

