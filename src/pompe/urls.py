from django.urls import path
from . import views

app_name = 'pompe'

urlpatterns = [
    path('', views.index, name="homepage"),
    path('pompe/', views.index, name="pompe"),
    path('versionapp/', views.version, name="version")

]
