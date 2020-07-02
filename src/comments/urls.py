from django.urls import path
from .views import comment_view

urlpatterns = [
    path('comment/<int:pk>/', comment_view, name="create_comment"),
]
