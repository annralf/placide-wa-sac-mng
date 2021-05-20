#from django.shortcuts import render
from django.http import HttpResponse
from .services.messages import sendMessage

def index(request):
    sendMessage( body = 'Mensaje de prueba', phone = '+573503376482' )
    return HttpResponse('Did')
