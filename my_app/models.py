from django.db import models

# Create your models here.

class Appointment(models.Model):
    DEPARTMENT_CHOICES = [
        ('Cardiology', 'Cardiology'),
        ('Dermatology', 'Dermatology'),
        ('Orthopedics', 'Orthopedics'),
        ('General Medicine', 'General Medicine'),
        ('ENT', 'ENT'),
    ]
    STATUS_CHOICES = [
        ('Booked', 'Booked'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]
    patient_name = models.CharField(max_length=40)
    patient_age = models.IntegerField()
    patient_email = models.EmailField(max_length=40)
    doctor_name = models.CharField(max_length=40)
    department= models.CharField(max_length=30, choices=DEPARTMENT_CHOICES)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    status = models.CharField(max_length=30, choices=STATUS_CHOICES)
    symptoms = models.TextField(blank=True, null=True)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.patient_name


    

