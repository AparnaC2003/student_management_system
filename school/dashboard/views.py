from django.shortcuts import render,redirect
from dashboard.models import All_Teacher,Announcement,classes
from main_system.models import USER
from django.contrib import messages 
# from django.contrib.auth.decorators import login_required

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

# all classes view
def all_classes(request):
    classes_list = classes.objects.all()  # fetch all classes
    return render(request, "principal/classes/all_classes.html", {"classes": classes_list})

def add_class(request):
    if request.method == 'POST':
        class_name = request.POST.get('class_name')
        class_teacher = request.POST.get('class_teacher')
        class_teacher_id = request.POST.get('class_teacher_id')
        strength = request.POST.get('strength')
        academic_year = request.POST.get('year')

        UserExist = classes.objects.filter(class_teacher_id = class_teacher_id,academic_year =  academic_year).first()
        if UserExist:
            print("class teacher of another class for this academic year already exist....")
            messages.error(request,'Already a class teacher of another class for this academic year....!')
            return redirect('add_class')
        else:
        # Save to database
            classes.objects.create(
                class_name=class_name,
                class_teacher=class_teacher,
                class_teacher_id=class_teacher_id,
                strength=strength,
                academic_year=academic_year
            )

        return redirect('all_classes')  # URL name
    return render(request,"principal/classes/add_class.html")

# announcement view

def principal_announcements(request):

    # If form is submitted
    if request.method == "POST":
        heading = request.POST.get("heading")
        details = request.POST.get("details")

        # Save to database
        Announcement.objects.create(
            title=heading,
            message=details,
            created_by="Principal"
        )

        return redirect("principal_announcements")   # URL name

    # Fetch all announcements (latest first)
    announcements = Announcement.objects.order_by("-created_at")

    return render(request, "principal/principal_announcements.html", {
        "announcements": announcements
    })




def teacher_view(request):
    return render(request,"teacher_view")

def student_view(request):
    return render(request,"student_view")
