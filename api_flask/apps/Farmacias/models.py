class Farmacia():
    def __init__(self,nombre, direccion, telefono, latitud, longitud):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.latitud = latitud
        self.longitud = longitud

    def __str__(self):
        data = {}
        data["Nombre"] = self.nombre
        data["Direccion"] = self.direccion
        data["Telefono"] = self.telefono
        data["Latitutd"] = self.Latitutd
        data["Longitud"] = self.Longitud
        return str(data)
