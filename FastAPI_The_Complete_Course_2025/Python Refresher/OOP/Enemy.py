class Enemy:
    def __init__(self, type_of_enemy, helth_points, attack_dammage):
        self.__type_of_enemy = type_of_enemy
        self.helth_points = helth_points
        self.attack_dammage = attack_dammage

    def talk(self):
        print(f"I am an Enemy.")

    def walk_forwprd(self):
        print(f"{self.__type_of_enemy} moves closer to you,")

    def attack(self):
        print(f"{self.__type_of_enemy} attacks for {self.attack_dammage} damage")

    def attack_damage(self):
        return self.attack_dammage

    def get_type_of_enemy(self):
        return self.__type_of_enemy

    def health_points(self):
        return self.health_points()

    def special_attack(self):
        print("Enemy has no special attack.")



