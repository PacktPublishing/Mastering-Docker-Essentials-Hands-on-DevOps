from django.shortcuts import render, redirect
from .models import Course


def login(request):
    return render(request, 'account/login.html')

def login(request):
    return render(request, 'account/login.html')

# def signup(request):
#     return redirect('account_signup')

def home(request):
    context = Course.objects.all()
    return render(request, 'home/home.html', {'context':context})

def youtube(request):
    return render(request, 'home/youtube.html')

def books(request):
    return render(request, 'home/books.html')

