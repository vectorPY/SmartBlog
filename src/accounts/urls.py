from django.urls import path
from .views import (ban_view,
                    exemption_request_view,
                    warn_user_view)

urlpatterns = [
    path('banUser/<str:user>/', ban_view, name="ban_view"),
    path('exempReq/<str:user>/', exemption_request_view, name="exemption_request"),
    path('warn/<str:user>/', warn_user_view, name="warn_user")
]
