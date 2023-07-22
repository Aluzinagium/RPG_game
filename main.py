# -*- coding: utf-8 -*-
import sys
import os
from items.Item import Item, ItemData
from character.player.Player import Player, PlayerData
from saves.Save_Game import Save
from scenes.Scene import Scene
from items.weapons.weapon import Weapon, WeaponData
from character.npcs.Npc import NPC, NPCData
from utils.default import *
from Game_State import Game_State, Game_State_Data

"""
Created on Wed Jul 19 20:39:45 2023

MAIN FOLDER

@author: User
"""
save = Save()
  
def main():
      #Limpa a tela e chama a primeira cena do jogo
      screen_clear()
      print("testeee")
      print("E foi memo")
      Scene.main_menu_scene()
      actualscene = Game_State_Data()
      #actualscene.npcstate = 
main()
  
  
  
  
  
  
  
  
  
  
  
  
  
 
   
 

