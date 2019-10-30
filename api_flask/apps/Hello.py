from flask_restful import Resource


class Hello(Resource):
    def get(self):
        data = {"message": "Api flask Farmacias de turno",
                "endpoints": {
                    "comunas":"http://127.0.0.1:5000/api/v1/comunas",
                    "farmacias": "http://127.0.0.1:5000/api/v1/farmacias",
                    "filtro": "http://127.0.0.1:5000/api/v1/comuna/<nombre_comuna>/farmacia/<nombre_farmacia>",
                    "ejemplo_filtro": "http://127.0.0.1:5000/api/v1/comuna/providencia/farmacia/ahumada",
                }}
        return data