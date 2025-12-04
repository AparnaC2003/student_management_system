from django.shortcuts import render,redirect

# Create your views here.
def principal_view(request):
    return render(request,"principal/principal.html")

def all_teachers(request):
    return render(request,"principal/teachers/all_teachers.html")

def add_teacher(request):
    return render(request,"principal/teachers/add_teacher.html")

def teacher_view(request):
    return render(request,"teacher_view")

def student_view(request):
    return render(request,"student_view")
