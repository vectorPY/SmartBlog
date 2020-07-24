from django.contrib import admin
from .models import Idea, DeleteIdea

# Register your models here.
admin.site.register(Idea)
admin.site.register(DeleteIdea)

