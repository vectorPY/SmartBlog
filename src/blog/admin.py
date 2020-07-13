from django.contrib import admin
from .models import Blog, DeleteBlog

# Register your models here.
admin.site.register(Blog)
admin.site.register(DeleteBlog)
