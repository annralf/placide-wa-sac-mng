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
    def send(request):
        if request.method == 'POST':
            message_handler = Manager()
            chatId = request.POST['chat_id']
            message_handler.sendMessage(request.POST['message_body'], chatId)
        return HttpResponseRedirect("/client?chat_id="+chatId)

    def setAgent(request, chat_id, status, agent_id):
        mng = Manager()
        response = mng.set(chat_id, status, agent_id)
        return redirect('/client/')

    def setStatus(request, chat_id, status):
        mng = Manager()
        response = mng.set(chat_id, status, None)
        return redirect('/client/chat_id='+chat_id)


class Label(View):
    template = 'label/list.html'
    def get(self, request):
        client_id = request.session['client_id'] if request.session['client_id'] else 1
        labels =Labels.objects.filter(client_id=client_id)
        return render(request,self.template,{'labels': labels})
    
    def new(request):
        template = 'label/new.html'
        client_id = request.session['client_id'] if request.session['client_id'] else 1
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

    def add(request, chat_id, label):
        mng = Manager()
        mng.setLabel(chat_id, label)
        return redirect('/client/')
