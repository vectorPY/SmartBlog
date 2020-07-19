from django import forms
from .models import (Banned,
                     ExemptionRequest,
                     WarnUser,
                     BanFromPartOfBlog)
from django.forms import Textarea, Select

parts = [
        ('Comments', 'Comments'),
        ('Write', 'Write'),
        ('Read', 'Read'),
]


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


class WarnUserForm(forms.ModelForm):
    class Meta:
        model = WarnUser
        fields = ['reason']

        widgets = {
            'reason': Textarea,
        }


class BanFromPartOfBlogForm(forms.ModelForm):
    class Meta:
        model = BanFromPartOfBlog
        fields = ['part', 'reason']

        widgets = {
            'reason': Textarea,
            'part': Select(choices=parts)
        }
