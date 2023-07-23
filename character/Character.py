from items.Item import Item

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
    dialogue = ""


class Character():
    def __init__(self, obj):
        self._name         = obj.name
        self._race         = obj.race
        self._class        = obj._class
        self._level        = obj.level
        self._armor        = obj.armor
        self._strength     = obj.strength
        self._dexterity    = obj.dexterity
        self._constitution = obj.constitution
        self._wisdom       = obj.wisdom
        self._intelligence = obj.intelligence
        self._carisma      = obj.carisma
        self._tendency     = obj.tendency
        self._alignment    = obj.alignment
        self._health       = obj.health
        self._mana         = obj.mana
        self._isAlive      = obj.isAlive
        self._weapon       = obj.weapon
        self._description  = obj.description
        self._dialogue     = obj.dialogue
        

          
        #-------------------STAT GETTERS --------------------
        
    def get_strength(self):
         return self._strength
    def get_dexterity(self):
         return self._dexterity
    def get_constitution(self):
         return self._constitution
    def get_wisdom(self):
         return self._wisdom
    def get_intelligence(self):
         return self._intelligence
    def get_carisma(self):
         return self._carisma
    def get_health(self):
         return self._health
    def get_mana(self):
         return self._mana
        
#---------------------OTHER IMPORTANT GETTERS-------------------
    def get_name(self):
         return self._name
    def get_race(self):
         return self._race
    def get_class(self):
         return self._class
    def get_armor(self):
         return self._armor
    def get_tendency(self):
         return self._tendency
    def get_alignment(self):
         return self._alignment
    def get_level(self):
         return self._level
    def get_weapon(self):
         return self.weapon
    def get_description(self):
         return self._description
    def get_isALive(self):
         return self._isAlive
    
                
             
 #----------------------------STAT SETTERS--------------------------
 
    def set_strength(self, value):
         self._strength = value
    
    def set_dexterity(self, value):
         self._dexterity = value
         
    def set_constitution(self, value):
         self._constitution = value
         
    def set_wisdom(self, value):
         self._wisdom = value
         
    def set_intelligence(self, value):
         self._intelligence = value
         
    def set_carisma(self, value):
         self._carisma = value
         
    def set_health(self, value):
         self._health = value
         
    def set_mana(self, value):
         self._mana = value
         
         
# --------------- OTHER SETTERS------------------
    def set_name(self, new_name):
         self._name = new_name
    def set_race(self, new_race):
         self._race = new_race
    def set_class(self, new_class):
         self._class = new_class
    def set_armor(self, new_armor):
         self._armor = new_armor
    def set_level(self, new_level):
         self.level = new_level
    def set_alignment(self, new_alignment):
         self._alignment = new_alignment
    def set_tendency(self, new_tend):
         self._tendency = new_tend
    def set_description(self, new_desc):
         self._description = new_desc
         
    def set_weapon(self, item):
          if item.type == 'arma':
               self._weapon = item
     
    def set_isAlive(self, value):
         self.isAlive = value
             
             
    # -------------GENERAL METHODS---------------
    
    def talk(self, dialogue):
        self._dialogue = dialogue
        print(f"{self._name}: {self._dialogue}")
    
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
    