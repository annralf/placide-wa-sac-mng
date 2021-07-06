# from app import client
from django.shortcuts import redirect, render
from django.views import View

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.views.generic.base import TemplateView

from  .models import Client as Cli
from .form import New as NewForm
from message.form import Message as MessageForm
from message.models import Labels
from user.models import Users 

from message.manager import Manager
from .manager import Manager as ClientMng

class Client(View):
    template = 'user/login.html'

    def get(self, request):
        form = AuthenticationForm()
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # return HttpResponseRedirect('/')
        else:
            return render(request, self.template, {'form': form})


class Admin(View):
    template = 'user/admin.html'
    def get(self, request, chat_id = None):
        client_id = request.session['client_id'] if 'client_id' in request.session else 1
        mng = Manager()
        chatList = mng.getChats('all',client_id)
        response = 'Manager Agent'
        actives = []
        queue = []
        closed = []        
        messages_labeled = []
        messages = []        
        for chat in chatList:
            if chat['chat_id'] == chat_id:
                actives.append(chat)
            if chat['type_chat'] == 'queue':
                queue.append(chat)
            elif chat['type_chat'] == 'active' and chat['label'] == 'N/A':
                actives.append(chat)
            elif chat['type_chat'] == 'cerrado':
                closed.append(chat)
            elif chat['label'] != 'N/A':
                messages_labeled.append(chat)
        if 'chat_id' in  request.GET:
            chat_id = request.GET['chat_id']
            mng = Manager()
            status = "active"
            mng.set(chat_id, status, None,client_id)
        else:
            if actives:
                chat_id = actives[0]['chat_id']
        messages = self.chat(chat_id, client_id)
       
        form = MessageForm         
        agents = Users.objects.filter(client_id= client_id).filter(status_user = 1)
        #Get setting labels
        labels = Labels.objects.filter(client_id=client_id)
        
        return render(request,self.template, {'agent_name': response, 'actives': actives, 'closed': closed, 'queue':queue, 'messages' : messages, 'form': form, 'agents': agents, 'labels': labels, 'messages_labeled' : messages_labeled})

    def chat(self, chat_id, client_id):      
        #Details from Chat
        mng = Manager()
        messages = mng.getChatDetail(chat_id, client_id)
        return messages

    def edit(request, id):
        template = 'client/edit.html'
        client_id = request.session['client_id'] if 'client_id' in request.session else 1
        if request.method == 'POST':
            client =  Cli.objects.get(id=id)
            form = NewForm(request.POST, instance= client)
            if form.is_valid():
                form.save()
                return redirect('admin')
            else:
                print(form.errors)
        else:
            client = Cli.objects.get(id=id)
            manager = ClientMng()
            image = manager.getQr(client_id)
            return render(request,template,{'client':client, 'image': image})
    
    def delete(request, id):
        try:
            client = Cli.objects.get(id=id)
            client.delete()
        except:
            print("An exception occurred")        
        return redirect('admin')

class Show(View):
    template = 'client/show.html'
    def get(self, request, id):
        client = Cli.objects.get(id=id)
        manager = ClientMng()
        image = manager.getQr(id)
        return render(request, self.template, {'client': client, 'image': image})


class New(View):
    template = 'client/new.html'
    def get(self, request):
        form = NewForm        
        return render(request,self.template, {'form': form})
    def post(self, request):
        form = NewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin')
        else:
            print(form.errors)
        return render(request,self.template, {'form': form})

class List(View):
    template = 'client/list.html'
    def get(self, request):
        clients = Cli.objects.all()
        return render(request,self.template, {'clients': clients})
