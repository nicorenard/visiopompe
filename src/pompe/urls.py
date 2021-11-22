from django.urls import path
from . import views


app_name = 'pompe'

urlpatterns = [
    path('', views.index, name="index"),
    path('versionapp', views.version, name="version"),
    path('huiles/', views.huile, name="huiles"),
    path('pieces/', views.piece, name="pieces"),
    path('kit/', views.kit, name="kit"),
    path('doc/', views.doc, name="docs"),
    path('forms/', views.ajout_pompe, name="ajout_pompe"),
    path('pompe_edit/<int:pk>/', views.modif_pompe, name="pompe_edit"),
    path('pompe_suppression/<int:pk>/', views.suppression_pompe, name="pompe_suppression"),
    path('forms2/', views.ajout_piece, name="ajout_piece"),
    path('piece_edit/<int:pk>/', views.modif_piece, name="piece_edit"),
    path('piece_suppression/<int:pk>/', views.suppression_piece, name="piece_suppression"),
    path('forms3/', views.ajout_huile, name="ajout_huile"),
    path('huile_edit/<int:pk>/', views.modif_huile, name="huile_edit"),
    path('huile_suppression/<int:pk>/', views.suppression_huile, name="huile_suppression"),
    path('forms4/', views.ajout_kit, name="ajout_kit"),
    path('kit_edit/<int:pk>/', views.modif_kit, name="kit_edit"),
    path('kit_suppression/<int:pk>/', views.suppression_kit, name="kit_suppression"),
    path('forms5/', views.ajout_doc, name="ajout_doc"),

]
