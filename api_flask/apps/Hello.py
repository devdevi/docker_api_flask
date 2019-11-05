from flask_restful import Resource


class Hello(Resource):
    def get(self):
        data = {"message": "Api flask Farmacias de turno",
                "endpoints": {
                    "comunas":"https://farmaciapi.herokuapp.com/api/v1/comunas",
                    "farmacias": "https://farmaciapi.herokuapp.com/api/v1/farmacias",
                    "filtro": "https://farmaciapi.herokuapp.com/api/v1/comuna/<nombre_comuna>/farmacia/<nombre_farmacia>",
                    "ejemplo_filtro": "https://farmaciapi.herokuapp.com/api/v1/comuna/providencia/farmacia/ahumada",
                }}
        return data