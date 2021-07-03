import requests 
from datetime import datetime
import os

class Connection:
    urlBase = os.environ.get("HOST_DEV")

class Manager:
    def getChats(self, type='all'):
        conn = Connection.urlBase
        url = conn+"/filter/"+type
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
            if label in chat:
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

    def getChatDetail(self, chat_id):
        #Get chats details
        conn = Connection.urlBase
        url = conn+"/messages?chatId="+chat_id
        response = requests.get(url)
        chats = response.json()
        list = []
        for chat in chats['payload']['messages'] :
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
        return list

    def sendMessage(self, body, phone):
        #Message Sender
        conn = Connection.urlBase
        url = conn+"/messages/"
        payload = {"messages": [
        {
            "body":body,
            "chatId": phone
        }
        ]}
        headers = {"Content-Type": "application/json"}
        response = requests.request("POST", url, json=payload, headers=headers)
        return True
