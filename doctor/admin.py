from django.contrib import admin
from doctor.models import Doctor, Notification  # Import the relevant models


class DoctorAdmin(admin.ModelAdmin):
    list_display = ['user', 'full_name', 'specialization', 'qualification', 'years_of_experience']


class NotificationAdmin(admin.ModelAdmin):
    list_display = ['doctor', 'appointment', 'type', 'seen', 'date']  # Corrected typo in 'ModelAdmin'


admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Notification, NotificationAdmin)
