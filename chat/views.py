from django.shortcuts import render
from django.views import View
from datetime import datetime
import json

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response

# Services
from .services.messages import getMessages, sendMessage, sendFile
from .services.dialogs import getDialogs
from .services.users import getQrcode

# Models
from .models import Message, Chat, Queue

def std_response(msg='successful',pld={},status='Ok'):
    return Response({"status": status, "payload": pld, "message": msg})

class Index(View):
    template = 'index.html'

    def get(self, request):
        agent_name = "testing agent"
        return render(request, self.template, {'agent_name': agent_name})

@api_view(['POST'])
@parser_classes([FormParser, MultiPartParser])
def uploadFile(request):
    print(request)
    print(dir(request))
    print(request.FILES)
    print(request.query_params)
    print(request.data)
    #r = sendFile(**request.data)
    return std_response()

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

@api_view(['GET','POST'])
def dialogs(request):
    if request.method == 'GET':
        if 'cached' in request.query_params:
            chat = Chat.objects.all()
            return std_response(pld=chat.to_mongo)
        else:
            r = getDialogs()
            return std_response(pld=r.json())

    if request.method == 'POST':
        if 'chat_id' in request.data and 'status' in request.data:
            chat_id = request.data['chat_id']
            status = request.data['status']
            chat = Chat.objects(chat_id=chat_id)
            chat.update(type_chat=status)
            return std_response()

        elif not 'agent_id' in request.data or not 'chat_id' in request.data:
            return std_response(status='Error', msg='Missing argument')

        else:
            #set agent to a chat
            chat_id = request.data['chat_id']
            agent_id = request.data['agent_id']
            chat = Chat.objects(chat_id=chat_id)
            fields = {
                'agent_id': agent_id
            }
            chat.update(**fields)
            return std_response()

@api_view(['POST'])
def hook(request):
    if request.method == 'POST':
        if 'messages' in request.data:
            chatId = request.data['messages'][0]['chatId']
            is_assigned = Chat.objects(chat_id=chatId)
            agentId = None
            chat_request_id = request.data['messages'][0]['id']
            sender = request.data['messages'][0]['senderName']
            created_at = datetime.fromtimestamp(request.data['messages'][0]['time'])
            chat_is_read = chat_request_id.split("_")
            if  is_assigned:
                '''actualizar update_at/status(0)/'''
                if chat_is_read[0] == 'false':
                    chat_status = 'wait'
                else:
                    chat_status = 'new'
                fields = {
                    'type_chat': chat_status,
                    'status': False,
                    'updated_at': datetime.utcnow
                }
                is_assigned.update_one(**fields)
            else:
                chat_status = 'queue'
                fields = {
                    'chat_id': chatId,
                    'sender': sender,
                    'agent_id': agentId,
                    'status': True,
                    'type_chat': chat_status,
                    'created_at': created_at,
                }
                chat = Chat(**fields)
                chat.save()
        return std_response('Ok')

@api_view(['GET'])
def chat_info(request,status):
    if request.method == 'GET':
        chat_status = status
        if status == "all":
            chat = Chat.objects()
        else:
            chat = Chat.objects(type_chat=chat_status)
        return std_response(pld=json.loads(chat.to_json()))

@api_view(['POST'])
def update_label(request):
    if request.method == 'POST':
        chat_id = request.data['chat_id']
        label = request.data['label']
        chat = Chat.objects(chat_id=chat_id)
        chat.update(label=label)
        return std_response()

@api_view(['GET'])
def get_qr(request):
    qr = getQrcode()
    return std_response(pld=qr)
