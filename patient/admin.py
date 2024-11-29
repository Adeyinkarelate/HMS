from django.contrib import admin
from patient.models import Patient, Notification  # Direct imports for clarity


class PatientAdmin(admin.ModelAdmin):
    list_display = ['user', 'full_name', 'email', 'gender', 'dob']  # Removed 'mobile'


class NotificationAdmin(admin.ModelAdmin):
    list_display = ['patient', 'appointment', 'type', 'seen', 'date']


admin.site.register(Patient, PatientAdmin)
admin.site.register(Notification, NotificationAdmin)
