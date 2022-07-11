from django.contrib import admin
from .models import Schedule,ConsultantStatus,LawyerStatus
# Register your models here.

admin.site.register(Schedule)
admin.site.register(ConsultantStatus)
admin.site.register(LawyerStatus)
