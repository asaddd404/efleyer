from django import forms
from .models import *

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

from django.forms.widgets import TextInput,PasswordInput



class UserForm(UserCreationForm):
     class Meta:
          model=User
          fields=['username','email','password1','password2']




class LoginForm(AuthenticationForm):
     username=forms.CharField(widget=TextInput())
     password=forms.CharField(widget=PasswordInput())


