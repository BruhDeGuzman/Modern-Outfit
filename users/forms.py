from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Here is the form of Register which we can modify our fields

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']