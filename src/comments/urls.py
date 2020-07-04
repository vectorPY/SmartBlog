from django.urls import path
from .views import comment_view, delete_comment

urlpatterns = [
    path('comment/<int:pk>/', comment_view, name="create_comment"),
    path('deleteComment/<int:pk>/', delete_comment, name="delete_comment")
]
