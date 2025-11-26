from django.shortcuts import render,redirect

# Create your views here.
def principal_view(request):
    return render(request,"principal.html")

def teacher_view(request):
    return render(request,"teacher_view")

def student_view(request):
    return render(request,"student_view")
