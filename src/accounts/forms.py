from django import forms
from .models import Banned, ExemptionRequest
from django.forms import Textarea


class BannedForm(forms.ModelForm):
    class Meta:
        model = Banned
        fields = ['user', 'reason']

        widgets = {
            'reason': Textarea,
        }


class ExemptionRequestForm(forms.ModelForm):
    class Meta:
        model = ExemptionRequest
        fields = ['reason']

        widgets = {
            'reason': Textarea,
        }
