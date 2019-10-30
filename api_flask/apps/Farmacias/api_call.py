# Models
from api_flask.apps.Farmacias.models import Farmacia
# Api url
from api_flask.config import farmanet_url, headers
import requests
import simplejson as json

farmacias = []

def getData():
    query = {}
    print(farmanet_url)
    try:
        r = requests.post(farmanet_url)
        results = r.json()
        for data in results:
            if data != ',Elija Comuna':
                setFarmacia(data)
    except requests.exceptions.ConnectionError as e:
        print(e)

def setFarmacia(elm):
    nombre = elm['local_nombre']
    direccion = elm['local_direccion']
    telefono = elm['local_telefono']
    latitud = elm['local_lat']
    longitud = elm['local_lng']
    farmacia = Farmacia(nombre, direccion, telefono, latitud, longitud)
    farmacias.append(farmacia.__dict__)
    return farmacia.__dict__

def getFarmacias():
    getData()
    return farmacias
