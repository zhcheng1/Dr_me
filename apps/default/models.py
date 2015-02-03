from django.db import models

class Doctor(models.Model):
    SEX_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
        )

    full_name = models.TextField(max_length=100)
    address = models.TextField(max_length=150)
    zip_code = models.CharField(max_length=30)
    age = models.CharField(max=10)
    sex = models.CharField(max_length=2, choices=SEX_CHOICES, default=FEMALE)
    specialty = models.TextField(max_length=100)

    def __str__(self):
        return self.full_name
