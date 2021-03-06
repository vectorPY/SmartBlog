from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_reason(value: str):
    if len(value) < 15:
        raise ValidationError(
            _('%(value)s (reason) is too short'),
            params={'value': value},
        )


# Create your models here.
class Banned(models.Model):
    banned_by = models.CharField(max_length=115)
    user = models.CharField(max_length=115)
    reason = models.CharField(max_length=415, validators=[validate_reason])
    timestamp = models.DateTimeField(auto_now_add=True)


class ExemptionRequest(models.Model):
    user = models.CharField(max_length=115)
    banned_by = models.CharField(max_length=115, default="vector")
    reason = models.CharField(max_length=1500, validators=[validate_reason])
    timestamp = models.DateTimeField(auto_now_add=True)


class WarnUser(models.Model):
    user = models.CharField(max_length=115)
    warned_by = models.CharField(max_length=115)
    reason = models.CharField(max_length=1500, validators=[validate_reason])
    timestamp = models.DateTimeField(auto_now_add=True)


class BanFromPartOfBlog(models.Model):
    user = models.CharField(max_length=115)
    banned_by = models.CharField(max_length=115)
    part = models.CharField(max_length=100)
    reason = models.CharField(max_length=1500)
    timestamp = models.DateTimeField(auto_now_add=True)
