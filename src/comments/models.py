from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_content(value: str):
    if len(value) > 1800:
        raise ValidationError(
            _('%(value)s (name) is too long'),
            params={'value': value},
        )


def validate_reason(value: str):
    if len(value) < 7:
        raise ValidationError(
            _('%(value)s (name) is too short'),
            params={'value': value},
        )


# Create your models here.
class Comment(models.Model):
    user = models.CharField(max_length=115)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=1800, validators=[validate_content])
    likes = models.IntegerField(default=0)
    article = models.IntegerField(default=0)


class DeleteComment(models.Model):
    deleted_by = models.CharField(max_length=115)
    timestamp = models.DateTimeField(auto_now_add=True)
    reason = models.CharField(max_length=415, validators=[validate_reason])


class ReportComment(models.Model):
    reporter = models.CharField(max_length=115)
    timestamp = models.DateTimeField(auto_now_add=True)
    reason = models.CharField(max_length=415, validators=[validate_reason])
    comment = models.IntegerField(default=0)
    done = models.BooleanField(default=False)


class ReplyComment(models.Model):
    author = models.CharField(max_length=115)
    replied_to = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=1915)
    likes = models.IntegerField(default=0)


class DeleteReply(models.Model):
    deleted_by = models.CharField(max_length=115)
    timestamp = models.DateTimeField(auto_now_add=True)
    reason = models.CharField(max_length=415, validators=[validate_reason])
