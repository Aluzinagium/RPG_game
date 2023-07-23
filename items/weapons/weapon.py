
from items.Item import Item, ItemData

class WeaponData(ItemData):
       w_type = ''
       damage = 0
       

    
class Weapon(Item):
    def __init__(self, obj):
        super().__init__(obj)
        self.w_type = obj.w_type
        self.damage = obj.damage
       
    
    def set_atk_damage(self, value):
        if(value > 0):
            self.damage = value
        else:
            self.size = 0
    def get_range(self):
        try:
            if self.atk_type == "melee":
                self.range = "close"
            else:
                self.range = "far"
        except:
            print("ERROR #5: Alcance inválido")
                
        return self.range
    
    def get_name(self):
        return self.name
    
    def get_type(self):
        return self.type
    
    
    