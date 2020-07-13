from django import forms
from .models import (Comment,
                     DeleteComment,
                     ReportComment,
                     ReplyComment,
                     DeleteReply)
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


class ReportCommentForm(forms.ModelForm):
    class Meta:
        model = ReportComment
        fields = ['reason']

        widgets = {
            'reason': Textarea,
        }


class ReplyCommentForm(forms.ModelForm):
    class Meta:
        model = ReplyComment
        fields = ['content']

        widgets = {
            'content': Textarea,
        }


class DeleteReplyForm(forms.ModelForm):
    class Meta:
        model = DeleteReply
        fields = ['reason']

        widgets = {
            'reason': Textarea,
        }
