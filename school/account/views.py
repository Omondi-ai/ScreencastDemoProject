from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

def home(request):
    return render(request, 'account/index.html')

def register(request):
    form = CreateUserForm()
    context = {'RegisterForm': form}  # Initialize context here

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save() 
            return redirect('my-login')
            return HttpResponse('User Registered')
           

    return render(request, 'account/register.html', context)


def my_login(request):
    form = AuthenticationForm()
    context = {'loginForm': form}

    if request.method == 'POST':

        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
#username/email
            user = authenticate(request, username=username, password=password)

            if  user.is_teacher  == True and user.is_student == False:

                login(request, user)

                return redirect('teacher-dashboard')



            elif  user.is_student  == True and user.is_teacher == False:

                login(request, user)

                return redirect('student-dashboard')

            elif user.is_student == False and user.is_teacher == False:

                login(request, user)
    
                return redirect('my-login')
          
            
           
    context = {'LoginForm': form}



    return render(request, 'account/my-login.html', context)


def user_logout(request):
    logout(request)
    return redirect("my-login")
