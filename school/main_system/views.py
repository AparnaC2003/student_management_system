from django.shortcuts import render,redirect
from main_system.models import USER
from django.contrib import messages

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        role = request.POST.get('role')
        password = request.POST.get('password')
        name = request.POST.get('username')
        userExist = USER.objects.filter(Email = email).first()
        if userExist:
            print("user already exist")
            messages.error(request,"User already exists...!")
        else:
            USER.objects.create(Username = name,Email = email,Role = role,Password = password)
            print("user added succcessfully....!")
            return redirect('login')
    return render(request,'signup.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        role = request.POST.get('role')
        password = request.POST.get('password')
        UserEXist = USER.objects.filter(Email = email,Role = role,Password = password).first()
        if UserEXist:
            print("login successfull...! ")
            if(role == 'principal'):
                return redirect('principal')
            elif(role == 'teacher'):
                return redirect('teacher')
            else:
                return redirect('student')
        else:
            print('user dosent exists')
            messages.error(request,'User does not exists...!')
            return redirect('login')
    return render(request,'login.html')