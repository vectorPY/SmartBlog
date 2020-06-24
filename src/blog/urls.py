from django.urls import path
from .views import home, ArticleList, create_blog

urlpatterns = [
    path('home/', home),
    path('', home),
    path('articles/', ArticleList.as_view(), name="list_articles"),
    path('create/', create_blog, name="create_article"),
]
