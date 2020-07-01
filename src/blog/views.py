from django.shortcuts import render, redirect
from django.views.generic import ListView, UpdateView
from .models import Blog
from .forms import RawBlogForm, MessageFrom
from django.urls import reverse_lazy
from django.core.mail import send_mail


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


class Edit(UpdateView):
    model = Blog
    form_class = RawBlogForm
    template_name = "blog_edit.html"
    success_url = reverse_lazy('list_articles')


def apply_author(response):
    form = MessageFrom()

    if response.method == 'POST':
        form = MessageFrom(response.POST)

        if form.is_valid():
            reason: str = form.cleaned_data['reason']
            interested_in: str = form.cleaned_data['interested_in']
            additional: str = form.cleaned_data['additional']
            name: str = form.cleaned_data['name']
            email: str = "muellergoldmann@gmail.com"
            msg: str = name + " " + interested_in + " " + additional

            send_mail(
                reason,
                msg,
                email,
                ["vector.thedev@gmail.com"],
                fail_silently=False,
            )
    else:
        form = MessageFrom()

    context = {
        "form": form,
    }

    return render(response, "message.html", context)
