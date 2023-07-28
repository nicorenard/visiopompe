"""
Les vues de l'applications centralisée dans le fichier views.py
"""
import os.path
import xlwt
from datetime import timedelta
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.http import HttpResponse


from .filters import PompeStockFilter
from .forms import *
from .models import *


def index(request):
    """
    Fonction d'affichage de la page d'accueil du site.
    Args:
        request: l'objet POST reçu en paramètre pour afficher la page dédiée.

    Returns:
        index.html : la page d'acceuil retournée.
    """

    return render(request, 'pompe/index.html')


# dashboard

def dashboard(request):
    """
    Fonction qui permet l'affichage de compteurs d'états généraux des pompes, de leurs types et leurs natures.
    Une option a été ajoutée pour un affichage spécifique en fonction des étages de l'UMR 6521, aux équipes et aux types
    de technologie de vide.

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

    context = {'p_all': p_all, 
               'p_valide': p_valide,
               'p_stock': p_stock,
               'p_hs': p_hs,
               'p_rep': p_rep,
               'p_atex': p_atex
               }
    return render(request, 'pompe/dashboard.html', context)


def equipe(request):
    """
    Fonction d'affichage des équipes et du formulaire de soumission de création d'un nouvelle équipe
    Args:
        request: l'élément soumis pour l'execution du formulaire de création d'une équipe

    Returns:
        equipe.html : la page d'affichage des équipes enregistrées et le formulaire vide.
    """
    equipes = ModelEquipe.objects.all().order_by('sigle')

    if request.method == "POST":
        form = Equipeform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            msg_succes = f'Une nouvelle équipe a bien été créée.'
            url = reverse('pompe:equipe') + '?msg_succes=' + msg_succes

        else:
            msg_erreur = "L'ajout n'a pas pu être fait."
            url = reverse('pompe:equipe') + '?msg_erreur=' + msg_erreur
        return redirect(url)
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
            msg_succes = f'L\'équipe a bien été mise à jour.'
            url = reverse('pompe:equipe') + '?msg_succes=' + msg_succes

        else:
            msg_erreur = "La modification de l'équipe n'a pas été faites."
            url = reverse('pompe:equipe') + '?msg_erreur=' + msg_erreur
        return redirect(url)

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
        msg_succes = f'L\'équipe a bien été supprimée.'
        url = reverse('pompe:equipe') + '?msg_succes=' + msg_succes
        return redirect(url)

    context = {
        'queryset': queryset
    }

    return render(request, 'pompe/equipe.html', context)


## fabriquant
def fabriquant(request):
    """
    Fonction d'affichage des fabriquants et du formulaire de soumission de création d'un nouveau fabriquant
    Args:
        request: l'élément soumis pour l'execution du formulaire de création d'un fabriquant

    Returns:
        fabriquant.html : la page d'affichage des fabriquants enregistres et le formulaire vide.
    """
    fabriquants = Fabriquant.objects.all().order_by('nom')

    if request.method == "POST" and 'fabriquant_form' in request.POST:
        form = Fabriquantform(request.POST, request.FILES)
        if form.is_valid():
            fabriquant = form.save(commit=False)
            cleaned_data = form.cleaned_data
            if cleaned_data:
                fabriquant.save()
            msg_succes = f'Une nouvelle fiche fabriquant a bien été créée.'
            url = reverse('pompe:fabriquant') + '?msg_succes=' + msg_succes

        else:
            msg_erreur = "L'ajout n'a pas pu être fait."
            url = reverse('pompe:fabriquant') + '?msg_erreur=' + msg_erreur
        return redirect(url)
    else:
        form = Fabriquantform()

    msg_succes = request.GET.get('msg_succes', '')
    msg_erreur = request.GET.get('msg_erreur', '')
    msg_warning = request.GET.get('msg_warning', '')

    context = {
        'fabriquants': fabriquants,
        'form': form,
        'msg_warning': msg_warning,
        'msg_erreur': msg_erreur,
        'msg_succes': msg_succes,
    }
    return render(request, 'pompe/fabriquant.html', context)


def update_fabriquant(request, pk):
    """
    Fonction de mise à jour d'un fabriquant existant.

    Args:
        request : l'objet soumis en requête post
        pk : l'identifiant du fabriquant en base de données

    Returns:
          fabriquant.html : la page des fabriquants avec les informations de mise à jour sinon la page du formulaire de
          soumission avec les erreurs.

    """
    fabriquants = get_object_or_404(Fabriquant, pk=pk)
    if request.method == "POST":
        form = ModifFabriquantForm(request.POST, request.FILES, instance=fabriquants)
        if form.is_valid():
            form.save()
            msg_succes = f'La fiche fabriquant a bien été mise à jour.'
            url = reverse('pompe:fabriquant') + '?msg_succes=' + msg_succes
        else:
            msg_erreur = f'La fiche fabriquant n\'a pas été mis à jour.'
            url = reverse('pompe:fabriquant') + '?msg_erreur=' + msg_erreur

        return redirect(url)
    else:
        form = ModifFabriquantForm(instance=fabriquants)
    return render(request, 'pompe/forms.html', {'form': form})


def delete_fabriquant(request, pk):
    """
    Fonction de suppression d'un fabriquant en base de données.

    Args:
        request: l'objet soumis en requête POST
        pk : l'identifiant du fabriquant à supprimer.

    Returns:
        fabriquant.html : la page fabriquant mise à jour.

    """
    queryset = get_object_or_404(Fabriquant, pk=pk)
    if request.method == "POST":

        # suppression des médias = logos
        logomax_path = queryset.logo_max.path
        logomax_parent_directory = os.path.dirname(logomax_path)
        logomini_path = queryset.logo_mini.path
        logomini_parent_directory = os.path.dirname(logomini_path)

        if os.path.exists(logomax_path):
            os.remove(logomax_path)
            # si dossier vide, on retire celui_ci du serveur
            if len(os.listdir(logomax_parent_directory)) == 0:
                os.rmdir(logomax_parent_directory)
        if os.path.exists(logomini_path):
            os.remove(logomini_path)
            # si dossier vide, on retire celui_ci du serveur
            if len(os.listdir(logomini_parent_directory)) == 0:
                os.rmdir(logomini_parent_directory)

        queryset.delete()
        msg_succes = f'Le fabriquant a bien été supprimé.'
        url = reverse('pompe:fabriquant') + '?msg_succes=' + msg_succes
        return redirect(url)

    context = {'fabriquants': queryset}
    return render(request, 'pompe/fabriquant.html', context)


## lieux
def piece(request):
    """
    Fonction d'affichage et de création, d'une salle ou pièce (lieux), étages, bâtiment et site en base de données.

    Args:
        request: l'objet soumis en requête POST

    Returns:
        lieux.html : la page lieux mise à jour.

    """
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
            msg_succes = f'Un site a bien été créé.'
            url = reverse('pompe:lieux') + '?msg_succes=' + msg_succes

        elif form2.is_valid() and 'batiment_form' in request.POST:
            form2.save()
            msg_succes = f'Un bâtiment a bien été créé.'
            url = reverse('pompe:lieux') + '?msg_succes=' + msg_succes

        elif form3.is_valid() and 'etage_form' in request.POST:
            form3.save()
            msg_succes = f'Un étage a bien été créé.'
            url = reverse('pompe:lieux') + '?msg_succes=' + msg_succes

        elif form4.is_valid() and 'piece_form' in request.POST:
            form4.save()
            msg_succes = f'Une pièce a bien été créée.'
            url = reverse('pompe:lieux') + '?msg_succes=' + msg_succes

        else:
            msg_erreur = "L'ajout n'a pas pu être fait."
            url = reverse('pompe:lieux') + '?msg_erreur=' + msg_erreur
        return redirect(url)

    else:
        form = Siteform()
        form2 = Batimentform()
        form3 = Etageform()
        form4 = Pieceform()

    msg_succes = request.GET.get('msg_succes', '')
    msg_erreur = request.GET.get('msg_erreur', '')
    msg_warning = request.GET.get('msg_warning', '')

    context = {'pieces': pieces,
               'sites': sites,
               'batiments': batiments,
               'etages': etages,
               'form': form,
               'form2': form2,
               'form3': form3,
               'form4': form4,
               'msg_warning': msg_warning,
               'msg_erreur': msg_erreur,
               'msg_succes': msg_succes,
               }
    return render(request, 'pompe/lieux.html', context)


def update_piece(request, pk):
    """
    Fonction de modification d'une salle ou pièce (lieux) en base de données.

    Args:
        request: l'objet soumis en requête POST
        pk : l'identifiant de la salle ou pièce à modifier.

    Returns:
        lieux.html : la page lieux mise à jour.

    """
    pieces = get_object_or_404(Piece, pk=pk)
    if request.method == "POST":
        form = ModifPieceForm(request.POST, instance=pieces)
        if form.is_valid():
            form.save()
            msg_succes = f'La pièce a bien été mise à jour.'
            url = reverse('pompe:lieux') + '?msg_succes=' + msg_succes
        else:
            msg_erreur = f'La pièce n\'a pas été mise à jour.'
            url = reverse('pompe:lieux') + '?msg_erreur=' + msg_erreur

        return redirect(url)
    else:
        form = ModifPieceForm(instance=pieces)

    context = {
        'form': form
    }
    return render(request, 'pompe/forms.html', context)


def delete_piece(request, pk):
    """
    Fonction de suppression d'une salle ou pièce (lieux) en base de données.

    Args:
        request: l'objet soumis en requête POST
        pk : l'identifiant de la salle ou pièce à supprimer.

    Returns:
        lieux.html : la page lieux mise à jour.

    """
    queryset = get_object_or_404(Piece, pk=pk)
    if request.method == "POST":
        queryset.delete()
        msg_succes = f'La pièce a bien été supprimé.'
        url = reverse('pompe:lieux') + '?msg_succes=' + msg_succes
        return redirect(url)

    context = {
        'queryset': queryset
    }

    return render(request, 'pompe/lieux.html', context)


def update_site(request, pk):
    """
    Fonction de modification d'un site (lieu) en base de données.

    Args:
        request: l'objet soumis en requête POST
        pk : l'identifiant du site à modifier.

    Returns:
        lieux.html : la page lieux mise à jour.

    """
    sites = get_object_or_404(Site, pk=pk)
    if request.method == "POST":
        form = ModifSiteForm(request.POST, instance=sites)
        if form.is_valid():
            form.save()
            msg_succes = f'Le site a bien été mis à jour.'
            url = reverse('pompe:lieux') + '?msg_succes=' + msg_succes
        else:
            msg_erreur = f'Le site n\'a pas été mis à jour.'
            url = reverse('pompe:lieux') + '?msg_erreur=' + msg_erreur

        return redirect(url)

    else:
        form = ModifSiteForm(instance=sites)
    return render(request, 'pompe/forms.html', {'form': form})


def delete_site(request, pk):
    """
    Fonction de suppression d'un site (lieu) en base de données.

    Args:
        request: l'objet soumis en requête POST
        pk : l'identifiant du site à supprimer.

    Returns:
        lieux.html : la page lieu mise à jour.

    """
    queryset = get_object_or_404(Site, pk=pk)
    if request.method == "POST":
        queryset.delete()
        msg_succes = f'Le site a bien été supprimé.'
        url = reverse('pompe:lieux') + '?msg_succes=' + msg_succes
        return redirect(url)

    return render(request, 'pompe/lieux.html', {'queryset': queryset})


def update_batiment(request, pk):
    """
    Fonction de mise à jour d'un bâtiment (lieu) en base de données.

    Args:
        request: l'objet soumis en requête POST
        pk : l'identifiant du bâtiment à modifier.

    Returns:
        lieux.html : la page lieux mise à jour.

    """
    batiments = get_object_or_404(Batiment, pk=pk)
    if request.method == "POST":
        form = ModifBatimentForm(request.POST, instance=batiments)
        if form.is_valid():
            form.save()
            msg_succes = f'Le bâtiment a bien été mis à jour.'
            url = reverse('pompe:lieux') + '?msg_succes=' + msg_succes
        else:
            msg_erreur = f'Le bâtiment n\'a pas été mis à jour.'
            url = reverse('pompe:lieux') + '?msg_erreur=' + msg_erreur

        return redirect(url)

    else:
        form = ModifBatimentForm(instance=batiments)
    return render(request, 'pompe/forms.html', {'form': form})


def delete_batiment(request, pk):
    """
    Fonction de suppression d'un bâtiment (lieu) en base de données.

    Args:
        request: l'objet soumis en requête POST
        pk : l'identifiant du bâtiment à supprimer.

    Returns:
        lieux.html : la page lieu mise à jour.

    """
    queryset2 = get_object_or_404(Batiment, pk=pk)
    if request.method == "POST":
        queryset2.delete()
        msg_succes = f'Le bâtiment a bien été supprimé.'
        url = reverse('pompe:lieux') + '?msg_succes=' + msg_succes
        return redirect(url)

    return render(request, 'pompe/lieux.html', {'queryset2': queryset2})


def update_etage(request, pk):
    """
    Fonction de mise à jour d'un étage (lieu) en base de données.

    Args:
        request: l'objet soumis en requête POST
        pk : l'identifiant d'un étage' à modifier.

    Returns:
        lieux.html : la page lieux mise à jour.

    """
    etages = get_object_or_404(Etage, pk=pk)
    if request.method == "POST":
        form = ModifEtageForm(request.POST, instance=etages)
        if form.is_valid():
            form.save()
            msg_succes = f'L\'étage a bien été mis à jour.'
            url = reverse('pompe:lieux') + '?msg_succes=' + msg_succes
        else:
            msg_erreur = f'L\'étage n\'a pas été mis à jour.'
            url = reverse('pompe:lieux') + '?msg_erreur=' + msg_erreur

        return redirect(url)

    else:
        form = ModifEtageForm(instance=etages)
    return render(request, 'pompe/forms.html', {'form': form})


def delete_etage(request, pk):
    """
    Fonction de suppression d'un étage (lieu) en base de données.

    Args:
        request: l'objet soumis en requête POST
        pk : l'identifiant d'un étage' à supprimer.

    Returns:
        lieux.html : la page lieu mise à jour.

    """
    queryset3 = get_object_or_404(Etage, pk=pk)
    if request.method == "POST":
        queryset3.delete()
        msg_succes = f'L\'étage a bien été supprimé.'
        url = reverse('pompe:lieux') + '?msg_succes=' + msg_succes
        return redirect(url)

    return render(request, 'pompe/lieux.html', {'queryset3': queryset3})


# stocks pompes
def pompe(request):
    """
    Fonction d'affichage des stocks de pompes.

    Args:
        request: l'objet soumis en requête POST

    Returns:
        pompe.html : la page pompe.

    """
    s_pompes = StockPompe.objects.all().order_by('mise_en_service')
    filterpompe = PompeStockFilter(request.GET, queryset=s_pompes)
    s_pompes = filterpompe.qs
    current_date = datetime.now().date()
    warning_date = current_date + timedelta(days=7)

    msg_succes = request.GET.get('msg_succes', '')
    msg_erreur = request.GET.get('msg_erreur', '')
    msg_warning = request.GET.get('msg_warning', '')

    context = {'s_pompes': s_pompes,
               'current_date': current_date,
               'warning_date': warning_date,
               'filterpompe': filterpompe,
               'msg_warning': msg_warning,
               'msg_erreur': msg_erreur,
               'msg_succes': msg_succes,
               }
    return render(request, 'pompe/pompe.html', context)


def historique(request, pk):
    """
    Fonction d'affichage de l' historique d'un stock de pompe en base de données.

    Args:
        request: l'objet soumis en requête POST
        pk : l'identifiant du stock de pompe.

    Returns:
        pompe.html : la page pompe mise à jour.

    """
    historic = StockHistory.objects.filter(stockpump=pk).order_by('-date_historique')

    return render(request, 'pompe/historique.html', {'historic': historic})


def add_stockpompe(request):
    """
    Fonction d'ajout d'un stock de pompe en base de données.

    Args:
        request: l'objet soumis en requête POST

    Returns:
        pompe.html : la page pompe mise à jour.

    """
    if request.method == "POST":
        form = StockPompeform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            msg_succes = f'Le stock de pompe a bien été ajouté.'
            url = reverse('pompe:pompe') + '?msg_succes=' + msg_succes
        return redirect(url)
    else:
        form = StockPompeform()
    return render(request, 'pompe/forms.html', {'form': form})


def update_stockpompe(request, pk):
    """
    Fonction de mise à jour d'un stock de pompe en base de données.

    Args:
        request: l'objet soumis en requête POST
        pk : l'identifiant du stock de pompe à modifier.

    Returns:
        pompe.html : la page pompe mise à jour.

    """
    s_pompes = get_object_or_404(StockPompe, pk=pk)
    if request.method == "POST":
        form = ModifStockPompeForm(request.POST, instance=s_pompes)
        if form.is_valid():
            form.save()
            msg_succes = f'Le stock de pompe a bien été mis à jour.'
            url = reverse('pompe:pompe') + '?msg_succes=' + msg_succes
        return redirect(url)
    else:
        form = ModifStockPompeForm(instance=s_pompes)
    return render(request, 'pompe/forms.html', {'form': form})


def delete_stockpompe(request, pk):
    """
    Fonction de suppression d'un stock de pompe en base de données.

    Args:
        request: l'objet soumis en requête POST
        pk : l'identifiant du stock de pompe à supprimer.

    Returns:
        pompe.html : la page pompe mise à jour.

    """
    queryset = get_object_or_404(StockPompe, pk=pk)
    if request.method == "POST":
        queryset.delete()
        msg_succes = f'Le stock de pompe a bien été supprimé.'
        url = reverse('pompe:pompe') + '?msg_succes=' + msg_succes
        return redirect(url)

    return render(request, 'pompe/pompe.html', {'queryset': queryset})


# fiche modele des pompes
def fichepompe(request):
    """
    Fonction d'affichage des fiches de pompes et technologie du vide'.

    Args:
        request: l'objet soumis en requête POST

    Returns:
        fiche_pompe.html : la page des modèles de pompes et technologie.

    """
    m_pompes = ModelePompe.objects.all().order_by('nom')
    technos = TechnologiePompe.objects.all().order_by('nom')

    if request.method == "POST":
        form = ModelPompeform(request.POST, request.FILES)
        form2 = Technologieform(request.POST, request.FILES)

        if form.is_valid() and 'fiche_form' in request.POST:
            cleaned_data = form.cleaned_data
            if cleaned_data:
                form.save()
                msg_succes = f'La fiche modèle a bien été créée.'
                url = reverse('pompe:fiche_pompe') + '?msg_succes=' + msg_succes

        elif form2.is_valid() and 'techno_form' in request.POST:
            cleaned_data2 = form2.cleaned_data
            if cleaned_data2:
                form2.save()
                msg_succes = f'La technologie de vide a bien été créée.'
                url = reverse('pompe:fiche_pompe') + '?msg_succes=' + msg_succes
        else:
            msg_erreur = "L'ajout n'a pas pu être fait."
            url = reverse('pompe:fiche_pompe') + '?msg_erreur=' + msg_erreur
        return redirect(url)
    else:
        form = ModelPompeform()
        form2 = Technologieform()

    msg_succes = request.GET.get('msg_succes', '')
    msg_erreur = request.GET.get('msg_erreur', '')
    msg_warning = request.GET.get('msg_warning', '')

    context = {'m_pompe': m_pompes,
               'technos': technos,
               'form': form,
               'form2': form2,
               'msg_warning': msg_warning,
               'msg_erreur': msg_erreur,
               'msg_succes': msg_succes,

               }
    return render(request, 'pompe/fiche_pompe.html', context)


def update_fichepompe(request, pk):
    """
    Fonction de mise à jour d'une fiche modèle de pompe en base de données.

    Args:
        request: l'objet soumis en requête POST
        pk : l'identifiant d'une fiche à modifier.

    Returns:
        fiche_pompe.html : la page des modèles de pompes mise à jour.

    """
    m_pompes = get_object_or_404(ModelePompe, pk=pk)
    if request.method == "POST":
        form = ModifModelPompeForm(request.POST, request.FILES, instance=m_pompes)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            if cleaned_data:
                form.save()
                msg_succes = f'La fiche {pk} a bien été mise à jour.'
                url = reverse('pompe:fiche_pompe') + '?msg_succes=' + msg_succes

        return redirect(url)
    else:
        form = ModifModelPompeForm(instance=m_pompes)
    return render(request, 'pompe/forms.html', {'form': form})


def delete_fichepompe(request, pk):
    """
    Fonction de suppression d'une fiche modèle de pompe en base de données.

    Args:
        request: l'objet soumis en requête POST
        pk : l'identifiant d'une fiche à supprimer.

    Returns:
        fiche_pompe.html : la page des modèles de pompes mise à jour.

    """
    queryset = get_object_or_404(ModelePompe, pk=pk)
    if request.method == "POST":
        image_path = queryset.image.path
        image_parent_directory = os.path.dirname(image_path)
        if os.path.exists(image_path):
            os.remove(image_path)
            if len(os.listdir(image_parent_directory)) == 0:
                os.rmdir(image_parent_directory)
            queryset.delete()
            msg_succes = f'La fiche {pk} a bien été supprimé.'
            url = reverse('pompe:fiche_pompe') + '?msg_succes=' + msg_succes

        return redirect(url)

    context = {
        'queryset': queryset
    }
    return render(request, 'pompe/fiche_pompe.html', context)


def update_techno(request, pk):
    """
    Fonction de mise à jour d'une technologie de vide en base de données.

    Args:
        request: l'objet soumis en requête POST
        pk : l'identifiant d'une technologie à modifier.

    Returns:
        fiche_pompe.html : la page des modèles de pompe mise à jour.

    """
    technos = get_object_or_404(TechnologiePompe, pk=pk)
    if request.method == "POST":
        form = ModifTechnoForm(request.POST, instance=technos)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            if cleaned_data:
                form.save()
                msg_succes = f'La technologie de vide, {pk} a bien été mise à jour.'
                url = reverse('pompe:fiche_pompe') + '?msg_succes=' + msg_succes

            return redirect(url)
        else:
            msg_erreur = f'La technologie de vide, {pk} n\'a pas été mise à jour.'
            url = reverse('pompe:fiche_pompe') + '?msg_erreur=' + msg_erreur

        return redirect(url)

    else:
        form = ModifTechnoForm(instance=technos)
    return render(request, 'pompe/forms.html', {'form': form})


def delete_techno(request, pk):
    """
    Fonction de suppression d'une technologie de vide en base de données.

    Args:
        request: l'objet soumis en requête POST
        pk : l'identifiant d'une technologie' à supprimer.

    Returns:
        fiche_pompe.html : la page des modèles de pompe mise à jour.

    """
    queryset1 = get_object_or_404(TechnologiePompe, pk=pk)
    if request.method == "POST":
        queryset1.delete()
        msg_succes = f'La technologie de vide, {pk} a bien été supprimée.'
        url = reverse('pompe:fiche_pompe') + '?msg_succes=' + msg_succes

        return redirect(url)

    context = {'queryset1': queryset1}
    return render(request, 'pompe/fiche_pompe.html', context)


# inventaire et tutelle
def inventaire(request):
    """
    Fonction d'affichage des tutelles budgétaire et numéros d'iventaire de stock de pompe.

    Args:
        request: l'objet soumis en requête POST

    Returns:
        inventaire.html : la page inventaire à afficher.

    """
    inventaires = Inventaire.objects.all().order_by('numero')
    tutelles = Tutelle.objects.all().order_by('nom')

    # forms
    if request.method == "POST":
        form = Inventaireform(request.POST)
        form2 = Tutelleform(request.POST)

        if form2.is_valid() and 'tutelle_form' in request.POST:
            form2.save()
            msg_succes = f'La tutelle budgétaire a bien été créée.'
            url = reverse('pompe:inventaire') + '?msg_succes=' + msg_succes

        elif form.is_valid() and 'inventaire_form' in request.POST:
            form.save()
            msg_succes = f'Le numéro d\'inventaire a bien été créé.'
            url = reverse('pompe:inventaire') + '?msg_succes=' + msg_succes

        return redirect(url)
    else:
        form = Inventaireform()
        form2 = Tutelleform()

    msg_succes = request.GET.get('msg_succes', '')
    msg_erreur = request.GET.get('msg_erreur', '')
    msg_warning = request.GET.get('msg_warning', '')

    context = {
        'inventaires': inventaires,
        'tutelles': tutelles,
        'form': form,
        'form2': form2,
        'msg_warning': msg_warning,
        'msg_erreur': msg_erreur,
        'msg_succes': msg_succes,

    }
    return render(request, 'pompe/inventaire.html', context)


def export_data_inventaire(request):
    """
    Fonction d'exportation des numéros d'inventaires des pompes.
    Args:
        request: la requête d'exportation

    Returns:
          inventaire_numero_pompe : le fichier excel contenant les numéros exportés
    """
    # Exportation en fichier excel

    dataset = Inventaire.objects.all()
    # Création du classeur excel
    classeur = xlwt.Workbook()
    page = classeur.add_sheet("InventaireNumero")
    #entete
    headers =["ID", "Tutelles","Numéro","Date de création"]
    for col_index, header in enumerate(headers):
        page.write(0, col_index, header)
    #datas
    for row_index, row in enumerate(dataset):
        page.write(row_index + 1, 0, row.id),
        page.write(row_index + 1, 1, row.tutelle.nom),
        page.write(row_index + 1, 2, row.numero),
        page.write(row_index + 1, 3, row.date_inventaire.strftime("%d/%m/%Y")),

    # préparation de l'objet au format excel a télécharger
    reponse = HttpResponse(content_type='application/ms-excel')
    reponse['Content-Disposition'] = 'attachment; filename="inventaire_numero_pompe.xls" '
    classeur.save(reponse)
    return reponse


def update_inventaire(request, pk):
    """
    Fonction de mise à jour d'un numéro d'inventaire en base de données.

    Args:
        request: l'objet soumis en requête POST
        pk : l'identifiant du numéro à modifier.

    Returns:
        inventaire.html : la page inventaire mise à jour.

    """
    inventaires = get_object_or_404(Inventaire, pk=pk)

    if request.method == "POST":
        form = ModifInventaireForm(request.POST, instance=inventaires)
        if form.is_valid():
            form.save()
            msg_succes = f'Le numéro d\'inventaire : {pk} a bien été mis à jour.'
            url = reverse('pompe:inventaire') + '?msg_succes=' + msg_succes
            return redirect(url)
        else:
            msg_erreur = f'Le numéro d\'inventaire : {pk} n\'a pas été mis à jour.'
            url = reverse('pompe:inventaire') + '?msg_erreur=' + msg_erreur
            return redirect(url)

    else:
        form = ModifInventaireForm(instance=inventaires)
    return render(request, 'pompe/forms.html', {'form': form})


def delete_inventaire(request, pk):
    """
    Fonction de suppression d'un numéro d'inventaire en base de données.

    Args:
        request: l'objet soumis en requête POST
        pk : l'identifiant du numéro à supprimer.

    Returns:
        inventaire.html : la page inventaire mise à jour.

    """
    queryset = get_object_or_404(Inventaire, pk=pk)
    if request.method == "POST":
        queryset.delete()
        msg_succes = f'Le numéro d\'inventaire a bien été supprimé.'
        url = reverse('pompe:inventaire') + '?msg_succes=' + msg_succes
        return redirect(url)

    return render(request, 'pompe/inventaire.html', {'queryset': queryset})


def delete_tutelle(request, pk):
    """
    Fonction de suppression d'une tutelle budgétaire en base de données.

    Args:
        request: l'objet soumis en requête POST
        pk : l'identifiant de la tutelle à supprimer.

    Returns:
        inventaire.html : la page inventaire mise à jour.

    """
    queryset1 = get_object_or_404(Tutelle, pk=pk)
    if request.method == "POST":
        queryset1.delete()
        msg_succes = f'La tutelle budgétaire a bien été supprimé.'
        url = reverse('pompe:inventaire') + '?msg_succes=' + msg_succes
        return redirect(url)

    return render(request, 'pompe/inventaire.html', {'queryset1': queryset1})


# pieces detachées
def pdetache(request):
    """
    Fonction d'affichage des pièces détachées.

    Args:
        request: l'objet soumis en requête POST

    Returns:
        piece.html : la page mise à jour.

    """
    pieces = PiecesPompe.objects.all().order_by('nom')

    msg_succes = request.GET.get('msg_succes', '')
    msg_erreur = request.GET.get('msg_erreur', '')
    msg_warning = request.GET.get('msg_warning', '')
    context = {
        'pieces': pieces,
        'msg_warning': msg_warning,
        'msg_erreur': msg_erreur,
        'msg_succes': msg_succes,
    }
    return render(request, 'pompe/piece.html', context)


def add_pdetache(request):
    """
    Fonction de création d'une pièce détachée en base de données.

    Args:
        request: l'objet soumis en requête POST

    Returns:
        piece.html : la page mise à jour.

    """
    if request.method == "POST":
        form = PiecePompeform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            msg_succes = f'La pièce a bien ajouté au stock.'
            url = reverse('pompe:pdetache') + '?msg_succes=' + msg_succes
        else:
            msg_erreur = f'La pièce n\'a pas pu être ajouté au stock.'
            url = reverse('pompe:pdetache') + '?msg_erreur=' + msg_erreur

        return redirect(url)

    else:
        form = PiecePompeform()
    return render(request, 'pompe/forms.html', {'form': form})


def update_pdetache(request, pk):
    """
    Fonction de mise à jour d'une pièce détachée en base de données.

    Args:
        request: l'objet soumis en requête POST
        pk : l'identifiant de la pièce détachée à modifier.

    Returns:
        piece.html : la page mise à jour.

    """
    pdetaches = get_object_or_404(PiecesPompe, pk=pk)

    if request.method == "POST":
        form = ModifPiecePompeForm(request.POST, request.FILES, instance=pdetaches)
        if form.is_valid():
            form.save()
            msg_succes = f'Le stock a bien été mis à jour.'
            url = reverse('pompe:pdetache') + '?msg_succes=' + msg_succes
        else:
            msg_erreur = f'Le stock n\'a pas pu être mis à jour.'
            url = reverse('pompe:pdetache') + '?msg_erreur=' + msg_erreur

        return redirect(url)
    else:
        form = ModifPiecePompeForm(instance=pdetaches)
    return render(request, 'pompe/forms.html', {'form': form})


def delete_pdetache(request, pk):
    """
    Fonction de suppression d'une pièce détachée en base de données.

    Args:
        request: l'objet soumis en requête POST
        pk : l'identifiant de la pièce détachée à supprimer.

    Returns:
        piece.html : la page mise à jour.

    """
    pieces = get_object_or_404(PiecesPompe, pk=pk)
    if request.method == "POST":
        pieces_image = pieces.image.path
        image_path = os.path.dirname(pieces_image)
        if os.path.exists(pieces_image):
            os.remove(pieces_image)
            if len(os.listdir(image_path)) == 0:
                os.rmdir(image_path)
            pieces.delete()
            msg_succes = f'Le stock a bien été supprimé.'
            url = reverse('pompe:pdetache') + '?msg_succes=' + msg_succes
        return redirect(url)

    return render(request, 'pompe/piece.html', {'pieces': pieces})


# huile
def huile(request):
    """
    Fonction d'affichage des lots d'huiles en base de données.

    Args:
        request: l'objet soumis en requête POST
        pk : l'identifiant du lot à supprimer.

    Returns:
        huile.html : la page mise à jour.

    """
    huiles = Huile.objects.all().order_by('nom')
    msg_succes = request.GET.get('msg_succes', '')
    msg_erreur = request.GET.get('msg_erreur', '')
    msg_warning = request.GET.get('msg_warning', '')

    context = {
        'huiles': huiles,
        'msg_warning': msg_warning,
        'msg_erreur': msg_erreur,
        'msg_succes': msg_succes,
    }
    return render(request, 'pompe/huile.html', context)


def add_huile(request):
    """
    Fonction de création d'un lot d'huile en base de données.

    Args:
        request: l'objet soumis en requête POST

    Returns:
        huile.html : la page mise à jour.

    """
    if request.method == "POST":
        form = Huileform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            msg_succes = f'Le stock a bien ajouté.'
            url = reverse('pompe:huile') + '?msg_succes=' + msg_succes
        else:
            msg_erreur = f'Le stock n\'a pas pu être ajouté.'
            url = reverse('pompe:huile') + '?msg_erreur=' + msg_erreur

        return redirect(url)
    else:
        form = Huileform()
    return render(request, 'pompe/forms.html', {'form': form})


def update_huile(request, pk):
    """
    Fonction de mise à jour d'un lot d'huile en base de données.

    Args:
        request: l'objet soumis en requête POST
        pk : l'identifiant du lot à modifier.

    Returns:
        huile.html : la page mise à jour.

    """
    huiles = get_object_or_404(Huile, pk=pk)

    if request.method == "POST":
        form = ModifHuileForm(request.POST, request.FILES, instance=huiles)
        if form.is_valid():
            form.save()
            msg_succes = f'Le stock a bien été mis à jour.'
            url = reverse('pompe:huile') + '?msg_succes=' + msg_succes
        else:
            msg_erreur = f'Le stock n\'a pas pu être mis à jour.'
            url = reverse('pompe:huile') + '?msg_erreur=' + msg_erreur
        return redirect(url)
    else:
        form = ModifHuileForm(instance=huiles)
    return render(request, 'pompe/forms.html', {'form': form})


def delete_huile(request, pk):
    """
    Fonction de suppression d'un lot d'huile en base de données.

    Args:
        request: l'objet soumis en requête POST
        pk : l'identifiant du lot à supprimer.

    Returns:
        huile.html : la page mise à jour.

    """
    huiles = get_object_or_404(Huile, pk=pk)
    if request.method == "POST":
        huile_path = huiles.image.path
        huile_directory = os.path.dirname(huile_path)
        if os.path.exists(huile_path):
            os.remove(huile_path)
            if len(os.listdir(huile_directory)) == 0:
                os.rmdir(huile_directory)
            huiles.delete()
            msg_succes = f'Le stock a bien été supprimé.'
            url = reverse('pompe:huile') + '?msg_succes=' + msg_succes
        return redirect(url)
    return render(request, 'pompe/huile.html', {'huiles': huiles})


# kit de maintenance
def kit(request):
    """
    Fonction d'affichage des kits de maintenance en base de données.

    Args:
        request: l'objet soumis en requête POST

    Returns:
        kit.html : la page des kits.

    """
    kits = Kit.objects.all().order_by('nom')
    msg_succes = request.GET.get('msg_succes', '')
    msg_erreur = request.GET.get('msg_erreur', '')
    msg_warning = request.GET.get('msg_warning', '')

    context = {
        'kits': kits,
        'msg_warning': msg_warning,
        'msg_erreur': msg_erreur,
        'msg_succes': msg_succes,
    }
    return render(request, 'pompe/kit.html', context)


def add_kit(request):
    """
    Fonction de création d'un kit de maintenance en base de données.

    Args:
        request: l'objet soumis en requête POST

    Returns:
        kit.html : la page des kits mise à jour.

    """
    if request.method == "POST":
        form = Kitform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            msg_succes = f'Le stock a bien ajouté.'
            url = reverse('pompe:kit') + '?msg_succes=' + msg_succes
        else:
            msg_erreur = f'Le stock n\'a pas pu être ajouté.'
            url = reverse('pompe:kit') + '?msg_erreur=' + msg_erreur

        return redirect(url)
    else:
        form = Kitform()
    return render(request, 'pompe/forms.html', {'form': form})


def update_kit(request, pk):
    """
    Fonction de mise à jour d'un kit de maintenance en base de données.

    Args:
        request: l'objet soumis en requête POST
        pk : l'identifiant du kit à modifier.

    Returns:
        kit.html : la page des kits mise à jour.

    """
    kits = get_object_or_404(Kit, pk=pk)
    if request.method == "POST":
        form = ModifKitForm(request.POST, request.FILES, instance=kits)
        if form.is_valid():
            form.save()
            msg_succes = f'Le stock a bien été mis à jour.'
            url = reverse('pompe:kit') + '?msg_succes=' + msg_succes
        else:
            msg_erreur = f'Le stock n\'a pas pu être mis à jour.'
            url = reverse('pompe:kit') + '?msg_erreur=' + msg_erreur
        return redirect(url)

    else:
        form = ModifKitForm(instance=kits)
    return render(request, 'pompe/forms.html', {'form': form})


def delete_kit(request, pk):
    """
    Fonction de suppression d'un kit de maintenance en base de données.

    Args:
        request: l'objet soumis en requête POST
        pk : l'identifiant du kit à supprimer.

    Returns:
        kit.html : la page des kits mise à jour.

    """
    kits = get_object_or_404(Kit, pk=pk)
    if request.method == "POST":
        kit_image = kits.image.path
        image_directory = os.path.dirname(kit_image)
        if os.path.exists(kit_image):
            os.remove(kit_image)
            if len(os.listdir(image_directory)) == 0:
                os.rmdir(image_directory)
            kits.delete()
            msg_succes = f'Le stock a bien supprimé.'
            url = reverse('pompe:kit') + '?msg_succes=' + msg_succes
        return redirect(url)
    return render(request, 'pompe/kit.html', {'kits': kits})


# Documentations

def doc(request):
    """
    Fonction d'affichage des documentations technique des pompes en base de données.

    Args:
        request: l'objet soumis en requête POST

    Returns:
        doc.html : la page des documentations.

    """
    docs = Document.objects.all().order_by('nom')
    msg_succes = request.GET.get('msg_succes', '')
    msg_erreur = request.GET.get('msg_erreur', '')
    msg_warning = request.GET.get('msg_warning', '')
    context = {
        'docs': docs,
        'msg_warning': msg_warning,
        'msg_erreur': msg_erreur,
        'msg_succes': msg_succes,
    }
    return render(request, 'pompe/doc.html', context)


def add_doc(request):
    """
    Fonction d'ajout d'une documentation technique des pompes en base de données.

    Args:
        request: l'objet soumis en requête POST

    Returns:
        doc.html : la page des documentations mise à jour.

    """
    if request.method == "POST":
        form = Docform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            msg_succes = f'La documentation a bien été ajoutée.'
            url = reverse('pompe:doc') + '?msg_succes=' + msg_succes
        else:
            msg_erreur = f'La documentation n\'a pas pu être ajoutée.'
            url = reverse('pompe:doc') + '?msg_erreur=' + msg_erreur

        return redirect(url)
    else:
        form = Docform()
    return render(request, 'pompe/forms.html', {'form': form})


def update_doc(request, pk):
    """
    Fonction de mise à jour d'une documentation technique des pompes en base de données.

    Args:
        request: l'objet soumis en requête POST
        pk : l'identifiant de la documentation à mettre à jour.

    Returns:
        doc.html : la page des documentations mise à jour.

    """
    docs = get_object_or_404(Document, pk=pk)

    if request.method == "POST":
        form = ModifDocForm(request.POST, request.FILES, instance=docs)
        if form.is_valid():
            form.save()
            msg_succes = f'La documentation a bien été mise à jour.'
            url = reverse('pompe:doc') + '?msg_succes=' + msg_succes
        else:
            msg_erreur = f'La documentation n\'a pas pu être mise à jour.'
            url = reverse('pompe:doc') + '?msg_erreur=' + msg_erreur
        return redirect(url)
    else:
        form = ModifDocForm(instance=docs)
    return render(request, 'pompe/forms.html', {'form': form})


def delete_doc(request, pk):
    """
    Fonction de suppression d'une documentation technique des pompes en base de données.

    Args:
        request: l'objet soumis en requête POST
        pk : l'identifiant de la documentation à supprimer.

    Returns:
        doc.html : la page des documentations mise à jour.

    """
    docs = get_object_or_404(Document, pk=pk)
    if request.method == "POST":
        #: Suppression du fichier sur le serveur
        doc_file = docs.manuel.path
        doc_directory = os.path.dirname(doc_file)
        if os.path.exists(doc_file):
            os.remove(doc_file)
            if len(os.listdir(doc_directory)) == 0:
                os.rmdir(doc_directory)
            docs.delete()
            msg_succes = f'La documentation a bien supprimée.'
            url = reverse('pompe:doc') + '?msg_succes=' + msg_succes
        return redirect(url)
    return render(request, 'pompe/doc.html', {'docs': docs})
