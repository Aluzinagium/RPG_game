#Responsável pelo sistema de COMBATE


class Combat():
    def __init__ (self, attackers, attacked):
        self.attackers = attackers
        self.attacked = attacked
        
    def start_combat(self):
        for attackers in self.attackers:
            for attacked in self.attacked:
                self.attack(attackers, attacked)
                
    def attack(self, attacker, defender):
        defender.defend -= attacker.attack