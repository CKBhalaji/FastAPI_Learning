from Enemy import *
import random

class Zombi(Enemy):
    def __init__(self, helth_points, attack_damage):
        super().__init__(type_of_enemy="Zombi", helth_points=helth_points, attack_dammage=attack_damage)

    def talk(self):
        print("*Grumbling...*")

    def spread_disease(self):
        print("The zombies are trying th spread infection")
        
    def special_attack(self):
        did_special_attack_work = random.random() < .50
        if did_special_attack_work:
            self.helth_points += 2
            print("Zombi regenerates 2 health points!")