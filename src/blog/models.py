from django.db import models
from ckeditor.fields import RichTextField
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_name(value: str):
    if len(value) <= 5:
        raise ValidationError(
            _('%(value)s (name) is too short'),
            params={'value': value},
        )
    elif len(value) >= 115:
        raise ValidationError(
            _('%(value)s (name) is too long'),
            params={'value': value},
        )


def validate_title(value: str):
    if len(value) > 250:
        raise ValidationError(
            _('%(value)s (title) is too long'),
            params={'value': value},
        )
    elif len(value) < 7:
        raise ValidationError(
            _('%(value)s (title) is too short'),
            params={'value': value},
        )


def validate_shortversion(value: str):
    if len(value) < 15:
        raise ValidationError(
            _('%(value)s (desctiption) is too short'),
            params={'value': value},
        )


# Create your models here.
class Blog(models.Model):
    author = models.CharField(max_length=115, validators=[validate_name])
    title = models.CharField(max_length=250, validators=[validate_title])
    timestamp = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    section = models.CharField(max_length=115)
    dislikes = models.IntegerField(default=0)
    short_version = models.CharField(max_length=1155, validators=[validate_shortversion])
    text = RichTextField(blank=True, null=True)
    image = models.ImageField(blank=True, upload_to="")
