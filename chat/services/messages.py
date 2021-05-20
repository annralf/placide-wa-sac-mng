import requests
from chat._constants import *

### Messages functions ###

# Get one or more messages from WS api
# 100 last mesages by default
def getMessages( lastMessageNumber = None, last = None, chatId = None,
                limit = None, min_time = None, max_time = None ):
    payload = {'token': TOKEN}

    # Optional params
    if lastMessageNumber is not None:
        payload['lastMessageNumber'] = lastMessageNumber 
    if las is not None:
        payload['last'] = last
    if chatId is not None:
        payload['chatId'] = chatId
    if limit is not None:
        payload['limit'] = limit
    if min_time is not None:
        payload['min_time'] = min_time
    if max_time is not None:
        payload['max_time'] = max_time

    r = requests.get(f'{API_URL}/messages', params=payload)
    return r

# Send messages to WS api
def sendMessage( body,quotedMsgId = None,chatId = None,phone = None,
                mentionedPhones = None ):
    payload = {'token': TOKEN}

    # Optional parameters
    if not chatId and not phone:
        raise Exception('Need chatId or phone to send the message')
    if chatId is not None:
        payload['chatId'] = chatId
    else:
        payload['phone'] = phone
    if mentionedPhones is not None:
        payload['mentionedPhones'] = mentionedPhones

    r = requests.post(f'{API_URL}/sendMessage', params = payload, 
                        data = {'body': body} )
    print(r.text)
    return r

# Forward message to a new or existing chat
def forwardMessage( body,messageId, chatId = None, phone = None ):
    payload = {'token': TOKEN}

    # Optional paramenters
    if not chatId and not phone:
        raise Exception('Need chatId or phone to send the message')
    if chatId is not None:
        payload['chatId'] = chatId
    else:
        payload['phone'] = phone

    r = requests.post(f'{API_URL}/forwardMessage', params = payload,
                        data = {'body': body} )
    return r
