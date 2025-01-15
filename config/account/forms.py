from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):  # Переименуем форму
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(forms.Form):  # Переименуем форму
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)