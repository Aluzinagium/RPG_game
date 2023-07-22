

class CharacterData():
    name = ''
    race = ''
    _class = ''
    armor = 0
    level = 1
    strength = 0
    dexterity = 0
    constitution = 0
    wisdom = 0
    intelligence = 0
    carisma = 0
    tendency = 'Neutral'
    alignment = 'Neutral'
    health = 10 + 8*constitution
    mana = 8 + 8*intelligence
    description = None
    weapon = 'No Weapon'
    isAlive = True


class Character():
    def __init__(self, obj):
        self._name = obj.name
        self._race = obj.race
        self._class = obj._class
        self._level = obj.level
        self._armor = obj.armor
        self._strength = obj.strength
        self._dexterity = obj.dexterity
        self._constitution = obj.constitution
        self._wisdom = obj.wisdom
        self._intelligence = obj.intelligence
        self._carisma = obj.carisma
        self._tendency = obj.tendency
        self._alignment = obj.alignment
        self._health = obj.health
        self._mana = obj.mana
        self._isAlive = obj.isAlive
        self._weapon = obj.weapon
        self._description = obj.description
        
    def talk(self, dialogue):
        self._dialogue = dialogue
        print(f"{self._name}: {self._dialogue}")
    def get_name(self):
        return self._name
    
    def attack(self):
            try:
               if self.weapon.w_type == 'Melee':
                    return self.weapon.damage + 10*self._strength
               elif self.weapon.w_type == 'Ranged':
                    return self.weapon.damage + 10*self._dexterity
            except:
               print("ERROR #7: Invalid Weapon type!!!")  
                 
                            
    def defend(self, dmg):
         return dmg - self.armor