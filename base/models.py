from django.db import models
from shortuuid.django_fields import ShortUUIDField


class Service(models.Model):
    image = models.FileField(upload_to="service_images", null=True, blank=True)
    name = models.CharField(max_length=255)  # Fixed max_Length
    description = models.TextField(blank=True, null=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    available_doctors = models.ManyToManyField('doctor.Doctor', blank=True)  # String reference for Doctor

    def __str__(self):
        return f"{self.name} - {self.cost}"


class Appointment(models.Model):
    STATUS = [
        ('Scheduled', 'Scheduled'),
        ('Completed', 'Completed'),
        ('Pending', 'Pending'),
        ('Cancelled', 'Cancelled'),
    ]

    service = models.ForeignKey(
        Service, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='service_app'
    )
    doctor = models.ForeignKey(
        'doctor.Doctor',  # String reference for Doctor
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='doctor_app'
    )
    patient = models.ForeignKey(
        'patient.Patient',  # String reference for Patient
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='patient_app'
    )
    appointment_date = models.DateTimeField(null=True, blank=True)
    issues = models.TextField(blank=True, null=True)
    symptoms = models.TextField(blank=True, null=True)  # Fixed extra space
    appointment_id = ShortUUIDField(length=6, max_length=10, alphabet="1234567890")  # Fixed Length
    status = models.CharField(max_length=120, choices=STATUS)

    def __str__(self):
        patient_name = self.patient.full_name if self.patient else "Unknown Patient"
        doctor_name = self.doctor.full_name if self.doctor else "Unknown Doctor"
        return f"{patient_name} with {doctor_name}"


class MedicalRecord(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)  # Fixed Foreignkey
    diagnosis = models.TextField()
    treatment = models.TextField()  # Fixed extra space

    def __str__(self):
        patient_name = (
            self.appointment.patient.full_name
            if self.appointment and self.appointment.patient
            else "Unknown Patient"
        )
        return f"Medical Record for {patient_name}"


class LabTest(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    test_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    result = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.test_name}"


class Prescription(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    medications = models.TextField(blank=True, null=True)

    def __str__(self):
        patient_name = (
            self.appointment.patient.full_name
            if self.appointment and self.appointment.patient
            else "Unknown Patient"
        )
        return f"Prescription for {patient_name}"


class Billing(models.Model):
    patient = models.ForeignKey(
        'patient.Patient',  # String reference for Patient
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="patient_billing"
    )
    appointment = models.ForeignKey(
        Appointment,
        on_delete=models.CASCADE,
        related_name='billing',
        blank=True,
        null=True
    )
    sub_total = models.DecimalField(max_digits=10, decimal_places=2)
    tax = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=120,
        choices=[('Paid', 'Paid'), ('Unpaid', 'Unpaid')]
    )
    billing_id = ShortUUIDField(length=6, max_length=10, alphabet="1234567890")  # Fixed Length
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        patient_name = self.patient.full_name if self.patient else "Unknown Patient"
        return f"Billing for {patient_name} - Total: {self.total}"
