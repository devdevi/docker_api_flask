class Site():
    def __init__(self,name,count,buckets,color, buckets_count, buckets_keys):
        self.name = name
        self.count = count
        self.buckets = buckets
        self.color = color
        self.buckets_count = buckets_count
        self.buckets_keys = buckets_keys

    def __str__(self):
        data = {}
        data["Name"] = self.name
        data["Count"] = self.count
        data["Buckets"] = self.buckets
        data["Color"] = self.color
        data["Buckets_count"] = self.buckets_count
        data["Buckets_keys"] = self.buckets_keys
        return str(data)
