class Comuna():
    def __init__(self,comuna_nombre, comuna_farmacias):
        self.comuna_nombre = comuna_nombre
        self.comuna_farmacias = comuna_farmacias

    def __str__(self):
        data = {}
        data["Comuna_nombre"] = self.comuna_nombre
        data["Comuna_farmacias"] = self.comuna_farmacias
        return str(data)
