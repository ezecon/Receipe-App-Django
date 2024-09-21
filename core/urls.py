from django.contrib import admin
from django.urls import path
from vegetable.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('receipes/', receipes, name="receipes"),
    path('delete-receipe/<id>', delete_receipe, name="delete-receipe"),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# This is already included in the Django staticfiles app; no need to add it here unless you have custom static files.
# urlpatterns += staticfiles_urlpatterns()
