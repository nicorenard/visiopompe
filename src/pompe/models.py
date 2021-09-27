from datetime import date
from django.db import models


class Pompes(models.Model):

    image = models.ImageField(upload_to='', max_length=254, blank=True)
    nom = models.CharField(max_length=100, default='')
    marque = models.CharField(max_length=50, default='')
    modele = models.CharField(max_length=20, default='')
    numero_serie = models.CharField(max_length=100, default='')
    puissance = models.DecimalField(default=0, max_digits=2, decimal_places=0)
    nombre_etage = models.DecimalField(default=0, max_digits=2, decimal_places=0)
    vide_teste = models.FloatField(default=0)
    vide_theorique = models.FloatField(default=0)
    phasage_code = [
        ('Mono', 'Monophasé'),
        ('Tri', 'Triphasé'),
    ]
    phasage = models.CharField(max_length=4, choices=phasage_code, default='M')
    code_umr = models.CharField(max_length=100, default='')
    localisation_etage = models.CharField(max_length=10, default='')
    localisation_piece = models.CharField(max_length=10, default='')
    localisation_emplacement = models.CharField(max_length=50, default='')
    mise_en_service = models.DateField(auto_now=date.today)
    statut_pompe = [
        ('A', 'Active'),
        ('S', 'Stockage'),
        ('R', 'En Réparation'),
        ('P', 'En panne'),
            ]
    statut = models.CharField(max_length=1, choices=statut_pompe, default='A')
    date_derniere_vidange = models.DateField(default=date.today)
    huile = models.CharField(max_length=50)
    manuel = models.FileField(upload_to='upload/', max_length=254, default='', blank=True)
    information = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.nom


class PiecesPompe(models.Model):
    nom = models.CharField(max_length=50)
    image = models.ImageField(upload_to='', max_length=254, default='')
    marque = models.CharField(max_length=50)
    type_pompe = models.CharField(max_length=100)
    quantite = models.DecimalField(default=0, max_digits=5, decimal_places=0)
    localisation = models.CharField(max_length=20, default='')
    information = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.nom


class Huile(models.Model):

    nom = models.CharField(max_length=50, default='')
    image = models.ImageField(upload_to='', max_length=254, default='')
    marque = models.CharField(max_length=50, default='')
    type_pompe = models.CharField(max_length=100, default='')
    quantite = models.DecimalField(default=0, max_digits=5, decimal_places=0)
    localisation = models.CharField(max_length=20, default='')
    information = models.TextField(max_length=100, default='')

    def __str__(self):
        return self.nom


class Kit(models.Model):

    nom = models.CharField(max_length=50, default='')
    image = models.ImageField(upload_to='', max_length=254, default='')
    marque = models.CharField(max_length=50, default='')
    reference_marque = models.CharField(max_length=50, default='')
    nom_revendeur = models.CharField(max_length=40, default='')
    reference_revendeur = models.CharField(max_length=50, default='')
    quantite = models.DecimalField(default=0, max_digits=5, decimal_places=0)
    localisation = models.CharField(max_length=20, default='')
    information = models.TextField(max_length=100, default='')

    def __str__(self):
        return self.nom


'''def historique(self, date_h, commentaire_h):
        date_h = models.DateField(auto_now=True)
        commentaire_h = models.TextField(max_length=500)
'''
