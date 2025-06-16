from Weapon import *
from Enemy import *

class Hero(Enemy):
    def __init__(self, health_point, attack_damage):
        self.health_point = health_point
        self.attack_damage = attack_damage
        self.is_weapon_equiped = False
        self.weapon: Weapen = None

    def equip_weapon(self):
        if self.weapon is not None and not self.is_weapon_equiped:
            self.attack_damage += self.weapon.attack_increase
            self.is_weapon_equiped = True

    def attack(self):
        print(f"Hero attacks for {self.attack_damage} damage.")