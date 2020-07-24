from django.urls import path
from .views import (create_idea,
                    idea_list,
                    delete_idea)

urlpatterns = [
    path('create/', create_idea, name="create_an_idea"),
    path('', idea_list, name="lists_the_ideas"),
    path('delete/<int:pk>/', delete_idea, name="delete_an_idea")
]