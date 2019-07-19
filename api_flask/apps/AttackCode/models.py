
class Attack():
    def __init__(self,name,count):
        self.name = name
        self.count = count

    def __str__(self):
        data = {}
        data["Name"] = self.name
        data["Count"] = self.count
        return str(data)