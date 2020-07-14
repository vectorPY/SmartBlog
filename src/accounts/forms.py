from django import forms
from .models import Banned
from django.forms import Textarea


class BannedForm(forms.ModelForm):
    class Meta:
        model = Banned
        fields = ['user', 'reason']

        widgets = {
            'reason': Textarea,
        }

