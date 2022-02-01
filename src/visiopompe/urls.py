from django.contrib import admin
from django.urls import path, include
from .views import index
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='homepage'),
    path('pompe/', include(('pompe.urls', 'pompe'), namespace='pompe')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# valable que dans le serveur de dev pas en production.
