from django.shortcuts import render
from django.views import View

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate

from  .models import Cli as Cli

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
        response = 'Jose Lopez'#Cli.getSetup("Jose Lopez")
        return render(request,self.template, {'agent_name': response})


class Edit(View):
    template = 'user/edit.html'
    def get(self, request):
        return render(request,self.template)

class List(View):
    template = 'user/list.html'
    def get(self, request):
        return render(request,self.template)
