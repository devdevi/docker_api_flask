import os

basedir = os.path.abspath(os.path.dirname(__file__))
farmanet_url = "https://farmanet.minsal.cl/maps/index.php/ws/getLocalesRegion?id_region=7"
minsal_url = "https://midastest.minsal.cl/farmacias/maps/index.php/utilidades/maps_obtener_comunas_por_regiones"
headers = {"content-type": "application/json"}
