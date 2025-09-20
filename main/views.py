from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, UserLoginForm

# Create your views here.


def home(request):
    return render(request,'main/home.html')

def log_in(request):
    if request.user.is_authenticated:
        return redirect('/home')
    else:
        form = UserLoginForm()
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/home')
            elif username == "" or password == "":
                messages.info(request, "Please enter username and password !")
            else:
                messages.error(request, "Username or Password is incorrect !")
        else:
            form = UserLoginForm()
            
        context = {"form": form}    
        return render(request,'registration/login.html', context)

def log_out(request):
    logout(request)
    return redirect('/home')


def sign_up(request):
    global form
    if request.user.is_authenticated:
        return redirect('/home')
    else:
        form = UserRegisterForm()
        if request.method == "POST":
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Account was created successfully.")
        else:
            form = UserRegisterForm()

        context = {"form": form}
        return render(request,'registration/sign-up.html', context)

def blog(request):
    context = {}
    return render(request,'main/blog.html', context)

def details(request):
    context = {}
    return render(request,'main/details.html', context)

def user(request):
    context = {}
    return render(request,'main/blog.html', context)

def about(request):
    context = {}
    return render(request,'main/about.html', context)

def contact(request):
    context = {}
    return render(request,'main/contact.html', context)
