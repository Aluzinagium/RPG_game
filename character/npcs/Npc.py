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


class NPC(Character):
    def __init__(self, obj):
        super().__init__(obj)
        self._loot = obj.loot
        self.weapon = obj.weapon

    def get_loot(self):
        return self.loot


# ---------------ENCODER E DECODER PARA SALVAMENTO----------------------


class NPC_Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, NPC):
            return {
                "name"        : obj.get_name(),
                "race"        : obj.get_race(),
                "classe"      : obj.get_class(),
                "armor"       : obj.get_armor(),
                "strength"    : obj.get_strength(),
                "dexterity"   : obj.get_dexterity(),
                "constitution": obj.get_constitution(),
                "wisdom"      : obj.get_wisdom(),
                "intelligence": obj.get_intelligence(),
                "carisma"     : obj.get_carisma(),
                "tendency"    : obj.get_tendency(),
                "alignment"   : obj.get_alignment(),
                "health"      : obj.get_health(),
                "mana"        : obj.get_mana(),
                "isAlive"     : obj.get_isALive(),
                "description" : obj.get_description(),
                "level"       : obj.get_level(),
                "loot"        : obj.get_loot(),
            }
        return super().default(obj)


class NPC_Decoder(json.JSONDecoder):
    def decode(self, obj):
        decoded_npc = super().decode(obj)
        if "NPC" in decoded_npc:
            decoded_npc = decoded_npc["NPC"]
            # cria uma instância de NPC com base nos dados do dicionário salvo
            npcData              = NPCData()
            npcData.name         = decoded_npc["name"]
            npcData.race         = decoded_npc["race"]
            npcData._class       = decoded_npc["classe"]
            npcData.armor        = decoded_npc["armor"]
            npcData.strength     = decoded_npc["strength"]
            npcData.constitution = decoded_npc["constitution"]
            npcData.wisdom       = decoded_npc["wisdom"]
            npcData.intelligence = decoded_npc["intelligence"]
            npcData.carisma      = decoded_npc["carisma"]
            npcData.tendency     = decoded_npc["tendency"]
            npcData.alignment    = decoded_npc["alignment"]
            npcData.health       = decoded_npc["health"]
            npcData.mana         = decoded_npc["mana"]
            npcData.isAlive      = decoded_npc["isAlive"]
            npcData.description  = decoded_npc["description"]
            npcData.level        = decoded_npc["level"]
            npcData.loot         = decoded_npc["loot"]
            return npcData
        return super().decode(obj)
