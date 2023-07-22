
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





def screen_clear():
    return os.system('cls')
