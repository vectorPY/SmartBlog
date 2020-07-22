from django.urls import path
from .views import create_idea

urlpatterns = [
    path('createIdea/', create_idea, name="create_an_idea")
]