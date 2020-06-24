from django.urls import path
from .views import home, ArticleList, CreateView

urlpatterns = [
    path('home/', home),
    path('', home),
    path('articles/', ArticleList.as_view(), name="list_articles"),
    path('create/', CreateView.as_view(), name="create_article"),
]
