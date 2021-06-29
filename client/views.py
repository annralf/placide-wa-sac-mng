from django.shortcuts import redirect, render
from django.views import View

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate

from  .models import Cli as Cli
from .form import New as NewForm

from message.manager import Manager

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
    def get(self, request):
        chatList = Manager.getChats('all')
        response = 'Manager Agent'
        actives = []
        queue = []
        closed = []        
        for chat in chatList:
            if chat['type_chat'] == 'queue':
                queue.append(chat)
            else:
                if  chat['label'] != 'cerrado':
                    actives.append(chat)
            if chat['label'] == 'cerrado':
                closed.append(chat)
        if 'chat_id' in  request.GET:
            chat_id = request.GET['chat_id']
        else:
            chat_id = actives[0]['chat_id']
        messages = self.chat(chat_id)
        return render(request,self.template, {'agent_name': response, 'actives': actives, 'closed': closed, 'queue':queue, 'messages' : messages})

    def chat(self, chat_id):      
        #Details from Chat
        mng = Manager()
        messages = mng.getChatDetail(chat_id)
        return messages

class Edit(View):
    template = 'user/edit.html'
    def get(self, request):
        return render(request,self.template)

class New(View):
    template = 'client/new.html'
    def get(self, request):
        form = NewForm        
        return render(request,self.template, {'form': form})
    def post(self, request):
        form = NewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/user/list")
        else:
            print(form.errors)
        return render(request,self.template, {'form': form})

class List(View):
    template = 'user/list.html'
    def get(self, request):
        return render(request,self.template)
