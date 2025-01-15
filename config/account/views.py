from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from .forms import RegisterForm, LoginForm  # Переименуйте формы для избежания конфликтов


def index(request):
    return render(request, 'index.html')

    
def register_view(request):  # Переименуйте функцию, чтобы избежать конфликта
    if request.method == 'POST':
        form = RegisterForm(request.POST)  # Используйте правильную форму
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})  # Исправьте ключ на 'form'

def login_view(request):  # Переименуйте функцию, чтобы избежать конфликта
    if request.method == 'POST':
        form = LoginForm(request.POST)  # Используйте правильную форму
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)  # Используйте переименованную функцию
                return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):  # Переименуйте функцию, чтобы избежать конфликта
    auth_logout(request)  # Используйте переименованную функцию
    return redirect('login')