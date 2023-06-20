"""
View of Visiopompe project centralized in views.py
"""

from datetime import timedelta
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
    """
    Fonction qui permet l'affichage de compteurs d'états généraux des pompes, de leurs types et leurs natures.
    Une option a été ajoutée pour un affichage spécifique en fonction des étages de l'UMR 6521.

    Args:
        request: la requête d'affichage des pompes

    Returns:
          dashboard.html : la page de la dashboard avec les différents objets filtrés pour l'affichage des compteurs
    """
    dash_pompes = StockPompe.objects.all()

    # general setting for dashboard

    p_all = dash_pompes.count()
    p_valide = dash_pompes.filter(statut='A').count()
    p_stock = dash_pompes.filter(statut='S').count()
    p_hs = dash_pompes.filter(statut='P').count()
    p_rep = dash_pompes.filter(statut='R').count()
    p_atex = dash_pompes.filter(atex='1').count()

    #: special to UMR 6521. Base on technologie of pump. #

    p_palette = dash_pompes.filter(pompe__technologie__nom__icontains='palette').count()
    p_membrane = dash_pompes.filter(pompe__technologie__nom__icontains='membrane').count()
    p_seche = dash_pompes.filter(pompe__technologie__cara2__icontains='seche').count()

    # special to UMR 6521 by stair. #
    p_etage_1 = dash_pompes.filter(etage__nom__icontains='1').count()
    p_etage_2 = dash_pompes.filter(etage__nom__icontains='2').count()
    p_etage_3 = dash_pompes.filter(etage__nom__icontains='3').count()

    # special to UMR6521 by teams. #
    p_ciel = dash_pompes.filter(equipe__sigle__icontains='ciel').count()
    p_spectre = dash_pompes.filter(equipe__sigle__icontains='spectre').count()
    p_cosm = dash_pompes.filter(equipe__sigle__icontains='cosm').count()
    p_umr = dash_pompes.filter(equipe__sigle__icontains='umr').count()

    context = {'p_all': p_all,'p_valide': p_valide, 'p_stock': p_stock,'p_hs': p_hs,'p_rep': p_rep,
               'p_atex': p_atex,
                'p_palette': p_palette, 'p_membrane':p_membrane, 'p_seche':p_seche,
               'p_etage_1':p_etage_1, 'p_etage_2': p_etage_2, 'p_etage_3':p_etage_3,
               'p_ciel':p_ciel, 'p_spectre': p_spectre, 'p_cosm':p_cosm, 'p_umr': p_umr,
               }
    return render(request, 'pompe/dashboard.html', context)


def equipe(request):
    """
    Fonction d'affichage des équipes et du formulaire de soumission de création d'un nouvelle équipe
    Args:
        request: l'élément soumis pour l'execution du formulaire de création d'une équipe

    Returns:
        equipe/html : la page d'affichage des équipes enregistrées et le formulaire vide.
    """
    equipes = ModelEquipe.objects.all().order_by('sigle')

    if request.method == "POST":
        form = Equipeform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/dashboard/equipe')
    else:
        form = Equipeform()
    return render(request, 'pompe/equipe.html', {'equipes': equipes, 'form': form})


def update_equipe(request, pk):
    """
    Fonction de mise à jour d'un équipe existante.

    Args:
        request : l'objet soumis en requête post
        pk : l'identifiant de l'équipe en base de données

    Returns:
          equipe.html : la page équipe avec les informations mise à jour sinon la page du formulaire de
          soumission avec les erreurs.

    """
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
    """
    Fonction de suppression d'une équipe en base de données.

    Args:
        request: l'objet soumis en requête POST
        pk : l'identifiant de l'équipe à supprimer.

    Returns:
        equipe.html : la page équipe mise à jour.

    """
    queryset = get_object_or_404(ModelEquipe, pk=pk)
    if request.method == "POST":
        queryset.delete()
        return redirect('/dashboard/equipe')

    return render(request, 'pompe/equipe.html', {'queryset': queryset})

