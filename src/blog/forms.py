from django import forms
from ckeditor.widgets import CKEditorWidget

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
    shortVersion = forms.CharField(widget=forms.Textarea)
    text = forms.CharField(widget=CKEditorWidget)
    image = forms.ImageField()

    def clean_author(self):
        author = self.cleaned_data.get('author')
        if len(author) > 150:
            raise forms.ValidationError("Your name is too long")
        elif len(author) < 5:
            raise forms.ValidationError("Your name is too short")
        else:
            return author

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) > 150:
            raise forms.ValidationError("Your title is too long")
        elif len(title) < 5:
            raise forms.ValidationError("Your title is too short")
        else:
            return title

    def clean_shortVersion(self):
        short = self.cleaned_data.get('shortVersion')
        if len(short) > 600:
            raise forms.ValidationError("The description is too long")
        else:
            return short

    def clean_section(self):
        section = self.cleaned_data.get('section')
        if section not in sections:
            raise forms.ValidationError("This section is not available")
        else:
            return section
