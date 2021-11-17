from django import forms
from django.db.models import fields
from .import models

class RegisterDog(forms.ModelForm):
    class Meta:
        model = models.Dog
        fields = ['name','sex','birthday','description']
