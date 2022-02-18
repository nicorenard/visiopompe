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

# dashboard
def dashboard(request):
    dash_pompes = StockPompe.objects.all()
    p_all = dash_pompes.count()
    p_valide = dash_pompes.filter(statut='A').count()
    p_stock = dash_pompes.filter(statut='S').count()
    p_hs = dash_pompes.filter(statut='P').count()
    p_rep = dash_pompes.filter(statut='R').count()
    p_etage = dash_pompes.filter(piece_id= 0).count()

    context = {'p_all': p_all,'p_valide': p_valide, 'p_stock': p_stock,'p_hs': p_hs,'p_rep': p_rep,
               'p_etage' : p_etage,
    }
    return render(request, 'pompe/dashboard.html', context)

## equipe
def equipe(request):
    equipes = ModelEquipe.objects.all().order_by('sigle')
    form = Equipeform()

    if request.method == "POST":
        form = Equipeform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/dashboard/equipe')
    else:
        form = Equipeform()
    return render(request, 'pompe/equipe.html', {'equipes': equipes, 'form': form})

def update_equipe(request, pk):
    equipes = get_object_or_404(ModelEquipe, pk=pk)
    if request.method == "POST":
        form = ModifEquipeForm(request.POST, instance=equipes)
        if form.is_valid():
            form.save()
        return redirect('/dashboard/equipe')
    else:
        form = ModifEquipeForm(instance=equipes)
    return render(request, 'pompe/forms.html', {'form': form})

def delete_equipe(request, pk):
    queryset = get_object_or_404(ModelEquipe, pk=pk)
    queryset.delete()
    return redirect('/dashboard/equipe')
## fabriquant
def fabriquant(request):
    fabriquants = Fabriquant.objects.all().order_by('nom')
    return render(request, 'pompe/fabriquant.html', {'fabriquants': fabriquants})

def add_fabriquant(request):
    if request.method == "POST":
        form = Fabriquantform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/fabriquants')
    else:
        form = Fabriquantform()
    return render(request, 'pompe/forms.html', {'form': form})

def update_fabriquant(request, pk):
    fabriquants = get_object_or_404(Fabriquant, pk=pk)
    if request.method == "POST":
        form = ModifFabriquantForm(request.POST, instance=fabriquants)
        if form.is_valid():
            form.save()
        return redirect('/fabriquants')
    else:
        form = ModifFabriquantForm(instance=fabriquants)
    return render(request, 'pompe/forms.html', {'form': form})

def delete_fabriquant(request, pk):
    queryset = get_object_or_404(Fabriquant, pk=pk)
    queryset.delete()
    return redirect('/fabriquants')

## lieux
def piece(request):
    pieces = Piece.objects.all().order_by('nom')
    form = Siteform()
    form2 = Batimentform()
    form3 = Etageform()
    form4 = Pieceform()

    if request.method == "POST":
        form = Siteform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('pompe/lieux')
    else:
        form = Siteform()

    if request.method == "POST":
        form2 = Batimentform(request.POST, request.FILES)
        if form2.is_valid():
            form2.save()
        return redirect('pompe/lieux')
    else:
        form2 = Batimentform()

    if request.method == "POST":
        form3 = Etageform(request.POST, request.FILES)
        if form3.is_valid():
            form3.save()
        return redirect('pompe/lieux')
    else:
        form3 = Etageform()

    if request.method == "POST":
        form4 = Pieceform(request.POST, request.FILES)
        if form4.is_valid():
            form4.save()
        return redirect('pompe/lieux')
    else:
        form4 = Pieceform()

    context = {'pieces': pieces, 'form': form, 'form2':form2, 'form3':form3, 'form4':form4}
    return render(request, 'pompe/lieux.html', context)

def update_piece(request, pk):
    pieces = get_object_or_404(Fabriquant, pk=pk)
    if request.method == "POST":
        form = ModifPieceForm(request.POST, instance=pieces)
        if form.is_valid():
            form.save()
        return redirect('pompe/lieux')
    else:
        form = ModifPieceForm(instance=pieces)
    return render(request, 'pompe/forms.html', {'form': form})

def delete_piece(request, pk):
    queryset = get_object_or_404(Piece, pk=pk)
    queryset.delete()
    return redirect('/pompe/lieux')
