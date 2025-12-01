
from django.db import models

class UserData(models.Model):
    first_name = models.CharField(max_length=100)        # ⭐ Important
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)               # ⭐ Important (email must be unique)
    phone_number = models.CharField(max_length=15)
    age = models.IntegerField()
    
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)   # ⭐ Important (dropdown)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
