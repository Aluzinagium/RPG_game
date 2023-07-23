# -*- coding: utf-8 -*-
import json
import sys
import os
import time

from items.Item import Item
from character.Character import Character, CharacterData
from utils.default import *

"""
Created on Wed Jul 19 21:10:28 2023

PLAYER FOLDER


@author: User
"""

class PlayerData(CharacterData):
     inventory = []
     
     def stats_distribution(self,values):
         
          os.system('cls')
          ordered_values = [0] * len(values)
          used_values = []
          for i, stats in enumerate(STATS_ORDER, start = 1):
               while True:
                    print(" Write the stats you want each of the values to be assigned to, sequentially to the order listed here:")
                    print(f"Stats : {STATS_ORDER}")
                    print(f"Values to assign: {values}")
                    print(f" Stat to assign: {i}- {stats}")
                    value = input ("Assigned to be assigned: >> ")
                    print(value)
                    try:
                         value = int(value)
                         if value in values:
                              print("value assigned!!")
                              time.sleep(1)
                              values.remove(value)
                              ordered_values[i-1] = value
                              os.system('cls')
                              break
                         else:
                              print("invalid value. DON'T TRY TO CHEAT, HUH!!" )
                              time.sleep(1)
                              os.system('cls')
                    except ValueError:
                         print("Invalid input. Try again.")
                         time.sleep(1)
                         os.system('cls')
                         
          self.strength = ordered_values[0]
          self.dexterity = ordered_values[1]
          self.constitution = ordered_values[2]
          self.wisdom = ordered_values[3]
          self.intelligence = ordered_values[4]
          self.carisma = ordered_values[5]
          
          print("VALORES ATRIBUÍDOS COM SUCESSO!! Veja:")
          print(f" Strength    : {self.strength}\n Dexterity   : {self.dexterity}\n Constitution: {self.constitution}\n Wisdom      : {self.wisdom}\n Intelligence: {self.intelligence}\n Carisma     : {self.carisma}\n")
 
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
            print("Not a Valid item to be put in the inventory.")
    
    def get_inventory(self):
        print("-------------------INVENTORY-------------------")
        print("Name".rjust(25) + "\tType\t" +  "Description".ljust(15))
        for items in self.inventory:
            print(f"{items.get_name()}\t   -     {items.get_type()}\t    - {items.get_description()}")
    
    def check_player_info(self):
         
         return (f" Name: {self.get_name()}\t Race: {self.get_race()}\n class: {self.get_class()}\t armor: {self.get_armor()}\n Description: {self.get_description()} \n\n \
              ------------------STATS-------------------: \n\n \
                 Strength: {self.get_strength()}\t        Dexterity: {self.get_dexterity()}\n \
                 Constitution: {self.get_constitution()}\t Wisdom: {self.get_wisdom()}\n \
                 Intelligence: {self.get_intelligence()}\t Carisma: {self.get_carisma()}\n\n ")
   
   
class Player_Encoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, Player):
                return {"name" :         obj.get_name(),
                        "race":          obj.get_race(),
                        "classe":        obj.get_class(),
                        "armor":         obj.get_armor(),
                        "strength":      obj.get_strength(),
                        "dexterity":     obj.get_dexterity(),
                        "constitution":  obj.get_constitution(),
                        "wisdom":        obj.get_wisdom(),
                        "intelligence":  obj.get_intelligence(),
                        "carisma":       obj.get_carisma(),
                        "tendency":      obj.get_tendency(),
                        "alignment":     obj.get_alignment(),
                        "health":        obj.get_health(),
                        "mana":          obj.get_mana(),
                        "isAlive":       obj.isAlive(),
                        "description":   obj.get_description(),
                        "level":         obj.get_level(),
                        "inventory":     obj.get_inventory()}
            return super().default(obj)
        
        
class Player_Decoder(json.JSONDecoder):
    def decode(self, obj):
        decoded_player = super().decode(obj)
        if "Player" in decoded_player:
            decoded_player = decoded_player['Player']
            #cria uma instância de Player com base nos dados do dicionário salvo
            playerData = PlayerData()
            playerData.name          = decoded_player["name"]
            playerData.race          = decoded_player["race"] 
            playerData._class        = decoded_player["classe"]
            playerData.constitution  = decoded_player["constitution"]
            playerData.tendency      = decoded_player["tendency"]
            playerData.alignment     = decoded_player["alignment"]
            playerData.description   = decoded_player["description"]
            playerData.level         = decoded_player["level"]
            return playerData
        return super().decode(obj)
        
        
        
        
        
        
        
        
        
        