# -*- coding: utf-8 -*-
import json
import sys
from character.player.Player import Player_Decoder , Player_Encoder


""" 
Created on Thu Jul 20 01:06:35 2023


SAVE GAME
Responsável por salvar e carregar o jogo
@author: User
"""

class Save():
    def __init__(self):
        self.is_saved = False
        self.is_loaded = False
        
    def is_game_saved(self):
        return self.is_saved
    
    def is_game_loaded(self):
        return self.is_loaded
        
    def save_game(self, obj, file_path):
        with open(file_path, "w") as save_file:
            json.dump(obj, save_file, cls=Player_Encoder)
            self.is_saved = True
           
   
            
    def load_game(self, file_path):
        with open(file_path, "r") as load_file:
            self.is_loaded = True
            return json.load(load_file, cls=Player_Decoder)
