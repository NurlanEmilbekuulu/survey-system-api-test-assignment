from django.contrib import admin
from django.urls import path, include

from .swagger import urlpatterns as doc_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('surveys.urls'), name='api'),
]

urlpatterns += doc_urls
