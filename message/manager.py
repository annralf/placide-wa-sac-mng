import requests 
from datetime import datetime
import os
from  client.models import Client

class Connection:
    urlBase = os.environ.get("HOST_DEV")

class Manager:
    def getChats(self, type, client_id):
        conn = Connection.urlBase
        print(client_id)
        try:
            client = Client.objects.get(id=client_id) 
            url = conn+"/filter/"+type+"/"+client.token+"/"+client.instance
            response = requests.get(url)
            chatList = response.json()
            list = []
            for chat in chatList['payload']:
                assigned_to = "N/A"
                label = "N/A"
                if 'sender' in chat:
                    sender = chat['sender']
                else:
                    sender = chat['chat_id']
                if 'agent_id' in chat:
                    assigned_to = chat['agent_id']
                if 'label' in chat:
                    label = chat['label']
                detail = {
                    'chat_id':chat['chat_id'],
                    'sender' : sender,
                    'label' : label,
                    'status' : chat['status'],
                    'is_assigned' : assigned_to,
                    'type_chat' : chat['type_chat']
                }
                list.append(detail)
            return list
        except:
            return 0

    def getChatDetail(self, chat_id, client_id):
        #Get chats details
        conn = Connection.urlBase
        client = Client.objects.filter(id=client_id).first() 
        url = conn+"/messages/"+client.token+"/"+client.instance+"/?chatId="+chat_id
        response = requests.get(url)
        chats = response.json()
        list = []
        try:
            for chat in chats['payload']['messages']:
                chat_request_id = chat['id']
                chat_is_read = chat_request_id.split("_")
                message = {
                    'is_client' : chat['fromMe'],
                    'time' : datetime.fromtimestamp(chat['time']),
                    'sender' : chat['senderName'],
                    'phone_number' :  chat['chatName'],
                    'is_response' : chat_is_read[0],
                    'message' : chat['body'],
                    'chat_id' :chat_id
                }
                list.append(message)
        except:
            print(chats)
        return list

    def sendMessage(self, body, phone, client_id):
        #Message Sender
        conn = Connection.urlBase
        client = Client.objects.filter(id=client_id).first() 
        url = conn+"/messages/"
        payload = {"messages": [
        {
            "body":body,
            "chatId": phone,
            "token" : client.token,
            "instance" : client.instance
        }
        ]}
        headers = {"Content-Type": "application/json"}
        response = requests.request("POST", url, json=payload, headers=headers)
        return True

    def setLabel(self, chat_id, label, client_id):
        conn = Connection.urlBase
        client = Client.objects.filter(id=client_id).first()
        url = conn+"/label"
        payload = {
            "chat_id": chat_id,
            "label": label,
            "token" : client.token,
            "instance" : client.instance
        }
        headers = {"Content-Type": "application/json"}
        response = requests.request("POST", url, json=payload, headers=headers)
        return True

    def set(self, chat_id, status, agent_id, client_id):
        conn = Connection.urlBase
        url = conn+"/chats"
        client = Client.objects.filter(id=client_id).first()
        headers = {"Content-Type": "application/json"}
        if(agent_id != None):
            status_data = {
                "chat_id": chat_id,
                "status": status,
                "token" : client.token,
                "instance" : client.instance
            }
            agent_data = {
                "chat_id": chat_id,
                "agent_id": agent_id,
                "token" : client.token,
                "instance" : client.instance
            }
            response_status = requests.request("POST", url, json=status_data, headers=headers)
            response_agent = requests.request("POST", url, json=agent_data, headers=headers)
        else:
            status_data = {
                "chat_id": chat_id,
                "status": status,
                "token" : client.token,
                "instance" : client.instance
            }
            response_status = requests.request("POST", url, json=status_data, headers=headers)
        return True
