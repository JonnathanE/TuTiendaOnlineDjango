from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from apps.WebApp import views

urlpatterns = [
    path("", views.home, name="Home"),
    path("store", views.store, name="Store"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
