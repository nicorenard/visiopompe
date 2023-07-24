"""
Database classes and functions
"""
import os.path
from datetime import date, datetime
from django.db import models
from django.utils import timezone

from .utils import upload_to_pompe, upload_to_huile, upload_to_documentation, upload_to_logoMiniFabriquant, \
    upload_to_logoFabriquant, upload_to_kit, upload_to_piecepompe, image_resize


class VersionApp(models.Model):
    """
    Classe pour gérer les versions de l'application.

    Args:
        models : Attribut de la classe Model de Django

    Returns:
          l'objet contenant la version avec ses attributs de classe
    """
    nom = models.CharField(default='x.x.x', max_length=20, verbose_name="Version")

    class Meta:
        db_table = "tab_version_vs"

    def __str__(self):
        return self.nom


# localisation tables #
class Site(models.Model):
    """
    Classe pour gérer les sites.

    Args:
        models : Attribut de la classe Model de Django

    Returns:
          l'objet contenant un site
    """
    nom = models.CharField(default='', max_length=254, verbose_name="Site")

    class Meta:
        db_table = "tab_site_st"

    def __str__(self):
        return self.nom


class Batiment(models.Model):
    """
    Classe pour gérer les bâtiments liés à un ou plusieurs sites.

    Args:
        models : Attribut de la classe Model de Django

    Returns:
          l'objet contenant un bâtiment
    """
    nom = models.CharField(default='', max_length=254, verbose_name="Bâtiment")
    site = models.ForeignKey(Site, null=True, on_delete=models.CASCADE)

    class Meta:
        db_table = "tab_batiment_bmt"

    def __str__(self):
        return self.nom


class Etage(models.Model):
    """
    Classe pour gérer les étages liés à un ou plusieurs bâtiments.

    Args:
        models : Attribut de la classe Model de Django

    Returns:
          l'objet contenant un étage
    """
    nom = models.CharField(default='', max_length=254, verbose_name="Etage")
    batiment = models.ForeignKey(Batiment, null=True, on_delete=models.CASCADE)

    class Meta:
        db_table = "tab_etage_etg"

    def __str__(self):
        return self.nom


class Piece(models.Model):
    """
    Classe pour gérer les pièces liés à un ou plusieurs étages.

    Args:
        models : Attribut de la classe Model de Django

    Returns:
          l'objet contenant une salle
    """
    nom = models.CharField(default='', max_length=254, verbose_name="Pièce")
    etage = models.ForeignKey(Etage, null=True, on_delete=models.CASCADE)

    class Meta:
        db_table = "piece"

    def __str__(self):
        return self.nom


# pump tables #
class Fabriquant(models.Model):
    """
    Classe pour gérer les fiches de fabriquants.

    Args:
        models : Attribut de la classe Model de Django

    Returns:
          l'objet contenant un fabriquant
    """
    nom = models.CharField(max_length=50)
    logo_max = models.ImageField(upload_to=upload_to_logoFabriquant, default="noimage.jpg",
                                 max_length=254, verbose_name='Logo')
    logo_mini = models.ImageField(upload_to=upload_to_logoMiniFabriquant, max_length=254,
                                  default="noimage.jpg", verbose_name='miniature')
    adresse = models.CharField(max_length=250, blank=True, null=True)
    code_postal = models.CharField(max_length=5, blank=True, null=True)
    ville = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        db_table = "tab_fabriquant_fab"

    def __str__(self):
        return self.nom

    def save(self, commit=True, *args, **kwargs):
        directory = os.path.dirname(self.logo_max.path)
        directory2 = os.path.dirname(self.logo_mini.path)
        if not os.path.exists(directory):
            os.makedirs(directory)
        if not os.path.exists(directory2):
            os.makedirs(directory2)

        if commit:
            image_resize(self.logo_max, 250, 250)
            image_resize(self.logo_mini, 80, 80)
            super().save(*args, **kwargs)

        super().save(*args, **kwargs)


