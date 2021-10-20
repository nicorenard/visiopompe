from django.urls import path
from . import views


app_name = 'pompe'

urlpatterns = [
    path('', views.index, name="index"),
    path('huiles/', views.huile, name="huiles"),
    path('pieces/', views.piece, name="pieces"),
    path('kit/', views.kit, name="kit"),
    path('forms/', views.ajout_pompe, name="ajout_pompe"),
    path('pompe_edit/<int:pk>/', views.modif_pompe, name="pompe_edit"),

]