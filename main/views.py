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
    return render(request, 'home.html', {'today': today})

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

def search(request):
    form = SearchForm(request.GET or None)
    results= []

    if form.is_valid():
        query = form.cleaned_data.get('query')
        date = form.cleaned_data.get('date')

        results = Destination.objects.all()

        if query:
            results = results.filter(
                Destination(name__icontains=query) | Destination(country__icontains=query)
            )
        if date:
            results = results.filter(
                available_from__lte=date,
                available_to__gte=date
            )
            
    context = {"form": form}
    return render(request,'/results.html', context)

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
