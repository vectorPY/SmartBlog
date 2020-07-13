from django.urls import path
from .views import comment_view, delete_comment, report_comment, reply_comment

urlpatterns = [
    path('comment/<int:pk>/', comment_view, name="create_comment"),
    path('deleteComment/<int:pk>/', delete_comment, name="delete_comment"),
    path('reportComment/<int:pk>/', report_comment, name="report_comment"),
    path('replyComment/<int:pk>/', reply_comment, name="reply_comment")
]