## fabriquant
def fabriquant(request):
    fabriquants = Fabriquant.objects.all().order_by('nom')

    if request.method == "POST"  and 'fabriquant_form' in request.POST:
        form = Fabriquantform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/fabriquants')
    else:
        form = Fabriquantform()

    context = {'fabriquants': fabriquants, 'form':form}
    return render(request, 'pompe/fabriquant.html', context)

def update_fabriquant(request, pk):
    fabriquants = get_object_or_404(Fabriquant, pk=pk)
    if request.method == "POST":
        form = ModifFabriquantForm(request.POST, request.FILES, instance=fabriquants)
        if form.is_valid():
            form.save()
        return redirect('/fabriquants')
    else:
        form = ModifFabriquantForm(instance=fabriquants)
    return render(request, 'pompe/forms.html', {'form': form})

def delete_fabriquant(request, pk):
    fabriquants = get_object_or_404(Fabriquant, pk=pk)
    if request.method == "POST":
        fabriquants.delete()
        return redirect("/fabriquants")

    context = {'fabriquants': fabriquants}
    return render(request, 'pompe/fabriquant.html', context)

## lieux
def piece(request):
    pieces = Piece.objects.all().order_by('nom')
    sites = Site.objects.all().order_by('nom')
    batiments = Batiment.objects.all().order_by('nom')
    etages = Etage.objects.all().order_by('nom')

    if request.method == "POST":
        form = Siteform(request.POST, request.FILES)
        form2 = Batimentform(request.POST, request.FILES)
        form3 = Etageform(request.POST, request.FILES)
        form4 = Pieceform(request.POST, request.FILES)
        if form.is_valid() and 'site_form' in request.POST:
            form.save()

        elif form2.is_valid() and 'batiment_form' in request.POST:
            form2.save()

        elif form3.is_valid() and 'etage_form' in request.POST:
            form3.save()

        elif form4.is_valid() and 'piece_form' in request.POST:
            form4.save()
        return redirect('/dashboard/lieux')
    else:
        form = Siteform()
        form2 = Batimentform()
        form3 = Etageform()
        form4 = Pieceform()

    context = {'pieces': pieces,
               'sites': sites,
               'batiments' : batiments,
               'etages' : etages,
               'form': form, 'form2': form2, 'form3': form3, 'form4': form4}
    return render(request, 'pompe/lieux.html', context)

def update_piece(request, pk):
    pieces = get_object_or_404(Piece, pk=pk)
    if request.method == "POST":
        form = ModifPieceForm(request.POST, instance=pieces)
        if form.is_valid():
            form.save()
        return redirect('/dashboard/lieux')
    else:
        form = ModifPieceForm(instance=pieces)
    return render(request, 'pompe/forms.html', {'form': form})

def delete_piece(request, pk):
    queryset = get_object_or_404(Piece, pk=pk)
    if request.method == "POST":
        queryset.delete()
        return redirect('/dashboard/lieux')

    return render(request, 'pompe/lieux.html', {'queryset': queryset})

def update_site(request, pk):
    sites = get_object_or_404(Site, pk=pk)
    if request.method == "POST":
        form = ModifSiteForm(request.POST, instance=sites)
        if form.is_valid():
            form.save()
        return redirect('/dashboard/lieux')
    else:
        form = ModifSiteForm(instance=sites)
    return render(request, 'pompe/forms.html', {'form': form})

def delete_site(request, pk):
    queryset = get_object_or_404(Site, pk=pk)
    if request.method == "POST":
        queryset.delete()
        return redirect('/dashboard/lieux')

    return render(request, 'pompe/lieux.html', {'queryset': queryset})

def update_batiment(request, pk):
    batiments = get_object_or_404(Batiment, pk=pk)
    if request.method == "POST":
        form = ModifBatimentForm(request.POST, instance=batiments)
        if form.is_valid():
            form.save()
        return redirect('/dashboard/lieux')
    else:
        form = ModifBatimentForm(instance=batiments)
    return render(request, 'pompe/forms.html', {'form': form})

