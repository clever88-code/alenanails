from django import forms
from django.core.exceptions import ValidationError
from requests import request

from main.models import *



class RecordForm(forms.ModelForm):
    success_url = '/record'
    class Meta:
        model = record
        fields = ['name', 'email', 'number']