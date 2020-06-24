from django.shortcuts import render
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
        form = RawBlogForm(response.POST)

        if form.is_valid():
            author = form.cleaned_data['author']
            title = form.cleaned_data['title']
            section = form.cleaned_data['section']
            short_version = form.cleaned_data['shortVersion']
            text = form.cleaned_data['text']
            image = form.cleaned_data['image']

            blog = Blog(author=author, title=title, section=section, short_version=short_version, text=text, image=image)

            blog.save()

            form = RawBlogForm
    else:
        form = RawBlogForm()

    context = {
        "form": form
    }
    return render(response, "create_blog.html", context)
