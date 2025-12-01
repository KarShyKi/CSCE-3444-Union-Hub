from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static  # for media files


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('formapp.urls')),  # your app URLs
]

# Serve media files in development mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
