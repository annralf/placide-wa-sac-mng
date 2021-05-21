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
    print(r.text)
    return r
