from django.urls import path

from apps.contact import views

urlpatterns = [
    path("", views.contact, name="Contact"),
    # path("category/<int:category_id>", views.category, name="Category"),
]
