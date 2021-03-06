from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate(value: str):
    if len(value) < 15:
        raise ValidationError(
            _('%(value)s (content   ) is too short'),
            params={'value': value},
        )


# Create your models here.
class Idea(models.Model):
    creator = models.CharField(max_length=115)
    subject = models.CharField(max_length=115, validators=[validate])
    content = models.CharField(max_length=1500, validators=[validate])
    reviewed = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)


class DeleteIdea(models.Model):
    deleted_by = models.CharField(max_length=115)
    reason = models.CharField(max_length=1500, validators=[validate])
    idea = models.IntegerField()
    timestamp = models. DateTimeField(auto_now_add=True)
