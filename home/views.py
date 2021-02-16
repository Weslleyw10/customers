from django.shortcuts import redirect, render
from django.contrib import auth

def index(request):
    return render(request, 'home.html')

def logout(request):
    auth.logout(request)
    return redirect('index')