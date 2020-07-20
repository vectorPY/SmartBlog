from django.urls import path
from .views import (ban_view,
                    exemption_request_view,
                    warn_user_view,
                    ban_part_of_blog_view)

urlpatterns = [
    path('banUser/<str:user>/', ban_view, name="ban_view"),
    path('exempReq/<str:user>/', exemption_request_view, name="exemption_request"),
    path('warn/<str:user>/', warn_user_view, name="warn_user"),
    path('banPart/<str:user>/', ban_part_of_blog_view, name="ban_user_from_part_of_blog")
]


