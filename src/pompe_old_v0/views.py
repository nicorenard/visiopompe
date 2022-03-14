import datetime

def index(request):
    pompes = Pompes.objects.all().order_by('mise_en_service')
    filterpompe = PompeFilter(request.GET, queryset=pompes)
    pompes = filterpompe.qs
    current_date = datetime.date.today()
    warning_date = current_date + datetime.timedelta(days=7)


    context = {'pompes': pompes, 'filterpompe': filterpompe, 'current_date': current_date,
               'warning_date': warning_date
               }
    return render(request, 'pompe/index.html', context)

def export(request):
    pompe_resource = PompeRessource()
    datapompe = pompe_resource.export()
    response = HttpResponse(datapompe.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="datapompe.csv"'
    return response

