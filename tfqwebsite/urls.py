# Website URLs
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')), # Blog URLs
    # path('contact/', include('contact.urls')), # Contact URLs
]