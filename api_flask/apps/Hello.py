from flask_restful import Resource


class Hello(Resource):
    def get(self):
        return {"message": "Api flask  Dashboard Banco de chile"}