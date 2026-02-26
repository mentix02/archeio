from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = (
    [
        path('', include('apps.core.urls')),
        path('user/', include('apps.user.urls')),
        path('storage/', include('apps.storage.urls')),
        path('admin/', admin.site.urls),
    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
