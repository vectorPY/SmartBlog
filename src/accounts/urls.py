from django.urls import path
from .views import ban_view

urlpatterns = [
    path('banUser/<str:user>/', ban_view, name="ban_view"),
]
