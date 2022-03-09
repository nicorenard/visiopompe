import datetime


from src.pompe.resource import PompeRessource


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



def suppression_pompe(request, pk):
    pompe = Pompes.objects.get(pk=pk)
    if request.method == "POST":
        pompe.delete()
        return redirect('/pompe')

    context = {'item': pompe}
    return render(request, 'pompe/forms_suppression.html', context)




def suppression_piece(request, pk):
    pieces = PiecesPompe.objects.get(pk=pk)
    if request.method == "POST":
        pieces.delete()
        return redirect("/pompe/pieces")

    context = {'item': pieces}
    return render(request, 'pompe/suppression_piece.html', context)



def suppression_huile(request, pk):
    huiles = Huile.objects.get(pk=pk)
    if request.method == "POST":
        huiles.delete()
        return redirect("/pompe/huiles")

    context = {'item': huiles}
    return render(request, 'pompe/suppression_huile.html', context)


def suppression_kit(request, pk):
    kits = Kit.objects.get(pk=pk)
    if request.method == "POST":
        kits.delete()
        return redirect("/pompe/kit")

    context = {'item': kits}
    return render(request, 'pompe/suppression_kit.html', context)
