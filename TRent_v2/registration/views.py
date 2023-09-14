from django.shortcuts import render, redirect
from .forms import SingUpForm, LoginForm, ForgotPasswordForm
from django.contrib.auth import authenticate, login
import urllib3.request


# Create your views here.

def home(request):
    return render (request, 'home.html')

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid:
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            form.save()
            new_user = authenticate(username=username, password=password)
            if new_user is not None:
                login(request, new_user)
                return redirect("home")
    
    form = LoginForm()
    context = {
        'form':form
    }
    return render(request,'login.html', context)

def forgot_password(request):
    if request.method == "POST":
        form = ForgotPasswordForm(request.POST)
        if form.is_valid:
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            form.save()
            new_user = authenticate(username=username, password=password)
            if new_user is not None:
                login(request, new_user)
                return redirect("home")
    
    form = ForgotPasswordForm()
    context = {
        'form':form
    }
    return render (request, 'forgot-password.html', context)

def signup(request):
    if request.method == "POST":
        form = ForgotPasswordForm(request.POST)
        if form.is_valid:
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            form.save()
            new_user = authenticate(username=username, password=password)
            if new_user is not None:
                login(request, new_user)
                return redirect("home")
    
    form = SingUpForm()
    context = {
        'form':form
    }
    return render(request,'signup.html', context)