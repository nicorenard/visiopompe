import datetime
from django.shortcuts import render
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
    pompes = StockPompe.objects.all().order_by('mise_en_service')
    current_date = datetime.date.today()
    warning_date = current_date + datetime.timedelta(days=7)
    context = {'pompes': pompes,
               'current_date': current_date,
               'warning_date': warning_date
               }
    return render(request, 'pompe/pompe.html', context)

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





