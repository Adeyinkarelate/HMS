from django.db import models
from shortuuid.django_fields import ShortUUIDField
from doctor import models as Doctor
from patient import models as Patient


class Service(models.Model):
    image = models.FileField(upload_to="service_images", null=True, blank=True)
    name = models.CharField(max_Length=255)
    description = models.TextField(blank=True, null=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    available_doctors = models.ManyToManyField(Doctor, blank=True)

    def _str_(self):
        return f"{self.name} - {self.cost}"


class Appointment(models.Model):

    STATUS = [
        ('Scheduled', 'Scheduled'),
        ('Completed', 'Completed'),
        ('Pending', 'Pending'),
        ('Cancelled', 'Cancelled')
    ]

    service = models.ForeignKey(
        Service, on_delete=models.SET_NULL, null=True, blank=True, related_name='service_app')
    doctor = models.ForeignKey(
        Doctor, on_delete=models.SET_NULL, null=True, blank=True, related_name='doctor_app')
    patient = models. ForeignKey(
        Patient, on_delete=models.SET_NULL, null=True, blank=True, related_name='patient_app')
    appointment_date = models.DateTimeField(null=True, blank=True)
    issues = models.TextField(blank=True, null=True)
    symptoms = models. TextField(blank=True, null=True)
    appointment_id = ShortUUIDField(
        Length=6, max_length=10, alphabet="1234567890")
    status = models.CharField(max_length=120, choices=STATUS)

    def _str_(self):
        return f"{self.patient.full_name} with {self.doctor.full_name}"


class MedicalRecord(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models. CASCADE)
    diagnosis = models.TextField()
    treatment = models. TextField()

    def str_(self):
        return f"Medical Record for {self.appointment.patient.full_name}"


class LabTest(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    test_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    result = models.TextField(blank=True, null=True)

    def _str_(self):
        return f"{self.test_name}"


class Prescription(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    medications = models. TextField(blank=True, null=True)

    def _str_(self):
        return f"Prescription for {self.appointment.patient.full_name}"

