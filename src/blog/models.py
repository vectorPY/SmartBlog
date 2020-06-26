from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Blog(models.Model):
    author = models.CharField(max_length=115)
    title = models.CharField(max_length=250)
    timestamp = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField()
    section = models.CharField(max_length=115)
    dislikes = models.IntegerField()
    short_version = models.CharField(max_length=1155)
    text = RichTextField(blank=True, null=True)
    image = models.ImageField(blank=True, upload_to="")
