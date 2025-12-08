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

# announcement table
class Announcement(models.Model):
    title = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100)  # optional: store "principal"
    
    def __str__(self):
        return self.title
    
# principal class
class classes(models.Model):
    class_name = models.CharField(max_length=20)
    class_teacher = models.CharField(max_length=255)
    class_teacher_id = models.CharField(max_length=10)
    strength = models.IntegerField()
    academic_year = models.CharField(max_length=20)