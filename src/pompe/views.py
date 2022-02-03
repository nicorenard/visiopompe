import datetime
from django.shortcuts import render, get_object_or_404, redirect
from .filters import PompeStockFilter
from .forms import *
from .models import *

def index(request):
   return render(request, 'pompe/index.html')

def version(request):
    versions = VersionApp.objects.all().order_by('-version')
    return render(request, 'pompe/versionapp.html', {'versions': versions})

def dashboard(request):
    dash_pompes = StockPompe.objects.all()
    p_all = dash_pompes.count()
    p_valide = dash_pompes.filter(statut='A').count()
    p_stock = dash_pompes.filter(statut='S').count()
    p_hs = dash_pompes.filter(statut='P').count()
    p_rep = dash_pompes.filter(statut='R').count()
    p_etage = dash_pompes.filter(piece_id= 0).count()

    fabriquants = Fabriquant.objects.all().order_by('nom')

    context = {'p_all': p_all,'p_valide': p_valide, 'p_stock': p_stock,'p_hs': p_hs,'p_rep': p_rep,
               'fabriquants': fabriquants, 'p_etage' : p_etage,

    }
    return render(request, 'pompe/dashboard.html', context)


def pompe(request):
    model_pompes = ModelePompe.objects.all().order_by('nom')
    stock_pompes = StockPompe.objects.all().order_by('num_inventaire')
    filterpompe = PompeStockFilter(request.GET, queryset=stock_pompes)
    stock_pompes = filterpompe.qs
    current_date = datetime.date.today()
    warning_date = current_date + datetime.timedelta(days=7)

    context = {'model_pompe': model_pompes,
               'stock_pompe' : stock_pompes,
               'current_date': current_date,
               'warning_date': warning_date,
               'filterpompe': filterpompe,
               }
    return render(request, 'pompe/pompe.html', context)

def add_stockpompe(request):
    if request.method == "POST":
        form = StockPompeform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('pompe/pompe')

    else:
        form = StockPompeform()
    return render(request, 'pompe/forms.html', {'form': form})


def update_stockpompe(request, pk):
    stock_pompes = get_object_or_404(StockPompe, pk=pk)

    if request.method == "POST":
        form = ModifStockPompeForm(request.POST, instance=stock_pompes)
        if form.is_valid():
            form.save()
            return redirect('/pompe/pompe')
    else:
        form = ModifStockPompeForm(instance=stock_pompes)
    return render(request, 'pompe/forms.html', {'form': form})

def piece(request):
    pieces = PiecesPompe.objects.all().order_by('nom')
    return render(request, 'pompe/piece.html', {'pieces': pieces})

def huile(request):
    huiles = Huile.objects.all().order_by('nom')
    return render(request, 'pompe/piece.html', {'huiles': huiles})

def kit(request):
    kits = Kit.objects.all().order_by('nom')
    return render(request, 'pompe/piece.html', {'kits': kits})

def doc(request):
    docs = Doc.objects.all().order_by('nom')
    return render(request, 'pompe/doc.html', {'docs' : docs})





