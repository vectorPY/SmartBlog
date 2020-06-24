from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Blog


# Create your views here.
def home(response):
    return render(response, "home.html", {})


class ArticleList(ListView):
    template_name = 'Blog_list.html'
    queryset = Blog.objects.all()


class CreateArticle(CreateView):
    template_name = 'create_list.html'
    model = Blog
    queryset = Blog.objects.all()
    fields = '__all__'
