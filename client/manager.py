import requests 
from datetime import datetime
import os
from  client.models import Client as Cli

class Connection:
    urlBase = os.environ.get("HOST_DEV")

class Manager:
    def getQr(self, client_id):
        conn = Connection.urlBase
        agent =   Cli.objects.get(id=client_id)  
        client_id = str(client_id)
        url = conn+'/qr/'+agent.token+'/'+agent.instance
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