# fiche stocks pompes
def pompe(request):
    s_pompes = StockPompe.objects.all().order_by('mise_en_service')
    filterpompe = PompeStockFilter(request.GET, queryset=s_pompes)
    s_pompes = filterpompe.qs
    current_date = datetime.date.today()
    warning_date = current_date + datetime.timedelta(days=7)

    context = {'s_pompes': s_pompes,
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
        return redirect('/pompes')
    else:
        form = StockPompeform()
    return render(request, 'pompe/forms.html', {'form': form})

def update_stockpompe(request, pk):
    s_pompes = get_object_or_404(StockPompe, pk=pk)
    if request.method == "POST":
        form = ModifStockPompeForm(request.POST, instance=s_pompes)
        if form.is_valid():
            form.save()
        return redirect('/pompes')
    else:
        form = ModifStockPompeForm(instance=s_pompes)
    return render(request, 'pompe/forms.html', {'form': form})

def delete_stockpompe(request, pk):
    s_pompes = get_object_or_404(StockPompe, pk=pk)
    s_pompes.delete()
    return redirect('/pompes')

#fiche modele des pompes
def fichepompe(request):
    m_pompes = ModelePompe.objects.all().order_by('nom')
    context = {'m_pompe': m_pompes}
    return render(request, 'pompe/fiche_pompe.html', context)

def add_fichepompe(request):
    if request.method == "POST":
        form = ModelPompeform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/fichepompe')
    else:
        form = ModelPompeform()
    return render(request, 'pompe/forms.html', {'form': form})

def update_fichepompe(request, pk):
    m_pompes = get_object_or_404(StockPompe, pk=pk)
    if request.method == "POST":
        form = ModifModelPompeForm(request.POST, instance=m_pompes)
        if form.is_valid():
            form.save()
            return redirect('/fiche_pompe')
    else:
        form = ModifModelPompeForm(instance=m_pompes)
    return render(request, 'pompe/forms.html', {'form': form})

def delete_fichepompe(request, pk):
    fiches = get_object_or_404(StockPompe, pk=pk)
    fiches.delete()
    return redirect('/fichepompe')

#inventaire et tutelle
def inventaire(request):
    inventaires = Inventaire.objects.all().order_by('numero')
    tutelles = Tutelle.objects.all().order_by('nom')
    context = {'inventaires': inventaires, 'tutelles': tutelles }
    return render(request, 'pompe/inventaire.html', context)

def add_inventaire(request):
    if request.method == "POST":
        form = Inventaireform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/inventaire')
    else:
        form = Inventaireform()
    return render(request, 'pompe/forms.html', {'form': form})

def update_inventaire(request, pk):
    inventaires = get_object_or_404(StockPompe, pk=pk)

    if request.method == "POST":
        form = ModifInventaireForm(request.POST, instance=inventaires)
        if form.is_valid():
            form.save()
            return redirect('/inventaire')
    else:
        form = ModifInventaireForm(instance=inventaires)
    return render(request, 'pompe/forms.html', {'form': form})

def delete_inventaire(request, pk):
    queryset = get_object_or_404(Inventaire, pk=pk)
    queryset.delete()
    return redirect('/inventaire')

#pieces detachées
def pdetache(request):
    pieces = PiecesPompe.objects.all().order_by('nom')
    return render(request, 'pompe/piece.html', {'pieces': pieces})

def add_pdetache(request):
    if request.method == "POST":
        form = PiecePompeform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/pdetache')
    else:
        form = PiecePompeform()
    return render(request, 'pompe/forms.html', {'form': form})

def update_pdetache(request, pk):
    pdetaches = get_object_or_404(PiecesPompe, pk=pk)

    if request.method == "POST":
        form = ModifPiecePompeForm(request.POST, instance=pdetaches)
        if form.is_valid():
            form.save()
            return redirect('/pdetache')
    else:
        form = ModifPiecePompeForm(instance=pdetaches)
    return render(request, 'pompe/forms.html', {'form': form})

def delete_pdetache(request, pk):
    pieces = get_object_or_404(PiecesPompe, pk=pk)
    pieces.delete()
    return redirect('/pieces_detaches')

#huile
def huile(request):
    huiles = Huile.objects.all().order_by('nom')
    return render(request, 'pompe/huile.html', {'huiles': huiles})

def add_huile(request):
    if request.method == "POST":
        form = Huileform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/huiles')
    else:
        form = Huileform()
    return render(request, 'pompe/forms.html', {'form': form})

def update_huile(request, pk):
    huiles = get_object_or_404(Huile, pk=pk)

    if request.method == "POST":
        form = ModifHuileForm(request.POST, instance=huiles)
        if form.is_valid():
            form.save()
            return redirect('/huiles')
    else:
        form = ModifHuileForm(instance=huiles)
    return render(request, 'pompe/forms.html', {'form': form})

def delete_huile(request, pk):
    huiles = get_object_or_404(Huile, pk=pk)
    huiles.delete()
    return redirect('/huiles')

#kit de maintenance
def kit(request):
    kits = Kit.objects.all().order_by('nom')
    return render(request, 'pompe/kit.html', {'kits': kits})

def add_kit(request):
    if request.method == "POST":
        form = Kitform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/kits')
    else:
        form = Kitform()
    return render(request, 'pompe/forms.html', {'form': form})

def update_kit(request, pk):
    kits = get_object_or_404(Kit, pk=pk)
    if request.method == "POST":
        form = ModifKitForm(request.POST, instance=kits)
        if form.is_valid():
            form.save()
            return redirect('/kits')
    else:
        form = ModifKitForm(instance=kits)
    return render(request, 'pompe/forms.html', {'form': form})

def delete_kit(request, pk):
    kits = get_object_or_404(Kit, pk=pk)
    kits.delete()
    return redirect('/kits')

# Documentations
def doc(request):
    docs = Doc.objects.all().order_by('nom')
    context = {'docs': docs}
    return render(request, 'pompe/doc.html', context)

def add_doc(request):
    if request.method == "POST":
        form = Docform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/docs')
    else:
        form = Docform()
    return render(request, 'pompe/forms.html', {'form': form})

def update_doc(request, pk):
    docs = get_object_or_404(Doc, pk=pk)

    if request.method == "POST":
        form = ModifDocForm(request.POST, instance=docs)
        if form.is_valid():
            form.save()
            return redirect('/docs')
    else:
        form = ModifDocForm(instance=docs)
    return render(request, 'pompe/forms.html', {'form': form})

def delete_doc(request, pk):
    docs = get_object_or_404(Doc, pk=pk)
    docs.delete()
    return redirect('/docs')


