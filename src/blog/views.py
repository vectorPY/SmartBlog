from django.shortcuts import render, redirect
from django.views.generic import ListView, UpdateView
from .models import Blog, DeleteBlog
from .forms import RawBlogForm, MessageFrom, DeleteBlogForm
from django.urls import reverse_lazy
from django.core.mail import send_mail
from comments.models import (Comment,
                             DeleteComment,
                             ReplyComment)
from django.contrib.auth.models import User


# Create your views here.
def home(response):
    return render(response, "home.html", {})


class ArticleList(ListView):
    template_name = 'Blog_list.html'
    queryset = Blog.objects.all()


def create_blog(response):
    users = User.objects.all()
    msg: str = "New blog released!"
    if response.method == 'POST':
        form = RawBlogForm(response.POST, response.FILES)

        if form.is_valid():
            instance = form.save()

            for user in users:
                if user.email is not None:
                    send_mail(
                        "New blog!",
                        msg,
                        "muellergoldmann@gmail.com",
                        ['vector.thedev@gmail.com'],
                        user.email
                    )
                else:
                    continue

            return redirect("../articles")

    else:
        form = RawBlogForm()

    context = {
        "form": form
    }
    return render(response, "create_blog.html", context)


def full_blog(response, my_id):
    blog = Blog.objects.filter(id=my_id)
    comments = Comment.objects.all().filter(article=my_id)
    replies = ReplyComment.objects.all()
    context = {
        "blog": blog,
        "comments": comments,
        "reply": replies,
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


def delete_view(response, pk):
    obj = Blog.objects.filter(pk=pk).first()
    form = DeleteBlogForm()

    if response.method == 'POST':
        form = DeleteBlogForm(response.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.deleted_by = response.user
            instance.save()

            deleted_by: str = form.cleaned_data['deleted_by']
            reason: str = form.cleaned_data['reason']
            msg: str = deleted_by + " " + reason
            email: str = "muellergoldmann@gmail.com"

            send_mail(
                "Your blog has been deleted",
                msg,
                email,
                ["vector.thedev@gmail.com"]
            )

            print("DEBUG: sent!")

            obj.delete()

        return redirect("../../articles")

    context = {
        "obj": obj,
        "form": form
    }
    return render(response, "delete.html", context)


def dashboard(response):
    blogs = Blog.objects.all()
    deleted_blogs = DeleteBlog.objects.all()
    comments = Comment.objects.all()
    deleted_comments = DeleteComment.objects.all()

    context = {
        "blogs": blogs,
        "deleted_blogs": deleted_blogs,
        "comments": comments,
        "deleted_comments": deleted_comments
    }
    return render(response, "dashboard.html", context)


def user_dashboard(response):
    users = User.objects.all()

    context = {
        "users": users,
    }
    return render(response, "user_dashboard.html", context)


