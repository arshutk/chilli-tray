from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.exceptions import ValidationError


from task1.models import CustomUser


class RegistrationForm(UserCreationForm):
    ''' Model for Custom User model'''
    
    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2')
    


class LoginForm(forms.Form):
    ''' Custom form for handdling the login'''

    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
