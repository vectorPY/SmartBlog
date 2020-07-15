from django.urls import path
from .views import ban_view, exemption_request_view

urlpatterns = [
    path('banUser/<str:user>/', ban_view, name="ban_view"),
    path('exempReq/<str:user>/', exemption_request_view, name="exemption_request")
]
