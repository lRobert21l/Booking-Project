from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.password_validation import validate_password

class StatusType(models.TextChoices):
    LIVE = 'LIVE', 'Live'
    PENDING = 'PENDING', 'Pending'
    REJECTED = 'REJECTED', 'Rejected'

class Destination(models.Model):
    
    name = models.CharField(max_length=100, default='')
    country = models.CharField(max_length=50, default='')
    image = models.ImageField(upload_to='posts')
    accommodations = models.PositiveIntegerField(default=1)
    statustype = models.CharField(max_length=10, choices=StatusType, default=StatusType.PENDING)

    def __str__(self):
        return f"{self.name},{self.country}"
    
        # <div class="destinations-container" id="destinations">
        #     {% for blog in blogs %}
        #         <div class="destination-card">
        #             <img src="{{ blog.image.url }}" alt="{{ blog.name }}">
        #             <h3>{{ blog.name }}</h3>
        #             <p>{{ blog.country }}</p>
        #             <p><strong>{{ blog.accommodations }}</strong></p>
        #         </div>
        #     {% endfor %}
        # </div>