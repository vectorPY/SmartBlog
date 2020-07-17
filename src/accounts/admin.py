from django.contrib import admin
from .models import (Banned,
                     ExemptionRequest,
                     WarnUser)


# Register your models here.
admin.site.register(Banned)
admin.site.register(ExemptionRequest)
admin.site.register(WarnUser)