class Document(models.Model):
    """
    Classe pour gérer les fiches de documentations techniques.

    Args:
        models : Attribut de la classe Model de Django

    Returns:
          l'objet contenant un document
    """
    nom = models.CharField(default='', max_length=50, verbose_name="Nom")
    fabriquant = models.ForeignKey(Fabriquant, null=True, blank=False, on_delete=models.SET_NULL)
    manuel = models.FileField(upload_to=upload_to_documentation, max_length=254, verbose_name="Téléverser le manuel")
    version = models.CharField(default='x.x.x', max_length=50, verbose_name="Version de la documentation")

    class Meta:
        db_table = "tab_document_doc"

    def __str__(self):
        return self.nom

    def save(self, commit=True, *args, **kwargs):
        directory = os.path.dirname(self.manuel.path)
        if not os.path.exists(directory):
            os.makedirs(directory)

        super().save(*args, **kwargs)


class TechnologiePompe(models.Model):
    """
    Classe pour gérer les technologies de vide pour les pompes.

    Args:
        models : Attribut de la classe Model de Django

    Returns:
          l'objet contenant une technologie
    """
    nom = models.CharField(default='', max_length=50, verbose_name="Type de technologie du vide (palettes, membranes...")
    info = models.CharField(default='', max_length=50, null=False, blank=True,
                            verbose_name="Détail de la technologie")

    class Meta:
        db_table = "tab_technologiePompe_tep"

    def __str__(self):
        return self.nom


