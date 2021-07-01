import requests
import base64
from io import BytesIO
from chat._constants import *

### Users functions ###

# Get user status
def userStatus( chatId = None, phone = None ):
    payload = {'token': TOKEN}

    # Parameters
    if not chatId and not phone:
        raise Exception('Need chatId or phone to know the status')

    if chatId is not None:
        payload['chatId'] = chatId
    else:
        payload['phone'] = phone

    r = requests.post(f'{API_URL}/userStatus', params = payload )
    return r

# Get instance qr code
def getQrcode():

    r = requests.get(f'{API_URL}/qr_code', params = {'token': TOKEN} )
    qr = BytesIO(r.content)
    data = base64.encodebytes(qr.getvalue()).decode('utf-8')
    return data
