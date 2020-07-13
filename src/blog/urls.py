from django.urls import path
from .views import (home,
                    ArticleList,
                    create_blog,
                    full_blog,
                    Edit,
                    apply_author,
                    delete_view,
                    dashboard,
                    user_dashboard,
                    one_user_dashboard)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/', home, name="homepage"),
    path('', home, name="homepage (root)"),
    path('articles/', ArticleList.as_view(), name="list_articles"),
    path('create/', create_blog, name="create_article"),
    path('blog/<int:my_id>', full_blog, name="full_blog"),
    path('edit/<int:pk>', Edit.as_view(), name="Edit-blog"),
    path('apply/', apply_author, name="Apply_author"),
    path('deleteBlog/<int:pk>/', delete_view, name="delete_blog"),
    path('dashboard/', dashboard, name="dashboard"),
    path('users/', user_dashboard, name="user_dashboard"),
    path('user/<str:pk>/', one_user_dashboard, name="dashboard_of_one_user")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
