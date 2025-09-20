from django.db import models
from django.contrib.auth.password_validation import validate_password

class StatusType(models.TextChoices):
    LIVE = 'LIVE', 'Live'
    PENDING = 'PENDING', 'Pending'
    REJECTED = 'REJECTED', 'Rejected'

class Hotel(models.Model):
    
    user = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    Description = models.TextField(max_length=50)
    Image = models.ImageField(max_length=255, upload_to='')
    Adress = models.CharField(max_length=255)
    Mobile = models.CharField(max_length=15)
    Email = models.EmailField(max_length=50)
    StatusType = models.CharField(max_length=10, choices=StatusType, default=StatusType.PENDING)