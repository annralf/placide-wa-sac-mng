from collections import UserList
from django.shortcuts import redirect, render
from django.views import View

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate

from . import models as User
from .agent_form import AgentForm

class Login(View):
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
        return render(request,self.template)


class Agent(View):
    def edit(request,id):
        template = 'user/edit.html'
        if request.method == 'POST':
            agent =  User.Users.objects.get(id=id)
            form = AgentForm(request.POST, instance= agent)
            if form.is_valid():
                form.save()
                return redirect("/user/list")
            else:
                print(form.errors)
        else:
            agent = User.Users.objects.get(id=id)
            rol = User.UsersRole.objects.all()
            return render(request,template,{'agent':agent, 'rol':rol})
    
    def new(request):
        newTemplate = 'user/new.html'
        if request.method == 'POST':
            form = AgentForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("/user/list")
            else:
                print(form.errors) 
        form = AgentForm()
        return render(request, newTemplate,{'form':form})

class List(View):
    template = 'user/list.html'
    def get(self, request):
        client_id = 1
        agents = User.Users.objects.filter(client_id=client_id)
        return render(request,self.template,{'agents': agents})