from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse, HttpResponseRedirect

from .form import *
from .manager import Manager
from .models import Labels

# Models
# from .models import Queue, Agent#, Chat

class Message(View):
#     activesTmp = 'message/actives.html'
#     queueTmp = 'message/queue.html'
#     closeTmp = 'message/close.html'
#     labeledTmp = 'message/labeled.html'

#     def get(self, request, type='active'):
#         if type == 'active':
#             return render(request, self.activesTmp) 

#         if type == 'queue':
#             return render(request, self.queueTmp) 

#         if type == 'closed':
#             return render(request, self.closeTmp) 

#         if type == 'labeled':
#             return render(request, self.labeledTmp) 
#         return redirect("/client/")


    def send(request):
        if request.method == 'POST':
            message_handler = Manager()
            chatId = request.POST['chat_id']
            message_handler.sendMessage(request.POST['message_body'], chatId)
        return redirect("/client/?chat_id="+chatId)


class Label(View):
    template = 'label/list.html'
    def get(self, request):
        client_id = 1
        labels =Labels.objects.filter(client_id=client_id)
        return render(request,self.template,{'labels': labels})
    
    def new(request):
        template = 'label/new.html'
        client_id = 1
        if request.method == 'POST':
            form = LabelsForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("/message/label")
            else:
                print(form.errors)
        form = LabelsForm()
        form.fields['client_id'].initial = client_id
        return render(request, template,{'form': form})
    
    def edit(request,id):
        template = 'label/edit.html'
        if request.method == 'POST':
            label =  Labels.objects.get(id=id)
            form = LabelsForm(request.POST, instance= label)
            if form.is_valid():
                form.save()
                return redirect("/message/label")
            else:
                print(form.errors)
        else:
            label = Labels.objects.get(id=id)
            return render(request,template,{'label':label})
    
    def delete(request,id):
        label = Labels.objects.get(id=id)
        label.delete()
        return redirect("/message/label")