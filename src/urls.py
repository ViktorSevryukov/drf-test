from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('apps.clients.urls', namespace='clients')),
    path('admin/', admin.site.urls),
    path('auth/', include('apps.auth_core.urls', namespace='auth')),
    path('api/v1/clients/', include('apps.clients.urls.api', namespace='clients_api'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