def delete_batiment(request, pk):
    queryset2 = get_object_or_404(Batiment, pk=pk)
    if request.method == "POST":
        queryset2.delete()
        return redirect('/dashboard/lieux')

    return render(request, 'pompe/lieux.html', {'queryset2': queryset2})

def update_etage(request, pk):
    etages = get_object_or_404(Etage, pk=pk)
    if request.method == "POST":
        form = ModifEtageForm(request.POST, instance=etages)
        if form.is_valid():
            form.save()
        return redirect('/dashboard/lieux')
    else:
        form = ModifEtageForm(instance=etages)
    return render(request, 'pompe/forms.html', {'form': form})

def delete_etage(request, pk):
    queryset3 = get_object_or_404(Etage, pk=pk)
    if request.method == "POST":
        queryset3.delete()
        return redirect('/dashboard/lieux')

    return render(request, 'pompe/lieux.html', {'queryset3': queryset3})

# stocks pompes
def pompe(request):
    s_pompes = StockPompe.objects.all().order_by('mise_en_service')
    filterpompe = PompeStockFilter(request.GET, queryset=s_pompes)
    s_pompes = filterpompe.qs
    current_date = datetime.now().date()
    warning_date = current_date + timedelta(days=7)

    context = {'s_pompes': s_pompes,
               'current_date': current_date,
               'warning_date': warning_date,
               'filterpompe': filterpompe,
                }
    return render(request, 'pompe/pompe.html', context)

def historique(request, pk):
    historic = StockHistory.objects.filter(stockpump=pk).order_by('-date_historique')

    return render(request, 'pompe/historique.html', {'historic': historic})

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
        form = ModifStockPompeForm(request.POST,  instance=s_pompes)
        if form.is_valid():
            form.save()
        return redirect('/pompes')
    else:
        form = ModifStockPompeForm(instance=s_pompes)
    return render(request, 'pompe/forms.html', {'form': form})

def delete_stockpompe(request, pk):
    queryset = get_object_or_404(StockPompe, pk=pk)
    if request.method == "POST":
        queryset.delete()
        return redirect('/pompes')

    return render(request,'pompe/pompe.html', {'queryset':queryset})

#fiche modele des pompes
def fichepompe(request):
    m_pompes = ModelePompe.objects.all().order_by('nom')
    technos = TechnologiePompe.objects.all().order_by('nom')

    if request.method == "POST":
        form = ModelPompeform(request.POST, request.FILES)
        form2 = Technologieform(request.POST, request.FILES)

        if form.is_valid() and 'fiche_form' in request.POST:
            form.save()

        elif form2.is_valid() and 'techno_form' in request.POST:
            form2.save()

        return redirect('/fichepompe')
    else:
        form = ModelPompeform()
        form2 = Technologieform()

    context = {'m_pompe': m_pompes, 'technos': technos,'form': form, 'form2': form2}
    return render(request, 'pompe/fiche_pompe.html', context)

def update_fichepompe(request, pk):
    m_pompes = get_object_or_404(ModelePompe, pk=pk)
    if request.method == "POST":
        form = ModifModelPompeForm(request.POST, request.FILES, instance=m_pompes)
        if form.is_valid():
            form.save()
            return redirect('/fichepompe')
    else:
        form = ModifModelPompeForm(instance=m_pompes)
    return render(request, 'pompe/forms.html', {'form': form})

def delete_fichepompe(request, pk):
    queryset = get_object_or_404(ModelePompe, pk=pk)
    if request.method == "POST":
        queryset.delete()
        return redirect('/fichepompe')

    context = {'queryset': queryset}
    return render(request, 'pompe/fiche_pompe.html', context)

def update_techno(request, pk):
    technos = get_object_or_404(TechnologiePompe, pk=pk)
    if request.method == "POST":
        form = ModifTechnoForm(request.POST, instance=technos)
        if form.is_valid():
            form.save()
            return redirect('/fichepompe')
    else:
        form = ModifTechnoForm(instance=technos)
    return render(request, 'pompe/forms.html', {'form': form})

