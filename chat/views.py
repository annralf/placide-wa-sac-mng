#from django.shortcuts import render
from django.http import HttpResponse
from .services import getMessages

def index(request):
    getMessages()
    return HttpResponse('Did')
