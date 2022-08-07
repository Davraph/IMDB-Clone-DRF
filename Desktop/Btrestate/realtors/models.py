import email
from django.db import models
from datetime import datetime

# Create your models here.
class Realtor(models.Model):
    name= models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%M/%d/')
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateField(default=False)
    
    def __str__(self):
        return self.name