from django import forms
from django.forms import fields
import importlib
from .models import Labels

class Message(forms.Form):
    chat_id = forms.CharField(widget=forms.HiddenInput())


class LabelsForm(forms.ModelForm):
    class Meta:
        model = Labels
        fields=['name', 'status_label', 'client_id']   
        widgets = {'client_id': forms.HiddenInput()}