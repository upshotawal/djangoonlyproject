from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import OrderPlaced, UserInfo


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserInfo(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['fname', 'lname', 'email', 'uname', 'adderess',
                  'payment', 'cname', 'cnum', 'CVV']
