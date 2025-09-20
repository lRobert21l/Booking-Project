from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.password_validation import validate_password

class StatusType(models.TextChoices):
    LIVE = 'LIVE', 'Live'
    PENDING = 'PENDING', 'Pending'
    REJECTED = 'REJECTED', 'Rejected'

class Destination(models.Model):
    
    city = models.CharField(max_length=100, default='')
    country = models.CharField(max_length=50, default='')
    image = models.ImageField(upload_to='posts')
    accommodations = models.PositiveIntegerField(default=1)
    statustype = models.CharField(max_length=10, choices=StatusType, default=StatusType.PENDING)

    def __str__(self):
        return f"{self.name},{self.country}"

