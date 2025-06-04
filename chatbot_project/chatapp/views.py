from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

def home(request):
    """
    Render the home page of the chatbot application.
    """
    return render(request, 'chatapp/home.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
        else:
            User.objects.create(username=username)
            messages.success(request, 'Registration successful')
            return redirect('home')
    return render(request, 'chatapp/register.html')