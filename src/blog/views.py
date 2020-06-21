from django.shortcuts import render
from django.views.generic import ListView
from .models import Blog


# Create your views here.
def home(response):
    return render(response, "home.html", {})


class ArticleList(ListView):
    template_name = ''
    queryset = Blog.objects.all()
