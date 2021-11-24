"""URL Configuration"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.views.generic import TemplateView
from django.conf.urls.static import static




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('apps.users.urls', 'users'), namespace='users')),    
    path('', include(('apps.import_excel.urls', 'import_excel'), namespace='import_excel')),    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [

        path('__debug__/', include(debug_toolbar.urls)),
    ]
