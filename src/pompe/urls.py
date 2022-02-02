from django.urls import path
from . import views

app_name = 'pompe'

urlpatterns = [
    path('', views.index, name="homepage"),
    path('pompes/', views.pompe, name="pompe"),
    path('pieces_detaches/', views.piece, name="piece"),
    path('kits/', views.kit, name="kit"),
    path('huiles/', views.huile, name="huile"),
    path('docs/', views.doc, name="doc"),
    path('versionapp/', views.version, name="version"),
    path('dashboard/', views.dashboard, name="dashboard"),

]
