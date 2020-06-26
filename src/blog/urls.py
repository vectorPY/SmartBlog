from django.urls import path
from .views import home, ArticleList, create_blog, full_blog
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/', home, name="homepage"),
    path('', home, name="homepage (root)"),
    path('articles/', ArticleList.as_view(), name="list_articles"),
    path('create/', create_blog, name="create_article"),
    path('blog/<int:my_id>', full_blog),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
