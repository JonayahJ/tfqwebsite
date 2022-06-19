# Website URLs
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# Wagtail dependencies
from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')), # Blog URLs
    # path('contact/', include('contact.urls')), # Contact URLs
    
    # Wagtail paths
    path('cms/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),
    path('pages/', include(wagtail_urls)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
