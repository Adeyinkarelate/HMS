from django.db import models
from django.utils import timezone
from userauth import models as userauths_models

NOTIFICATION_TYPE = (
    ("Appointment Scheduled", "Appointment Scheduled"),
    ("Appointment Cancelled", "Appointment Cancelled"),
)

class Patient(models.Model):
    user = models.OneToOneField(userauths_models.User, on_delete=models.CASCADE)
    image = models.FileField(upload_to="images", null=True, blank=True)
    full_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    bio = models.CharField(max_length=100, null=True, blank=True)  # Corrected max_length
    gender = models.CharField(max_length=100, null=True, blank=True)
    blood_group = models.CharField(max_length=10, null=True, blank=True)  # Corrected field name and max_length
    dob = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return f"{self.full_name}"

class Notification(models.Model):
    patient = models.ForeignKey(
        'Patient', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
    )
    appointment = models.ForeignKey(
        'base.Appointment',  # Use a string reference to avoid circular imports
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="patient_appointment_notification"
    )
    type = models.CharField(max_length=100, choices=NOTIFICATION_TYPE)
    seen = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Notifications"  # Corrected Meta class definition
    
    def __str__(self):
        patient_name = self.patient.full_name if self.patient else "Unknown"
        return f"{patient_name} notification"
