from django.db import models

class Appointment(models.Model):
    pass

class Doctor(models.Model):
    SEX_CHOICES = (
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
        ('OTHER', 'Other'),
        )

    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    address = models.TextField(max_length=100)
    zip_code = models.CharField(max_length=10)
    age = models.CharField(max_length=10)
    sex = models.CharField(max_length=2, choices=SEX_CHOICES, default='FEMALE')
    specialty = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name

class UserInfo(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=12)
    address = models.TextField(max_length=100)
    zip_code = models.CharField(max_length=10)
    appointment = models.ForeignKey(Appointment)
