from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.db import models

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class check(models.Model):
    userName = models.CharField(max_length=100)
    # oldPassword = models.CharField(max_length=100)
    # newPassword = models.CharField(max_length=100)
    # verify_code = models.CharField(max_length=6)
class reset(models.Model):
    newPassword = models.CharField(max_length=100)
    verify_code = models.CharField(max_length=6)

    


