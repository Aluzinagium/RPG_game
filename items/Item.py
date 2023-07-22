

class ItemData():
    name = ''
    type = ''
    description = ''
    

class Item():
    def __init__(self, obj):
        self.name = obj.name
        self.type = obj.type
        self.description = obj.description
        
    def get_name(self):
        return self.name
    
    def get_type(self):
        return self.type
        
    def get_description(self):
        return self.description
    
    