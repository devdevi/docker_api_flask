class Farmacia():
    def __init__(self,nombre, direccion, telefono, latitud, longitud, comuna):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.latitud = latitud
        self.longitud = longitud
        self.comuna = comuna

    def __str__(self):
        data = {}
        data["Nombre"] = self.nombre
        data["Direccion"] = self.direccion
        data["Telefono"] = self.telefono
        data["Latitutd"] = self.latitutd
        data["Longitud"] = self.longitud
        data["Comuna"] = self.Comuna
        return str(data)
