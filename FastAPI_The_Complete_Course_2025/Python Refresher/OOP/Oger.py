from Enemy import *
import random

class Oger(Enemy):
    def __init__(self, helth_points, attack_damage):
        super().__init__(type_of_enemy="Oger",helth_points=helth_points,attack_dammage=attack_damage)

    def talk(self):
        print("Oger is slamming hands all around")
        
    def special_attack(self):
        did_special_attack_work = random.random() < .20
        if did_special_attack_work:
            self.attack_dammage += 4
            print("Oger attsck has increseed by 4 health points!")