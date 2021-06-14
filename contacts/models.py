from django.db import models
from datetime import datetime

# Create your models here.

class Contact(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()
    Phone_no = models.CharField(max_length=20, blank=True)
    def __str__(self):
        return self.first_name