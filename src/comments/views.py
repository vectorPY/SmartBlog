from django.shortcuts import (render,
                              redirect)
from .forms import (CommentForm,
                    DeleteCommentForm,
                    ReportCommentForm,
                    ReplyCommentForm)
from blog.models import Blog
from .models import Comment, ReplyComment
from django.core.mail import send_mail


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


def report_comment(response, pk):
    obj = Comment.objects.filter(pk=pk).first()
    if response.method == 'POST':
        form = ReportCommentForm(response.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.reporter = response.user
            instance.comment = pk
            instance.save()

            reporter: str = form.cleaned_data['reporter']
            comment: str = str(form.cleaned_data['comment'])
            reason: str = form.cleaned_data['reason']
            email: str = "muellergoldmann@gmail.com"
            msg: str = reporter + " " + "reported the comment" + " " + comment + " because of" + reason

            send_mail(
                "Reported Comment",
                msg,
                email,
                ["vector.thedev@gmail.com"],
                fail_silently=False
            )

            print("DEBUG: Sent!")

            return redirect("../../home")

    else:
        form = DeleteCommentForm()

    context = {
        "form": form,
        "obj": obj
    }
    return render(response, "report.html", context)


def reply_comment(response, pk):
    comment = Comment.objects.filter(pk=pk).first()
    blog = Blog.objects.filter(pk=comment.article).first()
    if response.method == 'POST':
        form: ReplyCommentForm = ReplyCommentForm(response.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = response.user
            instance.replied_to = pk
            instance.save()

            return redirect(f"../../blog/{blog.id}")

    else:
        form = ReplyCommentForm()

    context = {
        "form": form,
        "comment": comment
    }

    return render(response, "reply_comment.html", context)


def delete_reply(response, pk):
    reply = ReplyComment.objects.filter(pk=pk).first()

    if response.method == 'POST':
        form: DeleteCommentForm = DeleteCommentForm(response.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.deleted_by = response.user

            instance.save()

            reply.delete()

            return redirect("../../articles")

    else:
        form: DeleteCommentForm = DeleteCommentForm(response.POST)

    context = {
        "form": form
    }

    return render(response, "", context)


