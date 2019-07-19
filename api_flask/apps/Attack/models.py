class Country():
    def __init__(self,name,count,color,code):
        self.name = name
        self.count = count
        self.color = color
        self.code = code

    def __str__(self):
        data = {}
        data["Name"] = self.name
        data["Count"] = self.count
        return str(data)


