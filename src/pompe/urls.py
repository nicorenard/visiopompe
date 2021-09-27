from django.contrib import admin
from django.urls import path
from . import views


app_name = 'pompe'

urlpatterns = [
    path('', views.index, name="index"),
    path('huiles/', views.huile, name="huiles"),
    path('pieces/', views.piece, name="pieces"),
    path('kit/', views.kit, name="kit"),

]