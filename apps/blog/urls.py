from django.urls import path

from apps.blog import views

urlpatterns = [
    path("", views.blogs, name="Blog"),
    path("category/<int:category_id>", views.category, name="Category"),
]
