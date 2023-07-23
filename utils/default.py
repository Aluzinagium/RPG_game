
import os
import sys

#-------------------------- LISTAS----------------------------------

STRING_SENTENCES = {
    'title': "The Bizarre adventures in Pythoria",
    'welcome': "Welcome to the game! are you ready?",
    'victory': "VICTORY! your enemies have been eliminated!!",
    'defeat': "DEFEAT! Your enemies have got you this time.",
    'look': "You can see: ",
    'eating': "you have eaten a ",
    'breaker': "\n\n-----------------------------------------------\n\n\n",
    
}

STATS_ORDER = ['strength', 'dexterity', 'constitution', 'wisdom', 'intelligence', 'carisma']




def screen_clear():
    return os.system('cls')


    
'''print(f" Name: {player.get_name()}      Race: {player.get_race()}\n \
                 class: {player.get_class()}      armor: {player.get_armor()}\n\
                 Description: {player.get_description()} \n\n \
              ------------------STATS-------------------: \n\n \
                 Strength: {player.get_strength()}      Dexterity: {player.get_dexterity()}\n \
                 Constitution: {player.get_constitution()}      Wisdom: {player.get_wisdom()}\n \
                 Intelligence: {player.get_intelligence()}      Carisma: {player.get_carisma()}")'''