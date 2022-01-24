import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import StockPompe, VersionApp
# from .filters import PompeFilter
#from .resource import PompeRessource


def index(request):
    pompes = StockPompe.objects.all().order_by('mise_en_service')
    filterpompe = PompeFilter(request.GET, queryset=pompes)
    pompes = filterpompe.qs
    current_date = datetime.date.today()
    warning_date = current_date + datetime.timedelta(days=7)



    context = {'pompes': pompes, 'filterpompe': filterpompe, 'current_date': current_date, 'warning_date': warning_date
               }
    return render(request, 'pompe/index.html', context)

'''def dashboard(request):
    pompes = StockPompe.objects.all()
    pompes_mod = ModelePompe.objects.all()
    pompe_ok = pompes.filter(statut='A').count()
    pompe_stock = pompes.filter(statut='S').count()
    pompe_hs = pompes.filter(statut='P').count()
    pompe_rep = pompes.filter(statut='R').count()
    pompe_e1 = pompes_mod.filter(piece.etage='1er étage').count()
    pompe_e2 = pompes_mod.filter(localisation_etage='2ème étage').count()
    pompe_e3 = pompes_mod.filter(localisation_etage='3ème étage').count()
    pompe_all = pompes.count()

    context = {'pompe_ok':pompe_ok}


def export(request):
    pompe_resource = PompeRessource()
    datapompe = pompe_resource.export()
    response = HttpResponse(datapompe.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="datapompe.csv"'
    return response
'''

def version(request):
    versions = VersionApp.objects.all().order_by('-version')
    return render(request, 'pompe/versionapp.html', {'versions': versions})
