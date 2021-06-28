from django import forms
from django.forms import fields
import importlib
from .models import Client

class New(forms.ModelForm):
    class Meta:
        model = Client 
        fields= '__all__'