class ModelePompe(models.Model):
    """
    Classe pour gérer les fiches de pompes (série ou famille).

    Args:
        models : Attribut de la classe Model de Django

    Returns:
          l'objet contenant un fiche
    """
    image = models.ImageField(upload_to=upload_to_pompe, max_length=254, default="noimage.jpg")
    nom = models.CharField(default='', max_length=50, verbose_name="Nom du modèle")
    modele = models.CharField(default='', max_length=50, verbose_name="Série ou famille ")
    PHASAGE = [
        ('Monophasé', 'Monophasé'),
        ('Triphasé', 'Triphasé')
    ]
    phasage = models.CharField(max_length=15, choices=PHASAGE, default='Monophasé',
                               verbose_name="Phasage du moteur électrique")
    PUISSANCE = [
        ('50 Hertz', '50 Hertz'),
        ('60 Hertz', '60 Hertz')
    ]
    puissance = models.CharField(default='50', choices=PUISSANCE, max_length=20, verbose_name="Puissance du moteur")
    technologie = models.ForeignKey(TechnologiePompe, null=False, blank=False, on_delete=models.DO_NOTHING)
    vide_theo = models.FloatField(default=0, verbose_name="Vide limite du fabriquant")
    fabriquant = models.ForeignKey(Fabriquant, null=True, blank=False, on_delete=models.SET_NULL)
    documentation = models.ForeignKey(Document, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = "tab_modelePompe_pom"

    def __str__(self):
        return self.nom

    def save(self, commit=True, *args, **kwargs):
        directory = os.path.dirname(self.image.path)
        if not os.path.exists(directory):
            os.makedirs(directory)

        if commit:
            image_resize(self.image, 250, 250)
            super().save(*args, **kwargs)

        super().save(*args, **kwargs)


class Huile(models.Model):
    """
    Classe pour gérer les types d'huiles pour les pompes.

    Args:
        models : Attribut de la classe Model de Django

    Returns:
          l'objet contenant une huile
    """
    nom = models.CharField(default='', max_length=50, verbose_name="Nom")
    image = models.ImageField(upload_to=upload_to_huile, max_length=254, default="noimage.jpg", verbose_name="Image")
    fabriquant = models.ForeignKey(Fabriquant, null=True, blank=False, on_delete=models.SET_NULL)
    ref_fab = models.CharField(max_length=150, default='', verbose_name="Référence", blank=True, null=True)
    piece = models.ForeignKey(Piece, null=True, blank=False, on_delete=models.SET_NULL)
    quantite = models.DecimalField(default=0, max_digits=5, decimal_places=0, verbose_name="Quantité en stock")
    date_maj = models.DateField(default=date.today, verbose_name="Date de mise à jour du stock", blank=True, null=True)
    information = models.TextField(blank=True, null=True, max_length=200, verbose_name="Information(s) complémentaire")

    class Meta:
        db_table = "tab_huile_hui"

    def __str__(self):
        return self.nom

    def save(self, commit=True, *args, **kwargs):
        directory = os.path.dirname(self.image.path)
        if not os.path.exists(directory):
            os.makedirs(directory)

        if commit:
            image_resize(self.image, 250, 250)
            super().save(*args, **kwargs)

        super().save(*args, **kwargs)


class ModelEquipe(models.Model):
    """
    Classe pour gérer les équipes d'appartenance de matériels.

    Args:
        models : Attribut de la classe Model de Django

    Returns:
          l'objet contenant une équipe
    """
    nom = models.CharField(default='', max_length=255, verbose_name="Nom complet de l'équipe")
    sigle = models.CharField(default='', max_length=10, verbose_name="Abbreviation du nom", blank=True, null=True)
    nom_responsable = models.CharField(default='', max_length=100, verbose_name="Responsable de l'équipe",
                                       blank=True, null=True)
    email_responsable = models.CharField(default='', max_length=50, verbose_name="Email du Responsable",
                                         blank=True, null=True)
    date = models.DateField(default=date.today, verbose_name="Date de création")
    localisation = models.ForeignKey(Etage, null=True, blank=False, on_delete=models.SET_NULL)

    class Meta:
        db_table = "tab_modeleEquipe_eqp"

    def __str__(self):
        return self.nom


class Tutelle(models.Model):
    """
    Classe pour gérer les tutelles budgétaires.

    Args:
        models : Attribut de la classe Model de Django

    Returns:
          l'objet contenant une tutelle budgétaire
    """
    nom = models.CharField(max_length=30, default='', verbose_name="Tutelle")

    class Meta:
        db_table = "tab_tutelle_tut"

    def __str__(self):
        return self.nom


class Inventaire(models.Model):
    """
    Classe pour gérer les numéros d'inventaire pour les pompes.

    Args:
        models : Attribut de la classe Model de Django

    Returns:
          l'objet contenant un numéro lié à une tutelle
    """
    tutelle = models.ForeignKey(Tutelle, null=True, blank=False, on_delete=models.CASCADE)
    numero = models.CharField(max_length=150, default='', verbose_name="Numéro d'inventaire")
    date_inventaire = models.DateField(default=date.today, verbose_name="Date de création")

    class Meta:
        db_table = "tab_inventaire_inv"

    def __str__(self):
        return self.numero


## historique on stock pump
# ref : https://stackoverflow.com/questions/10540111/store-versioned-history-of-field-in-django-model
class StockHistory(models.Model):
    """
    Classe pour gérer l'historique d'actions sur un stock de pompe.

    Args:
        models : Attribut de la classe Model de Django

    Returns:
          l'objet contenant l'historique d'un stock
    """
    version = models.IntegerField(editable=False)
    stockpump = models.ForeignKey('StockPompe', on_delete=models.CASCADE)
    date_historique = models.DateTimeField(default=datetime.now())
    history = models.TextField()

    class Meta:
        unique_together = ('version', 'stockpump')

    def save(self, *args, **kwargs):
        current_version = StockHistory.objects.filter(stockpump=self.stockpump).order_by('-version')[:1]
        self.version = current_version[0].version + 1 if current_version else 1
        super(StockHistory, self).save(*args, **kwargs)


class StockPompe(models.Model):
    """
    Classe pour gérer les stocks de pompes.

    Args:
        models : Attribut de la classe Model de Django

    Returns:
          l'objet contenant un stock
    """
    pompe = models.ForeignKey(ModelePompe, verbose_name="Modèle de pompe", null=True, blank=False,
                              on_delete=models.SET_NULL)
    mise_en_service = models.DateField(auto_now=date.today)
    etage = models.ForeignKey(Etage, null=True, blank=False, on_delete=models.SET_NULL)
    piece = models.ForeignKey(Piece, null=True, blank=False, on_delete=models.SET_NULL)
    place = models.CharField(default='', max_length=150, verbose_name="Emplacement dans la pièce",
                             blank=True, null=True)
    vide_user = models.FloatField(default=0, verbose_name="Vide limite testé", blank=True)
    num_serie = models.CharField(max_length=150, default='', verbose_name="Numéro de série")
    inventaire = models.ForeignKey(Inventaire, null=True, blank=True, on_delete=models.SET_NULL)
    STATUT_POMPE = [
        ('A', 'Active'),
        ('P', 'En panne'),
        ('R', 'En réparation'),
        ('S', 'En Stock'),
    ]
    statut = models.CharField(max_length=1, choices=STATUT_POMPE, default='A', verbose_name="Etat actuel de la pompe")
    atex = models.BooleanField(default=False, verbose_name="Pompe Atex ?")
    huile = models.ForeignKey(Huile, null=True, blank=True, on_delete=models.SET_NULL)
    equipe = models.ForeignKey(ModelEquipe, null=True, blank=True, on_delete=models.SET_NULL)
    vidange = models.DateField(default=timezone.now, verbose_name="Date de la prochaine vidange", blank=True, null=True)
    historique = models.TextField(blank=True, null=False, max_length=500, verbose_name="historique de la pompe")

    class Meta:
        db_table = "tab_stockpompe_stk"

    def __str__(self):
        return self.num_serie

    def stock_history(self):
        return StockHistory.objects.filter(stockpump=self).order_by('-version')

    def save(self, *args, **kwargs):
        super(StockPompe, self).save(*args, **kwargs)
        stock_history = self.stock_history()
        if not stock_history or self.historique != stock_history[0].history:
            newHistory = StockHistory(stockpump=self, history=self.historique)
            newHistory.save()


class Kit(models.Model):
    """
    Classe pour gérer les stocks de kit de maintenance.

    Args:
        models : Attribut de la classe Model de Django

    Returns:
          l'objet contenant un kit
    """
    image = models.ImageField(upload_to=upload_to_kit, max_length=254, default="noimage.jpg")
    nom = models.CharField(default='', max_length=50, verbose_name="Nom du kit")
    fabriquant = models.ForeignKey(Fabriquant, null=True, blank=False, verbose_name='Fabriquant',
                                   related_name="Fabriquant", on_delete=models.SET_NULL)
    date_maj = models.DateField(default=date.today, verbose_name="Date de mise à jour du stock", blank=True, null=True)
    ref_fab = models.CharField(max_length=50, default='', verbose_name="Référence Fabriquant", blank=True, null=True)
    revendeur = models.ForeignKey(Fabriquant, null=True, blank=True, verbose_name='Revendeur',
                                  related_name="Revendeur", on_delete=models.SET_NULL)
    ref_rev = models.CharField(max_length=50, default='', verbose_name="Référence Revendeur", blank=True, null=True)
    quantite = models.DecimalField(default=0, max_digits=5, decimal_places=0, verbose_name="Quantité en stock")
    piece = models.ForeignKey(Piece, null=True, blank=True, on_delete=models.SET_NULL)
    information = models.TextField(blank=True, null=True, max_length=200, verbose_name="Information(s) complémentaire")

    class Meta:
        db_table = "tab_kit_kit"

    def __str__(self):
        return self.nom

    def save(self, commit=True, *args, **kwargs):
        directory = os.path.dirname(self.image.path)
        if not os.path.exists(directory):
            os.makedirs(directory)

        if commit:
            image_resize(self.image, 250, 250)
            super().save(*args, **kwargs)

        super().save(*args, **kwargs)


class PiecesPompe(models.Model):
    """
    Classe pour gérer les pièces détachées d'un stock de pompe.

    Args:
        models : Attribut de la classe Model de Django

    Returns:
          l'objet contenant une pièce détachée
    """
    image = models.ImageField(upload_to=upload_to_piecepompe, max_length=254, blank=True, null=True, default="noimage.jpg")
    nom = models.CharField(default='', max_length=50, verbose_name="Nom de la pièce détachée")
    date_maj = models.DateField(default=date.today, verbose_name="Date de mise à jour du stock", blank=True, null=True)
    fabriquant = models.ForeignKey(Fabriquant, null=True, blank=False, on_delete=models.SET_NULL)
    piece = models.ForeignKey(Piece, null=True, blank=False, on_delete=models.SET_NULL)
    quantite = models.DecimalField(default=0, max_digits=5, decimal_places=0, verbose_name="Stock ?")
    information = models.TextField(blank=True, null=True, max_length=200,
                                   verbose_name="Information(s) complémentaire(s)")

    class Meta:
        db_table = "tab_piecepompe_pip"

    def __str__(self):
        return self.nom

    def save(self, commit=True, *args, **kwargs):
        directory = os.path.dirname(self.image.path)
        if not os.path.exists(directory):
            os.makedirs(directory)

        if commit:
            image_resize(self.image, 250, 250)
            super().save(*args, **kwargs)

        super().save(*args, **kwargs)
