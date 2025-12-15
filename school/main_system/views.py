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

        user = USER.objects.filter(
            Email=email,
            Role=role,
            Password=password,
            status=True
        ).first()

        if user:
            # ✅ SET SESSION
            request.session['user_id'] = user.id
            request.session['user_role'] = user.Role
            request.session['user_email'] = user.Email

            if role == 'principal':
                return redirect('principal')
            elif role == 'teacher':
                return redirect('teacher')
            else:
                return redirect('student')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')

    return render(request, 'login.html')





