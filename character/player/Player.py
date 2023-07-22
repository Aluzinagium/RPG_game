# -*- coding: utf-8 -*-
import json
import sys

from items.Item import Item
from character.Character import Character, CharacterData

"""
Created on Wed Jul 19 21:10:28 2023

PLAYER FOLDER


@author: User
"""

class PlayerData(CharacterData):
     inventory = []
 
class Player(Character):
    
    def __init__(self, obj):
        super().__init__(obj)
        self.inventory = obj.inventory
        
        
        
        #-----------------------SETTERS DOS ATRIBUTOS---------------------        
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
         
    #------------------------Outros SETTERS Importantes---------------------
    
    def set_class(self, _class):
         self._class = _class
         
    
    #------------------------GETTERS DOS ATRIBUTOS-------------------------
    
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
    
    # -----------------Outros GETTERS importantes------------------
    def get_name(self):
         return self._name
    def get_race(self):
         return self._race
    def get_class(self):
         return self._class
    def get_description(self):
         return self._description
    def get_tendency(self):
         return self._tendency
    def get_alignment(self):
         return self._alignment
    def get_level(self):
         return self._level
    
    def attack(self, weapon):
        if weapon == "Ranged":
            return 8 * self._dexterity
        elif weapon == "Magic":
            return 8 * self._intelligence
        elif weapon == "Melee":
            return 8 * self._strength
    
    def add_item_inv(self, item):
        if isinstance(item, Item):
            self.inventory.append(item)
        else:
            print("Não é um item válido para se colocar no inventário.")
    
    def get_inventory(self):
        print(" Nome ----------------Tipo ------------- Descrição")
        for items in self.inventory:
            print(f"{items.get_name()}   -     {items.get_type()}    - {items.get_description()}")
    
    
    #self, name, rc,_class, con, tend='Neutral', align='Neutral', desc='', level=1
class Player_Encoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, Player):
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
                        "inventory": obj.get_inventory()}
            return super().default(obj)
        
        
class Player_Decoder(json.JSONDecoder):
    def decode(self, obj):
        decoded_player = super().decode(obj)
        if "Player" in decoded_player:
            decoded_player = decoded_player['Player']
            #cria uma instância de Player com base nos dados do dicionário salvo
            playerData = PlayerData()
            playerData.name = decoded_player["name"]
            playerData.race = decoded_player["race"] 
            playerData._class = decoded_player["classe"]
            playerData.constitution = decoded_player["constitution"]
            playerData.tendency = decoded_player["tendency"]
            playerData.alignment = decoded_player["alignment"]
            playerData.description = decoded_player["description"]
            playerData.level = decoded_player["level"]
            return playerData
        return super().decode(obj)
        
        
        
        
        
        
        
        
        
        