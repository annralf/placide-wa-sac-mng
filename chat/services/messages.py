import requests
from chat._constants import *

### Messages functions ###

# Get one or more messages from WS api
# 100 last messages by default
def getMessages( lastMessageNumber = None, last = None, chatId = None,
                limit = None, min_time = None, max_time = None, token, instance ):
    payload = {'token': token}

    # Optional params
    if lastMessageNumber is not None:
        payload['lastMessageNumber'] = lastMessageNumber 
    if last is not None:
        payload['last'] = last
    if chatId is not None:
        payload['chatId'] = chatId
    if limit is not None:
        payload['limit'] = limit
    if min_time is not None:
        payload['min_time'] = min_time
    if max_time is not None:
        payload['max_time'] = max_time

    r = requests.get(f'{API_URL}/{instance}/messages', params=payload)
    return r

# Send messages to WS api
def sendMessage( body,quotedMsgId = None,chatId = None,phone = None,
                mentionedPhones = None, token, instance ):
    payload = {'token': token}

    # Optional parameters
    if not chatId and not phone:
        raise Exception('Need chatId or phone to send the message')
    if chatId is not None:
        payload['chatId'] = chatId
    else:
        payload['phone'] = phone
    if quotedMsgId is not None:
        payload['quotedMsgId'] = quotedMsgId
    if mentionedPhones is not None:
        payload['mentionedPhones'] = mentionedPhones

    r = requests.post(f'{API_URL}/{instance}/sendMessage', params = payload, 
                        data = {'body': body} )
    return r

# Forward message to a new or existing chat
def forwardMessage( body,messageId, chatId = None, phone = None,token, instance ):
    payload = {'token': token}

    # Optional paramenters
    if not chatId and not phone:
        raise Exception('Need chatId or phone to send the message')
    if chatId is not None:
        payload['chatId'] = chatId
    else:
        payload['phone'] = phone

    r = requests.post(f'{API_URL}/{instance}/forwardMessage', params = payload,
                        data = {'body': body} )
    return r

# Send a file
def sendFile( body, filename, caption = None ,quotedMsgId = None, cached = None,
                chatId = None, phone = None, mentionedPhones = None, token,
                instance ):
    payload = {'token': token}

    # Optional parameters
    if not chatId and not phone:
        raise Exception('Need chatId or phone to send the message')
    if chatId is not None:
        payload['chatId'] = chatId
    else:
        payload['phone'] = phone
    if quotedMsgId is not None:
        payload['quotedMsgId'] = quotedMsgId
    if quotedMsgId is not None:
        payload['caption'] = quotedMsgId
    if quotedMsgId is not None:
        payload['cached'] = quotedMsgId
    if mentionedPhones is not None:
        payload['mentionedPhones'] = mentionedPhones

    r = requests.post(f'{API_URL}/{instance}/sendFile', params = payload, 
                        data = {'body': body} )
    return r

# Get History of messages
def history( page = None, count = None, chatId = None ):
    payload = {'token': TOKEN}

    # Optional parameters
    if page is not None:
        payload['page'] = page
    if count is not None:
        payload['count'] = count
    if chatId is not None:
        payload['chatId'] = chatId

    r = requests.post(f'{API_URL}/messagesHistory', params = payload)

    return r

# Delete a message from Ws
def deleteMessage( messageId ):
    payload = {'token': TOKEN}

    # Paramater
    payload['messageId'] = messageId

    r = requests.post(f'{API_URL}/deleteMessage', params = payload)
    return r
