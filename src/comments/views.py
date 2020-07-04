from django.shortcuts import (render,
                              redirect)
from .forms import CommentForm, DeleteCommentForm
from blog.models import Blog
from .models import Comment


# Create your views here.
def comment_view(response, pk):
    obj = Blog.objects.filter(pk=pk).first()
    if response.method == 'POST':
        form = CommentForm(response.POST)
        if form.is_valid():
            instance = form.save(commit=False)

            instance.article = pk
            instance.user = response.user

            instance.save()

            return redirect(f"../../blog/{pk}")
    else:
        form = CommentForm()

    context = {
        "form": form,
        "obj": obj,
    }
    return render(response, "comment.html", context)


def delete_comment(response, pk):
    obj = Comment.objects.filter(pk=pk).first()
    if response.method == 'POST':
        form = DeleteCommentForm(response.POST)

        if form.is_valid():
            instance = form.save(commit=False)

            instance.deleted_by = response.user
            instance.save()

            obj.delete()

            return redirect(f"../../articles")

    else:
        form = DeleteCommentForm()

    context = {
        "form": form,
        "obj": obj,
    }

    return render(response, "delete_comment.html", context)
