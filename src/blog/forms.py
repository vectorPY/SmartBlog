from django import forms
from ckeditor.fields import RichTextField

sections = [
    ("Technology", "Technology"),
    ("Food", "Food"),
    ("Movies", "Movies"),
    ("Gaming", "Gaming"),
    ("Something else", "Something else")
]


class RawBlogForm(forms.Form):
    author = forms.CharField(label='Author:')
    title = forms.CharField(label='Title')
    section = forms.CharField(label='Section', widget=forms.Select(choices=sections))
    shortVersion = forms.TextInput()
    text = RichTextField()
    image = forms.ImageField()

    def clean_author(self):
        author = self.cleaned_data.get('description')
        if len(author) > 150:
            raise forms.ValidationError("Your name is too long")
        elif len(author) < 15:
            raise forms.ValidationError("Your name is too short")
        else:
            return author

