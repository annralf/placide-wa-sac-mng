from django.shortcuts import render
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
    
    def edit(request):
        template = 'user/edit.html'
        return render(request,template)

    def new(request):
        newTemplate = 'user/new.html'
        form = AgentForm()
        return render(request, newTemplate,{'form':form, 'lol':'casa'})

class List(View):
    template = 'user/list.html'
    def get(self, request):
        return render(request,self.template)