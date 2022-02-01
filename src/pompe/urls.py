from django.urls import path
from src.pompe import views

app_name = 'pompe'

urlpatterns = [
    path('', views.index, name="pompe"),
    path('versionapp', views.version, name="version")

]
