from django.urls import path
from . import views

app_name = 'pompe'

urlpatterns = [
    path('', views.index, name="homepage"),
    path('versionapp/', views.version, name="version"),
    path('pompes/', views.pompe, name="pompe"),
    path('fichepompe/', views.fichepompe, name="fiche_pompe"),
    path('pieces_detaches/', views.pdetache, name="pdetache"),
    path('kits/', views.kit, name="kit"),
    path('huiles/', views.huile, name="huile"),
    path('docs/', views.doc, name="doc"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('fabriquants/', views.fabriquant, name="fabriquant"),
    path('fabriquant_add/', views.add_fabriquant, name="add_fabriquant"),
    path('fabriquant_edit/<int:pk>/', views.update_fabriquant, name="fabriquant_edit"),
    path('fabriquant_edit/<int:pk>/', views.delete_fabriquant, name="fabriquant_delete"),
    path('stock_add/', views.add_stockpompe, name="add_pompe"),
    path('stock_edit/<int:pk>/', views.update_stockpompe, name="pompe_edit"),
    path('stock_delete/<int:pk>/', views.delete_stockpompe, name="pompe_delete"),
    path('fichepompe_add/', views.add_fichepompe, name="add_fichepompe"),
    path('fichepompe_edit/<int:pk>/', views.update_fichepompe, name="fichepompe_edit"),
    path('fichepompe_delete/<int:pk>/', views.delete_fichepompe, name="fichepompe_delete"),
    path('inventaire/', views.inventaire, name="inventaire"),
    path('pompes/inventaire_edit/<int:pk>/', views.update_inventaire, name="inventaire_edit"),
    path('pompes/inventaire_delete/<int:pk>/', views.delete_inventaire, name="inventaire_delete"),
    path('pdetache_add/', views.add_pdetache, name="add_pdetache"),
    path('pdetache_edit/<int:pk>/', views.update_pdetache, name="pdetache_edit"),
    path('pdetache/<int:pk>/', views.delete_pdetache, name="pdetache_delete"),
    path('kit_add/', views.add_kit, name="add_kit"),
    path('kit_edit/<int:pk>/', views.update_kit, name="kit_edit"),
    path('kit_delete/<int:pk>/', views.delete_kit, name="kit_delete"),
    path('huile_add/', views.add_huile, name="add_huile"),
    path('huile_edit/<int:pk>/', views.update_huile, name="huile_edit"),
    path('huile_delete/<int:pk>/', views.delete_huile, name="huile_delete"),
    path('doc_add/', views.add_doc, name="add_doc"),
    path('doc_edit/<int:pk>/', views.update_doc, name="doc_edit"),
    path('doc_delete/<int:pk>/', views.delete_doc, name="doc_delete"),
    path('dashboard/equipe', views.equipe, name="equipe"),
    path('dashboard/lieux', views.piece, name="lieux"),
    path('dashboard/equipe_edit/<int:pk>/', views.update_equipe, name="equipe_edit"),
    path('dashboard/equipe_delete/<int:pk>/', views.delete_equipe, name="equipe_delete"),
    # path('site_edit/<int:pk>/', views.update_site, name="site_edit"),
    # path('batiment_edit/<int:pk>/', views.update_batiment, name="batiment_edit"),
    # path('etage_edit/<int:pk>/', views.update_etage, name="etage_edit"),
    path('dashboard/piece_edit/<int:pk>/', views.update_piece, name="piece_edit"),
    path('dashboard/piece_delete/<int:pk>/', views.delete_piece, name="piece_delete"),


]
