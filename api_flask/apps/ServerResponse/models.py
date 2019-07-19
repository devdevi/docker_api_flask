class Response():
    def __init__(self,key, count):
        self.key = key
        self.count = count
    
    def __str__(self):
        data = {}
        data["Key"] = self.key
        data["Count"] = self.count
        return str(data)
