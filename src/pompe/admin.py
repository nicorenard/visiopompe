from django.contrib import admin
from .models import Pompes, PiecesPompe, Huile, Kit




# Register your models here.
class PompeAdmin(admin.ModelAdmin):
    list_display = ('nom', 'marque', 'localisation_piece', 'statut',  'date_derniere_vidange', 'code_umr', 'mise_en_service', 'manuel')
    search_fields = ('localisation_etage', 'localisation_etage', 'localisation_piece', 'statut', 'date_derniere_vidange')


class PiecesPompeAdmin(admin.ModelAdmin):
    list_display = ('nom', 'marque', 'quantite', 'localisation')
    search_fields = ('marque', 'nom')

class HuileAdmin(admin.ModelAdmin):
    list_display = ('nom', 'quantite', 'marque', 'localisation')
    search_fields = ('nom', 'localisation')


class KitAdmin(admin.ModelAdmin):
    list_display = ('nom', 'reference_marque', 'reference_revendeur', 'localisation')
    search_fields = ('nom', 'localisation', 'reference_marque')


admin.site.register(Pompes, PompeAdmin)
admin.site.register(PiecesPompe, PiecesPompeAdmin)
admin.site.register(Huile, HuileAdmin)
admin.site.register(Kit, KitAdmin)

