from django import forms
from .models import Idea, DeleteIdea
from django.forms.widgets import Textarea


class CreateIdeaForm(forms.ModelForm):
    class Meta:
        model = Idea
        fields = ['subject', 'content']

        widgets = {
            'content': Textarea
        }


class DeleteIdeaForm(forms.ModelForm):
    class Meta:
        model = DeleteIdea
        fields = ['reason']

        widgets = {
            'reason': Textarea
        }
