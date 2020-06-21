from django.urls import path
from .views import home, ArticleList

urlpatterns = [
    path('home/', home),
    path('', home),
    path('articles/', ArticleList.as_view(), name="list_articles")
]
