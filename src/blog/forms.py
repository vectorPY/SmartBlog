from django import forms
from .models import Blog


class RawBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['author', 'title', 'section', 'short_version', 'text', 'image']

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

