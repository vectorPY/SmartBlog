from django.contrib import admin
from .models import (Comment,
                     DeleteComment,
                     ReportComment,
                     ReplyComment,
                     DeleteReply)


# Register your models here.
admin.site.register(Comment)
admin.site.register(DeleteComment)
admin.site.register(ReportComment)
admin.site.register(ReplyComment)
admin.site.register(DeleteReply)

