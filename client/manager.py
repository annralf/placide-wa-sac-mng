import requests 
from datetime import datetime
import os

class Connection:
    urlBase = os.environ.get("HOST_DEV")

class Manager:
    def getQr(self, client_id):
        conn = Connection.urlBase
        client_id = str(client_id)
        url = conn+'/qr/'+client_id
        try:
            response = requests.get(url)
            code = response.json()
            if(code['status'] == 'Ok'):
                code = code['payload']
            else:
                code = None
            return code
        except:
            return 0


