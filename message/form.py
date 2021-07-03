from django import forms
from django.forms import fields
import importlib

class Message(forms.Form):
    chat_id = forms.CharField(widget=forms.HiddenInput())