from django.contrib import admin
from .models import Pompes, PiecesPompe, Huile, Kit




# Register your models here.
class PompeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Pompes._meta.get_fields()]
    search_fields = ('localisation_etage', 'localisation_etage', 'localisation_piece', 'statut', 'date_derniere_vidange')


class PiecesPompeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PiecesPompe._meta.get_fields()]
    search_fields = ('marque', 'nom')

class HuileAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Huile._meta.get_fields()]
    search_fields = ('nom', 'localisation')


class KitAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Kit._meta.get_fields()]
    search_fields = ('nom', 'localisation', 'reference_marque')


admin.site.register(Pompes, PompeAdmin)
admin.site.register(PiecesPompe, PiecesPompeAdmin)
admin.site.register(Huile, HuileAdmin)
admin.site.register(Kit, KitAdmin)

