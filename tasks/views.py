from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

# Create your views here.

def home(request):
    return render(request, 'home.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('home')

    return render(request, 'login.html')

def tasks(request):
    return render(request, 'tasks.html')