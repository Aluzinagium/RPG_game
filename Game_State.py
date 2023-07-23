from character.player.Player import Player
from character.npcs.Npc import NPC
from scenes.Scene import Scene

class Game_State_Data():
    playerstate = 'player'
    npcstate    = []
    scenestate  = 'scene'
    

class Game_State():
    def __init__(self, obj):
        
        self.player = obj.playerstate
        self.npc = []
        self.scene = obj.scenestate


    def get_npcs(self):
        for npcs in self.npc:
            for n in npcs:
                npcs.get_name()
        
        





def current_Scene(self, scene):
    return 0

def current_Combat(self, Combat):
    return 0

def current_building(self, building):
    return 0

def current_settlement(self, settlement):
    return 0

def NPC_state(self, NPC):
    return 0

def Player_state(self, Player):
    return 0


    