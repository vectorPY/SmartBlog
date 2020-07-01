from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_content(value: str):
    if len(value) > 1800:
        raise ValidationError(
            _('%(value)s (name) is too long'),
            params={'value': value},
        )


# Create your models here.
class Comment(models.Model):
    user = models.CharField(max_length=115)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=1800, validators=[validate_content])
    likes = models.IntegerField(default=0)

