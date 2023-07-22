# -*- coding: utf-8 -*-
import json
from items.weapons.weapon import Weapon
from items.Item import Item
from character.Character import Character, CharacterData
"""
Created on Thu Jul 20 18:34:29 2023

NPC FOLDER

@author: User
"""


class NPCData(CharacterData):
     loot = []
     weapon = 'no weapon'

class NPC(Character):

    def __init__(self, obj):
        super().__init__(obj)
        self._loot = obj.loot
        self.weapon = obj.weapon
        
        
        #-------------------GETTERS DOS ATRIBUTOS---------------------
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
        
        #---------------------OUTROS GETTERS IMPORTANTES---------------------
    def get_classe(self):
         return self._class
    def get_level(self):
         return self._level
    def get_loot(self):
         return self.loot
    def get_mana(self):
         return self._mana
    def get_weapon(self):
         return self.weapon
    
                
             
 #----------------------------SETTERS DOS ATRIBUTOS--------------------------
 
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
         
 # -------------MÉTODOS GERAIS---------------
 
    def set_weapon(self, weapon):
          if(isinstance(weapon, Weapon)):
              self.weapon = weapon
         
         
#---------------ENCODER E DECODER PARA SALVAMENTO----------------------

class NPC_Encoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, NPC):
                return {"name" : obj.get_name(),
                        "race": obj.get_race(),
                        "classe": obj.get_class(),
                        "armor": obj.get_armor(),
                        "strength": obj.get_strength(),
                        "dexterity": obj.get_dexterity(),
                        "constitution": obj.get_constitution(),
                        "wisdom": obj.get_wisdom(),
                        "intelligence": obj.get_intelligence(),
                        "carisma": obj.get_carisma(),
                        "tendency": obj.get_tendency(),
                        "alignment": obj.get_alignment(),
                        "health": obj.get_health(),
                        "mana": obj.get_mana(),
                        "isAlive": obj.isAlive(),
                        "description": obj.get_description(),
                        "level": obj.get_level(),
                        "loot": obj.get_loot()}
            return super().default(obj)
        
        
class NPC_Decoder(json.JSONDecoder):
    def decode(self, obj):
        decoded_npc = super().decode(obj)
        if "Player" in decoded_npc:
            decoded_npc = decoded_npc['NPC']
            #cria uma instância de NPC com base nos dados do dicionário salvo
            npcData = NPCData()
            npcData.name = decoded_npc["name"]
            npcData.race = decoded_npc["race"] 
            npcData._class = decoded_npc["classe"]
            npcData.constitution = decoded_npc["constitution"]
            npcData.tendency = decoded_npc["tendency"]
            npcData.alignment = decoded_npc["alignment"]
            npcData.description = decoded_npc["description"]
            npcData.level = decoded_npc["level"]
            return npcData
        return super().decode(obj)
         
    
    