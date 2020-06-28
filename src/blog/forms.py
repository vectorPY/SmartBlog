from django import forms
from .models import Blog
from django.forms import Select

sections = [
    ('Food', 'Food'),
    ('Gaming', 'Gaming'),
    ('Programming', 'Programming'),
    ('Technology', 'Technology'),
    ('Stories', 'Stories'),
]


class RawBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['author', 'title', 'section', 'short_version', 'text', 'image']

        widgets = {
            'section': Select(choices=sections)
        }


