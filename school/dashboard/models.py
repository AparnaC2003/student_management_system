from django.db import models

# Create your models here.
class All_Teacher(models.Model):
    teacher_id = models.CharField(max_length=10,unique=True)
    name = models.CharField(max_length=255)
    Email = models.CharField(max_length=225,unique=True)
    phone_no = models.CharField(max_length=10,unique=True)
    class_assigned = models.CharField(max_length=20)
    subject = models.CharField(max_length=255)
    joining_date = models.CharField(max_length=20)
    status = models.CharField(max_length=30)

