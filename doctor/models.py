from django.db import models
from django.utils import timezone
from userauth import models as userauths_models

NOTIFICATION_TYPE = (
    ("New Appointment", "New Appointment"),
    ("Appointment Cancelled", "Appointment Cancelled"),
)

class Doctor(models.Model):
    user = models.OneToOneField(userauths_models.User, on_delete=models.CASCADE)
    image = models.FileField(upload_to="images", null=True, blank=True)
    full_name = models.CharField(max_length=100, null=True, blank=True)
    mobile = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    bio = models.CharField(max_length=100, null=True, blank=True)  # Fixed max_length
    specialization = models.CharField(max_length=100, null=True, blank=True)
    qualification = models.CharField(max_length=100, null=True, blank=True)  # Fixed max_length
    years_of_experience = models.CharField(max_length=100, null=True, blank=True)
    next_available_appointment_date = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"Dr. {self.full_name}" if self.full_name else "Unknown Doctor"

class Notification(models.Model):
    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    appointment = models.ForeignKey(
        'base.Appointment',  # String reference to avoid circular import
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="doctor_appointment_notification"
    )
    type = models.CharField(max_length=100, choices=NOTIFICATION_TYPE)
    seen = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Notifications"  # Fixed Meta class

    def __str__(self):
        doctor_name = self.doctor.full_name if self.doctor else "Unknown Doctor"
        return f"Dr. {doctor_name} notification"
