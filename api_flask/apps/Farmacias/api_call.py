# Models
from api_flask.apps.Farmacias.models import Farmacia
# Api url
from api_flask.config import farmanet_url, headers
import requests
import simplejson as json
# Comunas
from api_flask.apps.Comunas.api_call import getComunas

farmacias = []

query = []

def getData():
    try:
        r = requests.post(farmanet_url)
        results = r.json()
        for data in results:
                setFarmacia(data)

    except requests.exceptions.ConnectionError as e:
        print(e)

def setFarmacia(elm):
    nombre = elm['local_nombre']
    direccion = elm['local_direccion']
    telefono = elm['local_telefono']
    latitud = elm['local_lat']
    longitud = elm['local_lng']
    comuna = elm['comuna_nombre']
    farmacia = Farmacia(nombre, direccion, telefono, latitud, longitud, comuna)
    farmacias.append(farmacia.__dict__)
    return farmacia.__dict__

def getFarmacias():
    getData()
    return farmacias


def filterComuna(comuna_param, farmacia_param):
    comuna_param = comuna_param.upper()
    farmacia_param = farmacia_param.upper()
    data_farmacias = getFarmacias()
    data_comunas = getComunas()
    for comuna in data_comunas:
        if comuna['comuna_nombre'] == comuna_param:
            for farmacia in data_farmacias:
                if  farmacia['comuna'] == comuna_param and farmacia['nombre'] == farmacia_param:
                    comuna['comuna_farmacias'].append(farmacia)
            query.append(comuna)
    return query