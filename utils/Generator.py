
import random
from character.player.Player import Player , PlayerData

#Generators to use in the game----



def stats_generator(character):
    statscount = 0
    statvalues = []
    while statscount < 6:
        
        statvalues.append(random.randint(1, 6))
        statscount+= 1
    
    return statvalues
    
