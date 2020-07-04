from django import forms
from .models import Comment, DeleteComment
from django.forms import Textarea


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

        widgets = {
            'content': Textarea,
        }


class DeleteCommentForm(forms.ModelForm):
    class Meta:
        model = DeleteComment
        fields = ['reason']

        widgets = {
            'reason': Textarea,
        }