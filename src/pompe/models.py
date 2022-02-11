from datetime import date
from django.db import models


# apps version #
class VersionApp(models.Model):
    version = models.CharField(default='x.x.x', max_length=10, verbose_name="Version")
    maj_maj = models.DecimalField(default=0, max_digits=10, decimal_places=0, verbose_name="Mise à jour majeur")
    maj_min = models.DecimalField(default=0, max_digits=10, decimal_places=0, verbose_name="Mise à jour mineur")
    bug = models.DecimalField(default=0, max_digits=10, decimal_places=0, verbose_name="Bugs")
    texte = models.TextField(blank=True, null=True, max_length=254, verbose_name="Description")
    date_version = models.DateField(default=date.today, verbose_name="Date")

    def __str__(self):
        return self.version

# localisation tables #
class Site(models.Model):
    nom = models.CharField(default='', max_length=254, verbose_name="Site")

    def __str__(self):
        return self.nom


class Batiment(models.Model):
    nom = models.CharField(default='', max_length=254, verbose_name="Batiment")
    site = models.ForeignKey(Site, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom


class Etage(models.Model):
    nom = models.CharField(default='', max_length=254, verbose_name="Etage")
    batiment = models.ForeignKey(Batiment, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom


class Piece(models.Model):
    nom = models.CharField(default='', max_length=254, verbose_name="Piece")
    etage = models.ForeignKey(Etage, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom


# pump tables #
class Fabriquant(models.Model):
    nom = models.CharField(max_length=50, blank=True)
    logo = models.ImageField(upload_to='logo_fabriquant/', max_length=254, blank=True, null=True)
    adresse = models.CharField(max_length=250, blank=True, null=True)
    code_postal = models.CharField(max_length=5, blank=True, null=True)
    ville = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.nom


class Doc(models.Model):
    nom = models.CharField(default='', max_length=50, verbose_name="Nom de la doc technique")
    fabriquant = models.ForeignKey(Fabriquant, null=True, blank=False, on_delete=models.SET_NULL)
    manuel = models.FileField(upload_to='manuel/', max_length=254, verbose_name="Télécharger le manuel")
    version = models.CharField(default='x.x.x', max_length=50, verbose_name="Version de la doc technique")

    def __str__(self):
        return self.nom


class ModelePompe(models.Model):
    image = models.ImageField(upload_to='pompe_img/', max_length=254, blank=True, null=True)
    nom = models.CharField(default='', max_length=50, verbose_name="Nom de la pompe")
    modele = models.CharField(default='', max_length=50, verbose_name="Modèle de la pompe")
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
    TECHNOLOGIE = [
        ('Sèches - Membranes', 'Sèches - Membranes'),
        ('Sèches - Vis', 'Sèches - Vis'),
        ('Palettes - 1 étage', 'Palettes - 1 étage'),
        ('Palettes - 2 étages', 'Palettes - 2 étages')
    ]
    technologie = models.CharField(max_length=30, choices=TECHNOLOGIE, verbose_name="Technologie du vide")
    vide_theo = models.FloatField(default=0, verbose_name="Vide limite Fabriquant")
    fabriquant = models.ForeignKey(Fabriquant, null=True, blank=False, on_delete=models.SET_NULL)
    documentation = models.ForeignKey(Doc, null=True, blank=False, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nom


class Huile(models.Model):

    nom = models.CharField(default='', max_length=50, verbose_name="Nom")
    image = models.ImageField(upload_to='huile_img/', max_length=254, blank=True, null=True, verbose_name="Image")
    fabriquant = models.ForeignKey(Fabriquant, null=True, blank=False, on_delete=models.SET_NULL)
    ref_fab = models.CharField(max_length=150, default='', verbose_name="Référence", blank=True, null=True)
    piece = models.ForeignKey(Piece, null=True, blank=False, on_delete=models.SET_NULL)
    quantite = models.DecimalField(default=0, max_digits=5, decimal_places=0, verbose_name="Quantité en stock")
    date_maj = models.DateField(default=date.today, verbose_name="Date de mise à jour du stock", blank=True, null=True)
    information = models.TextField(blank=True, null=True, max_length=200, verbose_name="Information(s) complémentaire")

    def __str__(self):
        return self.nom

class ModelEquipe(models.Model):
    nom = models.CharField(default='', max_length=255, verbose_name="Nom complet de l'équipe")
    sigle = models.CharField(default='', max_length=10, verbose_name="Abbreviation du nom", blank=True, null=True)
    nom_responsable = models.CharField(default='', max_length=100, verbose_name="Responsable de l'équipe",blank=True, null=True)
    email_responsable = models.CharField(default='', max_length=50,verbose_name="Email du Responsable",blank=True, null=True)
    date = models.DateField(default=date.today,verbose_name="Date de création")
    lieux = models.ForeignKey(Etage, null=True,blank=False, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nom

class Tutelle(models.Model):
    nom = models.CharField(max_length=10, default='', verbose_name="Tutelle")

    def __str__(self):
        return self.nom


class Inventaire(models.Model):
    tutelle = models.ForeignKey(Tutelle, null=True, blank=False, on_delete=models.CASCADE)
    numero = models.CharField(max_length=150, default='', verbose_name="Numéro d'inventaire")
    date_inventaire = models.DateField(default=date.today, verbose_name="Date de création")

    def __str__(self):
        return self.numero


class StockPompe(models.Model):
    pompe = models.ForeignKey(ModelePompe, null=True, blank=False, on_delete=models.SET_NULL)
    mise_en_service = models.DateField(auto_now=date.today)
    etage = models.ForeignKey(Etage, null=True, blank=False, on_delete=models.SET_NULL)
    piece = models.ForeignKey(Piece, null=True, blank=False, on_delete=models.SET_NULL)
    place = models.CharField(default='', max_length=150, verbose_name="Emplacement dans la pièce",
                             blank=True, null=True)
    vide_user = models.FloatField(default=0, verbose_name="Vide limite testé", blank=True)
    num_serie = models.CharField(max_length=150, default='', verbose_name="Numéro de série")
    inventaire = models.ForeignKey(Inventaire, null=True, blank=False, on_delete=models.SET_NULL)
    STATUT_POMPE = [
        ('A', 'Active'),
        ('S', 'En Stock'),
        ('R', 'En réparation'),
        ('P', 'En panne'),
    ]
    statut = models.CharField(max_length=1, choices=STATUT_POMPE, default='', verbose_name="Etat actuel de la pompe")
    huile = models.ForeignKey(Huile, null=True, blank=True, on_delete=models.SET_NULL)
    equipe = models.ForeignKey(ModelEquipe, null=True, blank=True, on_delete=models.SET_NULL)
    vidange = models.DateField(default=date.today, verbose_name="Date de la prochaine vidange", blank=True, null=True)
    historique = models.TextField(blank=True, null=True, max_length=500, verbose_name="historique de la pompe")

    def __str__(self):
        return self.num_serie


class Kit(models.Model):

    image = models.ImageField(upload_to='kit_img/', max_length=254, blank=True, null=True)
    nom = models.CharField(default='', max_length=50, verbose_name="Nom du kit")
    fabriquant = models.ForeignKey(Fabriquant, null=True, blank=False, verbose_name='Fabriquant', related_name="Fabriquant", on_delete=models.SET_NULL)
    date_maj = models.DateField(default=date.today, verbose_name="Date de mise à jour du stock", blank=True, null=True)
    ref_fab = models.CharField(max_length=50, default='', verbose_name="Référence Fabriquant", blank=True, null=True)
    revendeur = models.ForeignKey(Fabriquant, null=True, blank=True,  verbose_name='Revendeur', related_name="Revendeur", on_delete=models.SET_NULL)
    ref_rev = models.CharField(max_length=50, default='', verbose_name="Référence Revendeur", blank=True, null=True)
    quantite = models.DecimalField(default=0, max_digits=5, decimal_places=0, verbose_name="Quantité en stock")
    piece = models.ForeignKey(Piece, null=True, blank=True, on_delete=models.SET_NULL)
    information = models.TextField(blank=True, null=True, max_length=200, verbose_name="Information(s) complémentaire")


    def __str__(self):
        return self.nom


class PiecesPompe(models.Model):
    image = models.ImageField(upload_to='piecepompe_img/', max_length=254, blank=True, null=True)
    nom = models.CharField(default='', max_length=50, verbose_name="Nom de la pièce détachée")
    date_maj = models.DateField(default=date.today, verbose_name="Date de mise à jour du stock", blank=True, null=True)
    fabriquant = models.ForeignKey(Fabriquant, null=True, blank=False, on_delete=models.SET_NULL)
    piece = models.ForeignKey(Piece, null=True, blank=True, on_delete=models.SET_NULL)
    quantite = models.DecimalField(default=0, max_digits=5, decimal_places=0, verbose_name="Quantité en stock")
    information = models.TextField(blank=True, null=True, max_length=200, verbose_name="Information(s) complémentaire(s)")


    def __str__(self):
        return self.nom

