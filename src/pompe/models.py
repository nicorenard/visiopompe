"""
Database classes and functions
"""
import os.path
from datetime import date, datetime
from django.db import models
from django.utils import timezone

from .utils import upload_to_pompe, upload_to_huile, upload_to_documentation, upload_to_logoMiniFabriquant, \
    upload_to_logoFabriquant, upload_to_kit, upload_to_piecepompe


class VersionApp(models.Model):
    """
    Classe pour gérer les versions de l'application.

    Args:
        models : Attribut de la classe Model de Django

    Returns:
          l'objet contenant la version avec ses attributs de classe
    """
    version = models.CharField(default='x.x.x', max_length=10, verbose_name="Version")
    maj_maj = models.DecimalField(default=0, max_digits=10, decimal_places=0, verbose_name="Mise à jour majeur")
    maj_min = models.DecimalField(default=0, max_digits=10, decimal_places=0, verbose_name="Mise à jour mineur")
    bug = models.DecimalField(default=0, max_digits=10, decimal_places=0, verbose_name="Bugs")
    texte = models.TextField(blank=True, null=True, max_length=254, verbose_name="Description")
    date_version = models.DateField(default=date.today, verbose_name="Date")

    class Meta:
        db_table = "tab_version_vs"

    def __str__(self):
        return self.version


# localisation tables #
class Site(models.Model):
    nom = models.CharField(default='', max_length=254, verbose_name="Site")

    class Meta:
        db_table = "tab_site_st"

    def __str__(self):
        return self.nom


class Batiment(models.Model):
    nom = models.CharField(default='', max_length=254, verbose_name="Batiment")
    site = models.ForeignKey(Site, null=True, on_delete=models.CASCADE)

    class Meta:
        db_table = "tab_batiment_bmt"

    def __str__(self):
        return self.nom


class Etage(models.Model):
    nom = models.CharField(default='', max_length=254, verbose_name="Etage")
    batiment = models.ForeignKey(Batiment, null=True, on_delete=models.CASCADE)

    class Meta:
        db_table = "tab_etage_etg"

    def __str__(self):
        return self.nom


class Piece(models.Model):
    nom = models.CharField(default='', max_length=254, verbose_name="Piece")
    etage = models.ForeignKey(Etage, null=True, on_delete=models.CASCADE)

    class Meta:
        db_table = "piece"

    def __str__(self):
        return self.nom


# pump tables #
class Fabriquant(models.Model):
    nom = models.CharField(max_length=50)
    logo_max = models.ImageField(upload_to=upload_to_logoFabriquant, default="noimage.jpg",
                                 max_length=254, verbose_name='Logo')
    logo_mini = models.ImageField(upload_to=upload_to_logoMiniFabriquant, max_length=254,
                                  blank=True, null=True, verbose_name='miniature')
    adresse = models.CharField(max_length=250, blank=True, null=True)
    code_postal = models.CharField(max_length=5, blank=True, null=True)
    ville = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        db_table = "tab_fabriquant_fab"

    def __str__(self):
        return self.nom

    def save(self, *args, **kwargs):
        directory = os.path.dirname(self.image.path)
        if not os.path.exists(directory):
            os.makedirs(directory)

        super().save(*args, **kwargs)


class Document(models.Model):
    nom = models.CharField(default='', max_length=50, verbose_name="Nom de la doc technique")
    fabriquant = models.ForeignKey(Fabriquant, null=True, blank=False, on_delete=models.SET_NULL)
    manuel = models.FileField(upload_to=upload_to_documentation, max_length=254, verbose_name="Télécharger le manuel")
    version = models.CharField(default='x.x.x', max_length=50, verbose_name="Version de la doc technique")

    class Meta:
        db_table = "tab_document_doc"

    def __str__(self):
        return self.nom


class TechnologiePompe(models.Model):
    nom = models.CharField(default='', max_length=50, verbose_name="Type de technologie")
    info = models.CharField(default='', max_length=50, null=False, blank=True,
                            verbose_name="Détail de la technologie")

    class Meta:
        db_table = "tab_technologiePompe_tep"

    def __str__(self):
        return self.nom


class ModelePompe(models.Model):
    image = models.ImageField(upload_to=upload_to_pompe, max_length=254, blank=True, null=True)
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
    vide_theo = models.FloatField(default=0, verbose_name="Vide limite Fabriquant")
    fabriquant = models.ForeignKey(Fabriquant, null=True, blank=False, on_delete=models.SET_NULL)
    documentation = models.ForeignKey(Document, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = "tab_modelePompe_pom"

    def __str__(self):
        return self.nom

    def save(self, *args, **kwargs):
        directory = os.path.dirname(self.image.path)
        if not os.path.exists(directory):
            os.makedirs(directory)

        super().save(*args, **kwargs)


class Huile(models.Model):
    nom = models.CharField(default='', max_length=50, verbose_name="Nom")
    image = models.ImageField(upload_to=upload_to_huile, max_length=254, blank=True, null=True, verbose_name="Image")
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

    def save(self, *args, **kwargs):
        directory = os.path.dirname(self.image.path)
        if not os.path.exists(directory):
            os.makedirs(directory)

        super().save(*args, **kwargs)


class ModelEquipe(models.Model):
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
    nom = models.CharField(max_length=30, default='', verbose_name="Tutelle")

    class Meta:
        db_table = "tab_tutelle_tut"

    def __str__(self):
        return self.nom


class Inventaire(models.Model):
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
    image = models.ImageField(upload_to=upload_to_kit, max_length=254, blank=True, null=True)
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

    def save(self, *args, **kwargs):
        directory = os.path.dirname(self.image.path)
        if not os.path.exists(directory):
            os.makedirs(directory)

        super().save(*args, **kwargs)


class PiecesPompe(models.Model):
    image = models.ImageField(upload_to=upload_to_piecepompe, max_length=254, blank=True, null=True)
    nom = models.CharField(default='', max_length=50, verbose_name="Nom de la pièce détachée")
    date_maj = models.DateField(default=date.today, verbose_name="Date de mise à jour du stock", blank=True, null=True)
    fabriquant = models.ForeignKey(Fabriquant, null=True, blank=False, on_delete=models.SET_NULL)
    piece = models.ForeignKey(Piece, null=True, blank=True, on_delete=models.SET_NULL)
    quantite = models.DecimalField(default=0, max_digits=5, decimal_places=0, verbose_name="Stock ?")
    information = models.TextField(blank=True, null=True, max_length=200,
                                   verbose_name="Information(s) complémentaire(s)")

    class Meta:
        db_table = "tab_piecepompe_pip"

    def __str__(self):
        return self.nom

    def save(self, *args, **kwargs):
        directory = os.path.dirname(self.image.path)
        if not os.path.exists(directory):
            os.makedirs(directory)

        super().save(*args, **kwargs)
