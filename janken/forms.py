from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class SignupUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'image']

class LoginForm(AuthenticationForm):
    pass