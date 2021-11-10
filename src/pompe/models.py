from datetime import date
from django.db import models

class Pompes(models.Model):

    image_choix = [
        ('/pompe_img/adixen_pompe.jpg', 'Adixen'),
        ('/pompe_img/alcatel_pompe.jpg', 'Alcatel'),
        ('/pompe_img/edwards_pompe.jpg', 'Edwards'),
        ('/pompe_img/leybold_pompe.jpg', 'Leybold'),
        ('/pompe_img/pfeiffer_pompe.jpg', 'Pfeiffer'),
        ('/pompe_img/vaccubrand_1.jpg', 'Vaccubrand pompe à palettes'),
        ('/pompe_img/vaccubrand_membrane.jpg', 'Vaccubrand pompe à membranes'),
        ('/pompe_img/vaccubrand_pompage.jpg', 'Vaccubrand groupe de pompages'),
        ('/pompe_img/welch_pompe.jpg', 'Welch pompe à palettes'),
        ('/pompe_img/welch_pompe3.jpg', 'Welch groupe de pompages'),
        ('/pompe_img/welch_membrane.jpg', 'Welch pompe à membranes'),
        ('/pompe_img/noimage.jpg', 'Aucune image'),

    ]
    image = models.ImageField(max_length=254, choices=image_choix, blank=True, null=True)
    nom = models.CharField(max_length=100, default='')
    marque_choix = [
        ('Adixen', 'Adixen'),
        ('Alcatel', 'Alcatel'),
        ('Edwards Vacuum', 'Edwards Vacuum'),
        ('Pfeiffer Vacuum', 'Pfeiffer Vacuum'),
        ('Vacuubrand', 'Vacuubrand'),
        ('Welch', 'Welch'),
        ('Autres', 'Autres'),
    ]
    marque = models.CharField(max_length=50, choices=marque_choix, default='', verbose_name="Fabriquant")
    modele = models.CharField(max_length=20, default='', verbose_name="Modèle de la pompe")
    numero_serie = models.CharField(max_length=100, default='')
    puissance_choix = [
        ('50', '50 Hertz'),
        ('60', '60 Hertz'),

    ]
    puissance = models.CharField(default='50', choices=puissance_choix, max_length=2, verbose_name="Puissance du moteur")
    etage_choix = [
        ('0', 'Membranes'),
        ('1', '1 étage'),
        ('2', '2 étages')
    ]
    nombre_etage = models.CharField(max_length=1, choices=etage_choix, default='0', verbose_name="Nombre d'étages")
    vide_teste = models.FloatField(default=0, verbose_name="Vide limite testé")
    vide_theorique = models.FloatField(default=0, verbose_name="Vide limite Fabriquant")
    phasage_code = [
        ('Monophasé', 'Monophasé'),
        ('Triphasé', 'Triphasé'),
    ]
    phasage = models.CharField(max_length=4, choices=phasage_code, default='M', verbose_name="Phasage du moteur électrique")
    code_umr = models.CharField(max_length=100, default='', verbose_name="Codification UMR")
    localisation_choix = [
        ('1er étage', '1er étage'),
        ('2ème étage', '2ème étage'),
        ('3ème étage', '3ème étage'),
    ]
    localisation_etage = models.CharField(max_length=10, default='', verbose_name="Etage", choices=localisation_choix)
    localisation_piece = models.CharField(max_length=10, default='', verbose_name="Pièce")
    localisation_emplacement = models.CharField(max_length=50, default='', verbose_name="Place dans la pièce", blank=True)
    mise_en_service = models.DateField(auto_now=date.today)
    statut_pompe = [
        ('A', 'Active'),
        ('S', 'Stockage'),
        ('R', 'En Réparation'),
        ('P', 'En panne'),
            ]
    statut = models.CharField(max_length=1, choices=statut_pompe, default='A', verbose_name="Etat actuel de la pompe")
    date_derniere_vidange = models.DateField(default=date.today, verbose_name="Date de la dernière vidange")
    huile = models.CharField(max_length=50, verbose_name="Huile utilisée", blank=True)
    manuel = models.FileField(upload_to='upload/', max_length=254, default='', blank=True, verbose_name="Manuel technique")
    information = models.CharField(max_length=100, default='', blank=True)

    def __str__(self):
        return self.nom


class PiecesPompe(models.Model):
    nom = models.CharField(max_length=50)
    image = models.ImageField(upload_to='', max_length=254, blank=True, null=True)
    marque = models.CharField(max_length=50, verbose_name="Fabriquant")
    type_pompe = models.CharField(max_length=100, verbose_name="Modèle de pompe")
    quantite = models.DecimalField(default=0, max_digits=5, decimal_places=0, verbose_name="Stock")
    localisation = models.CharField(max_length=20, default='', verbose_name="Lieux de stockage")
    information = models.CharField(max_length=50, default='', blank=True)

    def __str__(self):
        return self.nom


class Huile(models.Model):

    nom = models.CharField(max_length=50, default='')
    huile_image = [
        ('/huile_img/huile_adixen.jpg', 'Adixen'),
        ('/huile_img/huile_alcatel.jpg', 'Alcatel'),
        ('/huile_img/huile_edwards.jpg', 'Edwards'),
        ('/huile_img/huile_leybold.png', 'Leybold'),
        ('/huile_img/huile_pfeiffer.jpg', 'Pfeiffer'),
        ('/huile_img/huile_vaccubrand.jpg', 'Vaccubrand'),
        ('/huile_img/huile_welch.jpg', 'Welch'),
        ('/huile_img/huile_universelle.jpg', 'Huile universelle'),
        ('/pompe_img/noimage.jpg', 'Aucune image'),

    ]
    image = models.ImageField(choices=huile_image, max_length=254, blank=True, null=True)
    marque = models.CharField(max_length=50, default='', verbose_name="Fabriquant")
    type_pompe = models.CharField(max_length=100, default='', verbose_name="Modèle de pompe")
    quantite = models.DecimalField(default=0, max_digits=5, decimal_places=0, verbose_name="Stock")
    localisation = models.CharField(max_length=20, default='', verbose_name="Lieux de stockage")
    information = models.TextField(max_length=100, default='', blank=True)

    def __str__(self):
        return self.nom


class Kit(models.Model):

    nom = models.CharField(max_length=50, default='')
    image = models.ImageField(upload_to='', max_length=254, blank=True, null=True)
    marque = models.CharField(max_length=50, default='', verbose_name="Fabriquant")
    reference_marque = models.CharField(max_length=50, default='', verbose_name="Référence Fabriquant")
    nom_revendeur = models.CharField(max_length=40, default='', verbose_name="Révendeur")
    reference_revendeur = models.CharField(max_length=50, default='', verbose_name="Référence Revendeur")
    quantite = models.DecimalField(default=0, max_digits=5, decimal_places=0, verbose_name="Stock")
    localisation = models.CharField(max_length=20, default='', verbose_name="Lieux de stockage")
    information = models.TextField(max_length=100, default='', blank=True)

    def __str__(self):
        return self.nom


'''def historique(self, date_h, commentaire_h):
        date_h = models.DateField(auto_now=True)
        commentaire_h = models.TextField(max_length=500)
'''
