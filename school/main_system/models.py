from django.db import models

# Create your models here.
class USER(models.Model):
    Username = models.CharField(max_length=255)
    Email = models.CharField(max_length=225,unique=True)
    Role = models.CharField(max_length=50)
    Password = models.CharField(max_length=200)
    status = models.BooleanField(default=True)  # account is active by default


