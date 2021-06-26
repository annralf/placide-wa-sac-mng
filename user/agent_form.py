from django import forms
from django.forms import fields
import importlib
from .models import Users, UsersRole

class AgentForm(forms.ModelForm):
    class Meta:
        model = Users 
        # fields = "__all__"  
        fields=['name', 'lastname', 'username', 'password','role','status', 'client_id']       