from django import forms
from django.db.models import fields
from .import models

class checkForm(forms.ModelForm):
    class Meta:
        model = models.check
        fields = ['userName']

#,'newPassword','verify_code'

class resetForm(forms.ModelForm):
    class Meta:
        model = models.reset
        fields = ['newPassword','verify_code']