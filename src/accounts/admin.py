from django.contrib import admin
from .models import Banned, ExemptionRequest

# Register your models here.
admin.site.register(Banned)
admin.site.register(ExemptionRequest)