def delete_techno(request, pk):
    queryset1 = get_object_or_404(TechnologiePompe, pk=pk)
    if request.method == "POST":
        queryset1.delete()
        return redirect('/fichepompe')

    context = {'queryset1': queryset1}
    return render(request, 'pompe/fiche_pompe.html', context)

# inventaire et tutelle
def inventaire(request):
    inventaires = Inventaire.objects.all().order_by('numero')
    tutelles = Tutelle.objects.all().order_by('nom')

    if request.method == "POST":
        form = Inventaireform(request.POST)
        form2 = Tutelleform(request.POST)

        if form2.is_valid() and 'tutelle_form' in request.POST:
            form2.save()

        elif form.is_valid() and 'inventaire_form' in request.POST:
            form.save()

        return redirect('/inventaire')
    else:
        form = Inventaireform()
        form2 = Tutelleform()

    context = {'inventaires': inventaires, 'tutelles': tutelles, 'form': form, 'form2': form2}
    return render(request, 'pompe/inventaire.html', context)

def update_inventaire(request, pk):
    inventaires = get_object_or_404(Inventaire, pk=pk)

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
    if request.method == "POST":
        queryset.delete()
        return redirect('/inventaire')

    return render(request, 'pompe/inventaire.html', {'queryset': queryset})

def delete_tutelle(request, pk):
    queryset1 = get_object_or_404(Tutelle, pk=pk)
    if request.method == "POST":
        queryset1.delete()
        return redirect('/inventaire')

    return render(request, 'pompe/inventaire.html', {'queryset1': queryset1})

# pieces detachées
def pdetache(request):
    pieces = PiecesPompe.objects.all().order_by('nom')
    return render(request, 'pompe/piece.html', {'pieces': pieces})

def add_pdetache(request):
    if request.method == "POST":
        form = PiecePompeform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/pieces_detaches')
    else:
        form = PiecePompeform()
    return render(request, 'pompe/forms.html', {'form': form})

def update_pdetache(request, pk):
    pdetaches = get_object_or_404(PiecesPompe, pk=pk)

    if request.method == "POST":
        form = ModifPiecePompeForm(request.POST, request.FILES, instance=pdetaches)
        if form.is_valid():
            form.save()
            return redirect('/pieces_detaches')
    else:
        form = ModifPiecePompeForm(instance=pdetaches)
    return render(request, 'pompe/forms.html', {'form': form})

def delete_pdetache(request, pk):
    pieces = get_object_or_404(PiecesPompe, pk=pk)
    if request.method == "POST":
        pieces.delete()
        return redirect('/pieces_detaches')
    return render(request, 'pompe/piece.html', {'pieces': pieces})

# huile
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
        form = ModifHuileForm(request.POST, request.FILES, instance=huiles)
        if form.is_valid():
            form.save()
            return redirect('/huiles')
    else:
        form = ModifHuileForm(instance=huiles)
    return render(request, 'pompe/forms.html', {'form': form})

def delete_huile(request, pk):
    huiles = get_object_or_404(Huile, pk=pk)
    if request.method == "POST":
        huiles.delete()
        return redirect('/huiles')
    return render(request, 'pompe/huile.html', {'huiles': huiles})

# kit de maintenance
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
        form = ModifKitForm(request.POST, request.FILES, instance=kits)
        if form.is_valid():
            form.save()
            return redirect('/kits')
    else:
        form = ModifKitForm(instance=kits)
    return render(request, 'pompe/forms.html', {'form': form})

def delete_kit(request, pk):
    kits = get_object_or_404(Kit, pk=pk)
    if request.method == "POST":
        kits.delete()
        return redirect('/kits')
    return render(request, 'pompe/kit.html', {'kits': kits})

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
        form = ModifDocForm(request.POST, request.FILES, instance=docs)
        if form.is_valid():
            form.save()
            return redirect('/docs')
    else:
        form = ModifDocForm(instance=docs)
    return render(request, 'pompe/forms.html', {'form': form})

def delete_doc(request, pk):
    docs = get_object_or_404(Doc, pk=pk)
    if request.method == "POST":
        docs.delete()
        return redirect('/docs')
    return render(request, 'pompe/doc.html', {'docs': docs})

