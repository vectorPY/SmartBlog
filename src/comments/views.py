from django.shortcuts import render
from .forms import CommentForm


# Create your views here.
def comment_view(response):
    form = CommentForm()
    context = {
        "form": form
    }
    return render(response, "comment.html", context)
