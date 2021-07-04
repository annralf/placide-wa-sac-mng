from collections import UserList
from django.contrib.auth import forms
from django.shortcuts import redirect, render
from django.views import View

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate

from . import models as User
from .agent_form import *

class Login(View):
    template = 'user/login.html'
    def get(self, request):
        form = AuthForm()
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = AuthForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        agent =  User.Users.objects.get(username=username,password=password)
        form = AuthForm(request.POST, instance= agent)
        if form.is_valid():
            form.save()
            request.session['user_id'] = form.cleaned_data.get('id')
            request.session['full_name'] = form.cleaned_data.get('name')
            request.session['rol'] = form.cleaned_data.get('role')
            request.session['client_id'] = form.cleaned_data.get('client_id')
            return redirect("home")
        else:
            form = AuthForm()
            print(form.errors)
            return render(request, self.template, {'form': form})
            
    def logout(request):
        del request.session['user_id']
        del request.session['full_name']
        del request.session['rol']
        del request.session['client_id']
        return redirect("login")
        

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
    
    def delete(request,id):
        user = User.Users.objects.get(id=id)
        user.delete()
        return redirect("/user/list")

class List(View):
    template = 'user/list.html'
    def get(self, request):
        client_id = 1
        agents = User.Users.objects.filter(client_id=client_id)
        return render(request,self.template,{'agents': agents})

class Rol(View):
    template = 'rol/list.html'
    def get(self, request):
        client_id = 1
        rol = User.UsersRole.objects.filter(client_id=client_id)
        return render(request,self.template,{'roles': rol})
    
    def new(request):
        template = 'rol/new.html'
        client_id = 1
        if request.method == 'POST':
            form = RolForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("/user/rol")
            else:
                print(form.errors)
        form = RolForm()
        form.fields['client_id'].initial = client_id
        return render(request, template,{'form': form,'client_id': client_id})
    
    def edit(request,id):
        template = 'rol/edit.html'
        if request.method == 'POST':
            rol =  User.UsersRole.objects.get(id=id)
            form = RolForm(request.POST, instance= rol)
            if form.is_valid():
                form.save()
                return redirect("/user/rol")
            else:
                print(form.errors)
        else:
            rol = User.UsersRole.objects.get(id=id)
            return render(request,template,{'rol':rol})
    
    def delete(request,id):
        role = User.UsersRole.objects.get(id=id)
        role.delete()
        return redirect("/user/rol")