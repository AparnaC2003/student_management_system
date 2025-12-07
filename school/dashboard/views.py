from django.shortcuts import render,redirect
from dashboard.models import All_Teacher
from django.contrib import messages 

# Create your views here.
def principal_view(request):
    return render(request,"principal/principal.html")

def all_teachers(request):
    teachers = All_Teacher.objects.all()   # fetch ALL teachers
    return render(request,"principal/teachers/all_teachers.html" , {"teachers": teachers})

def add_teacher(request):
    if request.method == 'POST':
        Teacher_id = request.POST.get('teacher_id')
        Name = request.POST.get('name')
        Email = request.POST.get('email')
        Phone = request.POST.get('phone')
        Class = request.POST.get('class_assigned')
        Subject = request.POST.get('subject')
        Joining_date = request.POST.get('joining_date')
        status = request.POST.get('status')

        UserExist = All_Teacher.objects.filter(teacher_id = Teacher_id).first()

        if UserExist:
            print("Teacher already exist....")
            messages.error(request,'Teacher already exist....!')
        else:
            All_Teacher.objects.create(teacher_id=Teacher_id,name=Name,Email=Email,phone_no=Phone,class_assigned=Class,subject=Subject,joining_date=Joining_date,status=status)
            print("teacher added successfully.....!")
            return redirect('all_teachers')

    return render(request,"principal/teachers/add_teacher.html")

def teacher_view(request):
    return render(request,"teacher_view")

def student_view(request):
    return render(request,"student_view")
