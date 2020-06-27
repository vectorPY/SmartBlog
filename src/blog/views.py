from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Blog
from .forms import RawBlogForm


# Create your views here.
def home(response):
    return render(response, "home.html", {})


class ArticleList(ListView):
    template_name = 'Blog_list.html'
    queryset = Blog.objects.all()


def create_blog(response):
    if response.method == 'POST':
        form = RawBlogForm(response.POST, response.FILES)

        if form.is_valid():
            instance = form.save()

    else:
        form = RawBlogForm()

    context = {
        "form": form
    }
    return render(response, "create_blog.html", context)


def full_blog(response, my_id):
    blog = Blog.objects.filter(id=my_id)

    context = {
        "blog": blog
    }
    return render(response, "full_blog.html", context)


def edit_blog(response, my_id):
    blog = Blog.objects.filter(id=my_id)

    if response.method == "POST":
        form = RawBlogForm(response.POST, instance=blog)