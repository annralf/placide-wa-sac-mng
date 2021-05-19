import requests
from ._constants import *

#GET messages from WS api
#100 last mesages by default
def getMessages(lastMessageNumber=None,last=None,chatId=None,
                limit=None,min_time=None,max_time=None):
    payload = {'token': TOKEN}

    #Optional params
    payload['lastMessageNumber'] = lastMessageNumber 

    r = requests.get(f'{API_URL}/messages', params=payload)
    return r
