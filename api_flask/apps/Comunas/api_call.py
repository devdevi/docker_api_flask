# Models
from api_flask.apps.Comunas.models import Comuna
# Api url
from api_flask.config import minsal_url

# from api_flask.apps.firestore_services import get_comunas
import requests
import simplejson as json
import datetime
from requests_toolbelt.multipart.encoder import MultipartEncoder
import re

multipart_data = MultipartEncoder(
    fields={
            'reg_id': '7',
           }
    )

headers = {"content-type": "multipart/form-data"}

comunas = []

def getData():
    try:
        r = requests.post(minsal_url,
            data=multipart_data,
            headers={'Content-Type': multipart_data.content_type})
        cleanr = re.compile('<.*?>')
        cleantext = re.sub(cleanr, ',', r.text)
        results = cleantext.split(",,")
        for data in results:
            if data != ',Elija Comuna':
                setComuna(data)
        return results
    except requests.exceptions.ConnectionError as e:
        print(e)

def setComuna(elm):
    comuna_nombre = elm
    comuna_farmacias = []
    comuna = Comuna(comuna_nombre, comuna_farmacias)
    comunas.append(comuna.__dict__)
    return comuna.__dict__

def getComunas():
    getData()
    return comunas