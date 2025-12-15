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

    
# principal class
class classes(models.Model):
    class_name = models.CharField(max_length=20)
    class_teacher = models.CharField(max_length=255)
    class_teacher_id = models.CharField(max_length=10)
    strength = models.IntegerField()
    academic_year = models.CharField(max_length=20)

    status = models.CharField(
        max_length=20,
        choices=[('ongoing', 'Ongoing'), ('completed', 'Completed')],
        default='ongoing'
    )



class ClassTeacherAssignment(models.Model):
    class_obj = models.ForeignKey(classes, on_delete=models.CASCADE)
    teacher = models.ForeignKey(All_Teacher, on_delete=models.CASCADE)

    subject = models.CharField(max_length=255)
    teacher_name = models.CharField(max_length=255)
    is_class_teacher = models.BooleanField(default=False)

    academic_year = models.CharField(max_length=20)

    class Meta:
        unique_together = ('teacher', 'class_obj', 'subject', 'academic_year')


# student setails table\

class Student(models.Model):
    admission_no = models.CharField(max_length=20, primary_key=True)
    roll_no = models.IntegerField()

    name = models.CharField(max_length=255)
    father_name = models.CharField(max_length=255)
    mother_name = models.CharField(max_length=255)
    phone_no = models.CharField(max_length=10)

    class_obj = models.ForeignKey(classes, on_delete=models.CASCADE)

    status = models.CharField(
        max_length=20,
        choices=[('active', 'Active'), ('inactive', 'Inactive')],
        default='active'
    )

    def __str__(self):
        return f"{self.admission_no} - {self.name}"


# announcement table
class Announcement(models.Model):
    title = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100)  # optional: store "principal"
    
    def __str__(self):
        return self.title
    

