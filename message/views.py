from django.shortcuts import render
from django.views import View

from django.contrib.auth.forms import AuthenticationForm

# Models
# from .models import Queue, Agent#, Chat

class Message(View):
    activesTmp = 'message/actives.html'
    queueTmp = 'message/queue.html'
    closeTmp = 'message/close.html'
    labeledTmp = 'message/labeled.html'

    def get(self, request, type='active'):
        if type == 'active':
            return render(request, self.activesTmp) 

        if type == 'queue':
            return render(request, self.queueTmp) 

        if type == 'closed':
            return render(request, self.closeTmp) 

        if type == 'labeled':
            return render(request, self.labeledTmp) 
