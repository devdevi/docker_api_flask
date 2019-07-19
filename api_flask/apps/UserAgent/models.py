class UserAgent():
    def __init__(self,name,count,agent_type,percentage):
        self.name = name
        self.count = count
        self.agent_type = agent_type
        self.percentage = percentage

    def __str__(self):
        data = {}
        data["Name"] = self.name
        data["Count"] = self.count
        data["Agent_type"] = self.agent_type
        data["percentage"] = self.percentage

        return str(data)
