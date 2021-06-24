import requests
from chat._constants import *

### Dialogs functions ###

# Get one or more messages from WS api
# 100 last mesages by default
def getDialogs( limit = None, page = None, order = None ):
    payload = {'token': TOKEN}

    # Optional params
    if limit is not None:
        payload['limit'] = limit
    if page is not None:
        payload['page'] = page
    if order is not None:
        payload['order'] = order

    r = requests.get(f'{API_URL}/dialogs', params=payload)
    return r

# Send messages to WS api
def getDialogInfo():
    payload = {'token': TOKEN}

    r = requests.post(f'{API_URL}/sendMessage', params = payload, 
                        data = {'body': body} )
    return r

# Set "typing..." status to chat
def toggleTypingStatus( chatId = None, phone = None, on = True, duration = 3 ):
    payload = {'token': TOKEN}

    # Optionals parameters
    if not chatId and not phone:
        raise Exception('Need chatId or phone to set the state')
    if chatId is not None:
        payload['chatId'] = chatId
    else:
        payload['phone'] = phone

    payload['on'] = on
    payload['duration'] = duration

    r = requests.post(f'{API_URL}/typing', params = payload)
    return r
