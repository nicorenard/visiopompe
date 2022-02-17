from django.urls import path
from . import views

app_name = 'pompe'

urlpatterns = [
    path('', views.index, name="homepage"),
    path('versionapp/', views.version, name="version"),
    path('pompes/', views.pompe, name="pompe"),
    path('fichepompe/', views.fichepompe, name="fiche_pompe"),
    path('pieces_detaches/', views.pdetache, name="piece"),
    path('kits/', views.kit, name="kit"),
    path('huiles/', views.huile, name="huile"),
    path('docs/', views.doc, name="doc"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('dashboard/equipe', views.equipe, name="equipe"),
    path('dashboard/lieux', views.piece, name="lieux"),
    path('dashboard/fabriquant', views.fabriquant, name="fabriquant"),
    path('stock_add/', views.add_stockpompe, name="add_pompe"),
    path('stock_edit/<int:pk>/', views.update_stockpompe, name="pompe_edit"),
    path('stock_delete/<int:pk>/', views.delete_stockpompe, name="pompe_delete"),
    path('fichepompe_add/', views.add_fichepompe, name="add_fichepompe"),
    path('fichepompe_edit/<int:pk>/', views.update_fichepompe, name="fichepompe_edit"),
    path('inventaire/', views.inventaire, name="inventaire"),
    #path('pompes/inventaire_edit/<int:pk>/', view.update_inventaire, name="inventaire_edit"),
    path('pdetache_add/', views.add_pdetache, name="add_pdetache"),
    path('pdetache_edit/<int:pk>/', views.update_pdetache, name="pdetache_edit"),
    path('kit_add/', views.add_kit, name="add_kit"),
    path('kit_edit/<int:pk>/', views.update_kit, name="kit_edit"),
    path('huile_add/', views.add_huile, name="add_huile"),
    path('huile_edit/<int:pk>/', views.update_huile, name="huile_edit"),
    path('doc_add/', views.add_doc, name="add_doc"),
    path('doc_edit/<int:pk>/', views.update_doc, name="doc_edit"),
    path('dashboard/equipe_add/', views.add_equipe, name="add_equipe"),
    #path('dashboard/equipe_edit/<int:pk>/', views.update_equipe, name="equipe_edit"),
    path('site_add/', views.add_site, name="add_site"),
    #path('site_edit/<int:pk>/', views.update_site, name="site_edit"),
    path('batiment_add/', views.add_batiment, name="add_batiment"),
    # path('batiment_edit/<int:pk>/', views.update_batiment, name="batiment_edit"),
    path('etage_add/', views.add_piece, name="add_etage"),
    # path('etage_edit/<int:pk>/', views.update_etage, name="etage_edit"),
    path('piece_add/', views.add_piece, name="add_piece"),
    # path('piece_edit/<int:pk>/', views.update_piece, name="piece_edit"),
    path('fabriquant_add/', views.add_fabriquant, name="add_fabriquant"),
    #path('fabriquant_edit/<int:pk>/', views.update_fabriquant, name="fabriquant_edit"),


]
