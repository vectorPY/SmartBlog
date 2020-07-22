from django import forms
from .models import Idea
from django.forms.widgets import Textarea


class CreateIdeaForm(forms.ModelForm):
    class Meta:
        model = Idea
        fields = ['subject', 'content']

        widgets = {
            'content': Textarea,
        }

