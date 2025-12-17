from django.shortcuts import render,redirect, get_object_or_404 
from dashboard.models import All_Teacher,Announcement,classes,ClassTeacherAssignment,Student
from main_system.models import USER
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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

def assigned_details(request):
    assignments = ClassTeacherAssignment.objects.select_related("class_obj").all().order_by("-id")

    return render(request, "principal/assigned_details.html", {
        "assignments": assignments
    })


def add_details(request):

    if request.method == "POST":

        class_id = request.POST.get("class_obj")
        subject = request.POST.get("subject")
        teacher_id = request.POST.get("teacher")
        is_class_teacher = request.POST.get("is_class_teacher") == "True"
        academic_year = request.POST.get("academic_year")
        status = request.POST.get("status")

        # 🔥 Fetch teacher name automatically (IMPORTANT FIX)
        try:
            teacher_obj = All_Teacher.objects.get(id=teacher_id)
            teacher_name = teacher_obj.name
        except All_Teacher.DoesNotExist:
            messages.error(request, "Invalid teacher selected.")
            return redirect("add_details")

        # ❌ Prevent duplicate class teacher in same academic year
        if is_class_teacher:
            exists = ClassTeacherAssignment.objects.filter(
                is_class_teacher=True,
                academic_year=academic_year,
                teacher_id=teacher_id
            ).first()

            if exists:
                messages.error(request, "This teacher is already a class teacher for this academic year!")
                return redirect("add_details")

        # ✔ Save the assignment
        ClassTeacherAssignment.objects.create(
            class_obj_id=class_id,
            subject=subject,
            teacher_id=teacher_id,
            teacher_name=teacher_name,  # auto-fetched
            is_class_teacher=is_class_teacher,
            academic_year=academic_year,
            status=status
        )

        messages.success(request, "Teacher assigned successfully!")
        return redirect("assigned_details")

    # GET request → send classes + teacher list
    classes_list = classes.objects.all()
    teachers_list = All_Teacher.objects.all()

    return render(request, "principal/add_details.html", {
        "classes": classes_list,
        "teachers": teachers_list
    })


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


# teacher dashboard views

def teacher_view(request):
    return render(request,"teacher/teacher.html")


# teacher_my_class view


def teacher_my_class(request):
    if request.session.get('user_role') != 'teacher':
        return redirect('login')

    teacher = All_Teacher.objects.get(
        Email=request.session.get('user_email')
    )

    assignments = ClassTeacherAssignment.objects.filter(
        teacher=teacher
    ).select_related('class_obj')

    return render(request, 'teacher/my_class.html', {
        'assignments': assignments
    })

# view more button in my class next page

def teacher_class_dashboard(request, assignment_id):
    assignment = get_object_or_404(
        ClassTeacherAssignment,
        id=assignment_id
    )

    return render(
        request,
        'teacher/myclass_dashboard.html',
        {
            'assignment': assignment
        }
    )

# student details view
def teacher_class_students(request, assignment_id):
    assignment = get_object_or_404(
        ClassTeacherAssignment,
        id=assignment_id
    )

    # fetch students of that class only
    students = Student.objects.filter(
        class_obj=assignment.class_obj
    )

    return render(
        request,
        'teacher/myclass_students.html',
        {
            'assignment': assignment,
            'students': students
        }
    )

# adding the student details in teacher myclass

# def add_student_details(request):



def student_view(request):
    return render(request,"student_view")
