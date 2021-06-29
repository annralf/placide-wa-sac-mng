from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse, HttpResponseRedirect

from .manager import Manager


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

    def send(request):
        if request.method == 'POST':
            message_handler = Manager()
            contex = {
                'messages':[
                    {
                        'body': request.POST['message_body'],
                        'phone': request.POST['phone_number'],
                    }
                ]
            }
            message_handler.sendMessage(contex)
        return HttpResponseRedirect("/client/")