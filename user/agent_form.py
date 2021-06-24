from django import forms
from django.forms import fields
import importlib
from .models import Users

class AgentForm(forms.ModelForm):
    class Meta:
        model = Users 
        fields="__all__"