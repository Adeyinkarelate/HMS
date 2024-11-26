from django.db import models
from django.utils import timezone
from userauth import models as userauths_models
from base.models import Appointment

NOTIFICATION_TYPE = (
    ("Appointment Scheduled","Appointment Scheduled"),
    ("Appointment Cancelled","Appointment Cancelled"),
)

class Patient(models.Model):
    user =models.OneToOneField(userauths_models.User, on_delete=models.CASCADE)
    image = models.FileField(upload_to="images", null=True, blank=True)
    full_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    bio = models.CharField(max_length=1e0, null=True, blank=True)
    gender = models.CharField(max_length=100, null=True, blank=True)
    blod_group = models.CharField(max_length=1e0, null=True, blank=True)
    dob = models.CharField(max_length=100, null=True, blank=True)
    

    def _str_(self):
       
        return f"{self.full_name}"

class Notification(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models. SET_NULL, null=True, blank=True)
    appointment = models.ForeignKey(Appointment,on_delete=models.CASCADE,null=True ,blank=True,related_name="doctor_appointment_notification")
    type = models.CharField(max_length=100 ,choices=NOTIFICATION_TYPE)
    seen = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta():
        verbose_name_plural ="Notification"
        
    def __str__(self):
        return f" {self.patient.full_name} notification"