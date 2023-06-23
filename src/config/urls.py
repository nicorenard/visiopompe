from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .settings import DEBUG

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('pompe.urls', 'pompe'), namespace='pompe')),


] \

if DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# valable que dans le serveur de dev pas en production.
