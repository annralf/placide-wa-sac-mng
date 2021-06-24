from django.shortcuts import render
from django.views import View

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Services
from .services.messages import getMessages, sendMessage
from .services.dialogs import getDialogs

# Models
from .models import Message, Chat, Queue

def std_response(msg='successful',pld={}):
    return Response({"status": 'Ok', "payload": pld, "message": msg})

class Index(View):
    template = 'index.html'

    def get(self, request):
        agent_name = "testing agent"
        return render(request, self.template, {'agent_name': agent_name})

@api_view(['GET','POST','PUT'])
def agents(request, name = None, instance_id = None):
    if request.method == 'GET':
        if name is None:
            pass
            r = Agent.objects.all()
        else:
            pass
            r = Agent.objects.filter(agent_name = name)

        print(dir(r))
        return std_response(pld=r.values())

    if request.method == 'POST':
        if 'name' in request.data:
            pass
            q = Agent(agent_name = request.data['name'])
            q.save()
        else:
            return std_response('Mising argument "NAME"')
        return std_response('Done')

    if request.method == 'PUT':
        if 'name' in request.data and 'instance' in request.data:
            name = request.data['name']
            instace = request.data['instance']
            agent =  Agent.objects.filter(agent_name = name)
            print(agent)
            agent['instances'] = list(agent['instances']).append(instance)
            agent.save()

        return std_response('assigned')

@api_view(['GET','POST'])
def messages(request,id = None):
    if request.method == 'GET':
        if id is not None:
            r = Queue.objects.filter(message = {'ws_id': id})
            return std_response(pld=r.values())

        elif 'cached' in request.query_params:
            r = Queue.objects.all()
            return std_response(pld=r.values())
        else:
            r = getMessages(**request.query_params)
            return std_response(pld=r.json())

    elif request.method == 'POST':
        if not 'messages' in request.data:
            r = sendMessage(**request.data)
            return std_response(pld=r.json())
        else:
            r = []
            for message in request.data['messages']:
                aux = sendMessage(**message)
                r.append(aux.json())
            return std_response(msg='All messages sent',pld=r)

@api_view(['GET'])
def dialogs(request):
    if request.method == 'GET':
        r = getDialogs()
        return std_response(pld=r.json())

@api_view(['POST'])
def hook(request):
    if request.method == 'POST':
        if 'messages' in request.data:
            print(request.data)
            dialog_id = request.data['messages'][0]['chatId']
            r = Chat.objects(dialog_id__exists=dialog_id)
            if not r:
                message = Message()
                message.id_message = request.data['messages'][0]['id']
                message.body = request.data['messages'][0]['body']
                message.author = request.data['messages'][0]['author']
                message.sender_name = request.data['messages'][0]['senderName']
                message.time = request.data['messages'][0]['time']
                message.dialog_id = request.data['messages'][0]['chatId']
                message.assigned = False
                print(message.objects())
                queue = Queue()
                queue.unasigned_messages.append(message)
                print(queue.objects())
                queue.save()

        return std_response('Ok')

@api_view(['GET'])
def queue(request):
    if request.method == 'GET':
        r = Queue()
        print(dir(r))
        return Response('a')
