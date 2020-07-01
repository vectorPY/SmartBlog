from django.urls import path
from .views import comment_view

urlpatterns = [
    path("comment/", comment_view, name="create_comment"),
]
