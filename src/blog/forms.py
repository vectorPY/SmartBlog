from django import forms
from .models import Blog, DeleteBlog
from django.forms import Select, Textarea

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


class MessageFrom(forms.Form):
    name = forms.CharField(label='Enter your name: ')
    reason = forms.CharField(label='Your reason: ')
    interested_in = forms.CharField(label="Interested in: ", widget=forms.Select(choices=sections))
    additional = forms.CharField(widget=forms.Textarea)

    def clean_reason(self):
        reason = self.cleaned_data.get('reason')
        if len(reason) > 250:
            raise forms.ValidationError("Your reason is too long")
        elif len(reason) < 8:
            raise forms.ValidationError("You have to enter a longer reason or you won't get the author permisson")
        else:
            return reason


class DeleteBlogForm(forms.ModelForm):
    class Meta:
        model = DeleteBlog
        fields = ['reason']

        widgets = {
            "reason": Textarea,
        }

