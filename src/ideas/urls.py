from django.urls import path
from .views import (create_idea,
                    idea_list)

urlpatterns = [
    path('createIdea/', create_idea, name="create_an_idea"),
    path('ideas/', idea_list, name="lists_the_ideas")
]