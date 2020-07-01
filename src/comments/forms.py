from django import forms
from .models import Comment
from django.forms import Textarea


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

        widgets = {
            'content': Textarea,
        }

