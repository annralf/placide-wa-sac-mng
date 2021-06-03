from django.shortcuts import render
from django.views import View

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Services
from .services.messages import getMessages, sendMessage
from .services.dialogs import getDialogs

# Models
#from .models import Queue, Agent#, Chat

class Index(View):
    template = 'index.html'

    def get(self, request):
        return render(request, self.template)

@api_view(['GET','POST','PUT'])
def agents(request, name = None, instance_id = None):
    if request.method == 'GET':
        if name is None:
            pass
 #           r = Agent.objects.using('messages').all()
        else:
            pass
  #          r = Agent.objects.using('messages').filter(agent_name = name)

 #       print(dir(r))
        return Response(r.values())

    if request.method == 'POST':
        if 'name' in request.data:
            pass
#            q = Agent(agent_name = request.data['name'])
#            q.save(using='messages')
        else:
            return Response('MISSING ARGUMENT "NAME"')
        return Response('Done')

    if request.method == 'PUT':
        if 'name' in request.data and 'instance' in request.data:
            name = request.data['name']
            instace = request.data['instance']
#            agent =  Agent.objects.using('messages').filter(agent_name = name)
            print(agent)
#            agent['instances'] = list(agent['instances']).append(instance)
#            agent.save(using = 'messages')

        return Response('assigned')

@api_view(['GET','POST'])
def messages(request,id = None):
    if request.method == 'GET':
        if id is not None:
#            r = Queue.objects.using('messages').filter(message = {'ws_id': id})
            return Response(r.values())

        elif 'cached' in request.query_params:
#            r = Queue.objects.using('messages').all()
            return Response(r.values())
        else:
            r = getMessages(**request.query_params)
            return Response(r.json())

    elif request.method == 'POST':
        for message in request.data['messages']:
            r = sendMessage(**message)
        return Response(r.json())

@api_view(['GET'])
def dialogs(request):
    if request.method == 'GET':
        r = getDialogs()
        return Response(r.json())

@api_view(['POST'])
def hook(request):
    if request.method == 'POST':
        if 'messages' in request.data:
            print(request.data)
            ws_id = request.data['messages'][0]['id']
#            q = Queue()
#            q.message = {
#                'raw_data': request.data,
#                'ws_id': ws_id,
#                'assigned': False,
#            }
#            q.save(using='messages')
            print(request.data)
        return Response('Ok')

@api_view(['GET'])
def queue(request):
    if request.method == 'GET':
        pass
#        r = Queue.objects.using('messages').filter(message = {'assigned':False})
#        return Response(r.values_list())
