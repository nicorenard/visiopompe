import datetime
from django.shortcuts import render
from src.pompe.models import StockPompe, VersionApp



def index(request):
    pompes = StockPompe.objects.all().order_by('mise_en_service')
    current_date = datetime.date.today()
    warning_date = current_date + datetime.timedelta(days=7)



    context = {'pompes': pompes, 'current_date': current_date, 'warning_date': warning_date
               }
    return render(request, 'pompe/index.html', context)


def version(request):
    versions = VersionApp.objects.all().order_by('-version')
    return render(request, 'pompe/versionapp.html', {'versions': versions})
