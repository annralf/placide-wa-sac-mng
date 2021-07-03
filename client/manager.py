import requests 
from datetime import datetime
from chat ._constants import *

class Manager:
    def getQr(self):
        url = BASE+'qr'
        response = requests.get(url)
        code = response.json()
        if(code['status'] == 'Ok'):
            code = code['payload']
        else:
            code = None
        return code


