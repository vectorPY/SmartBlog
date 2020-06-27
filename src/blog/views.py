from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, UpdateView
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

            return redirect("../articles")

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


"""
def edit_blog(response, my_id):
    blog = get_object_or_404(Blog, id=my_id)

    if response.method == "POST":
        form = RawBlogForm(response.POST, instance=blog)

        if form.is_valid():
            blog = form.save()
            return redirect(f"../articles/{my_id}")

        else:
            print(form.errors)

    else:
        form = RawBlogForm(response.POST, instance=blog)

    context = {
        "form": form
    }

    return render(response, "blog_edit.html", context)
"""


class Edit(UpdateView):
    model = Blog
    form_class = RawBlogForm
    template_name = "blog_edit.html"
    success_url = '../../articles'
