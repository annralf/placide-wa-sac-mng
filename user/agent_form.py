from django import forms
from django.forms import fields, models
import importlib
from .models import Users, UsersRole

class AgentForm(forms.ModelForm):
    class Meta:
        model = Users 
        fields=['name', 'lastname', 'username', 'password','role','status_user', 'client_id']       

class RolForm(forms.ModelForm):
    class Meta:
        model = UsersRole
        fields=['name', 'status_rol', 'client_id']   
        widgets = {'client_id': forms.HiddenInput()}