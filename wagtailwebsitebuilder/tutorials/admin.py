from django.contrib import admin

from .models import Tutorial, Batch, BatchEnrollee


admin.site.register(Tutorial)
admin.site.register(Batch)
admin.site.register(BatchEnrollee)
