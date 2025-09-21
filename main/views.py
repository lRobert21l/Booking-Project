from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, UserLoginForm, SearchForm
from .models import Destination
from datetime import date

# Create your views here.


def home(request):
    today = date.today()
    return render(request, 'main/home.html', {'today': today})

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

def destinations(request):
    destinations = Destination.objects.all()

    return render(request,'main/blog.html', {"destinations": destinations})

def results(request):
    if request.method == "POST":
        location = request.POST.get('location')
        date = request.POST.get('date')

        destinations = Destination.objects.all()

        # Filter by location
        if location:
            destinations = destinations.filter(city__icontains=location) | destinations.filter(country__icontains=location)

        # Filter by date if needed (example: only show future destinations)
        if date:
            # You can extend with date filtering logic
            pass

        return render(request, 'main/results.html',
            {
                'destinations': destinations,
                'location': location,
                'date': date,
            }
        )

    return render(request, 'main/results.html', {'destinations': []})

def user(request):
    context = {}
    return render(request,'main/details.html', context)

def about(request):
    context = {}
    return render(request,'main/about.html', context)

def contact(request):
    context = {}
    return render(request,'main/contact.html', context)
