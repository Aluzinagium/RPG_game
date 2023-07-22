# -*- coding: utf-8 -*-


import sys
import os
from items.Item import Item, ItemData
from character.player.Player import Player, PlayerData
from saves.Save_Game import Save
from items.weapons.weapon import Weapon, WeaponData
from character.npcs.Npc import NPC, NPCData
from utils.default import STRING_SENTENCES

"""
Created on Thu Jul 20 19:23:14 2023


SCENE FOLDER
@author: User
"""

class Scene():
    
    def main_menu_scene():
       # scenestate = 
        print(STRING_SENTENCES['title'])
        
        print("""Choose your option:
        1. Play
        2. Continue
        3. Exit:
        4. Testing grounds """)
        
        menu_selection = int(input(">> "))
                
                
                
        if menu_selection == 1:
            print ("Game started!")
           
        
            
        elif menu_selection == 2:
            print("Carregando arquivo salvo...")
           # player_loader_state = #save.load_game(r"C:\Users\User\OneDrive\Coding Adventure\Python\RPG_game\saves\player_save.json")
          #  player = Player(player_loader_state)
          
            
        elif menu_selection == 3:
            print("Exiting game")
            sys.exit()
        elif menu_selection == 4:
            playerdata = PlayerData()
            playerdata.name = "João"
            playerdata.race = "human"
            playerdata._class = "Thief"
            playerdata.description = "Um ladrãozinho"
            playerdata.constitution = 6
            player = Player(playerdata)
            
            
            
            itemdata = ItemData()
            itemdata.name = "Poção de cura"
            itemdata.type = "poção"
            itemdata.description = "Uma poção que restaura vida"
            pocao_cura = Item(itemdata)
            
            espada = WeaponData()
            espada.name = "Espada Bastarda"
            espada.type = "Arma"
            espada.description = "Uma espada pesada e longa. O peso em si já é fatal."
            espada.w_type = "melee"
            espada.damage = 12
            
            
            
            player.add_item_inv(pocao_cura)
            player.add_item_inv(Weapon(espada))
            player.print_inventory()
            
            print("\n\n\n\n\n")
            
            npcData = NPCData()
            npcData.name = "Bandido"
            npcData.description = "Um Bandido miserável"
            npcData.race = "Humano"
            npcData.constitution = 2
            npcData.level = 2
            npcData.armor = 3
            #--------
            adagaData = WeaponData()
            adagaData.name = "Adaga velha"
            adagaData.type = "Arma"
            adagaData.description = "Uma adaga velha que ja perdeu a lamina há muito tempo"
            adagaData.w_type = 'melee'
            npcData.weapon = Weapon(adagaData)
            npc = NPC(npcData) 
            #--------
            print(f"Um {npc.get_name()} surgiu! ele está equipado com {npc.get_weapon().name}!")
            
                    
    def show_scene(self):
        print("""Voce está de frente a uma caverna, no meio de uma floresta. Esta caverna aparenta ser muito antiga e, aparentemente, ninguém vem aqui há muito tempo, pois você descobriu a caverna após retirar várias plantas que bloqueavam a entrada.""")
        npc_kobold = NPC("Edgar", "Kobold", "warrior", "neutral evil", "Enemy", 2, [5, 8, 2, 1, 1, 2], 
"Um kobold guerreiro armado com uma espada enferrujada e quebrada. Parece um rato.",
"espada velha", 24, 6, "vivo")
        print(npc_kobold.get_stats('health'))
        npc_kobold.set_health(40)
        print(npc_kobold.get_stats('health'))
        weapon = Weapon('Longsword', 'Weapon', 'melee', 'Espada enferrujada',5 )
        npc_kobold.set_weapon(weapon)
        print(npc_kobold.print_weapon())
        
        npc_kobold
           
        print(f"Voce encontra {npc_kobold._description}")
          
   