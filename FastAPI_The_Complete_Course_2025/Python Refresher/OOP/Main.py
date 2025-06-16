from Enemy import *
from Zombi import *
from Oger import *
from Hero import *
from Weapon import *

# def battle(e: Enemy):
#     e.talk()
#     e.attack()
#
# zombi = Zombi(10, 1)
#
# oger = Oger(100,10)

# big_zombi = Enemy("zooommbbiii", 100, 10)
#
# zombi.talk()
#
# zombi.walk_forwprd()
#
# zombi.attack()


# print(f"{zombi.get_type_of_enemy()} has {zombi.helth_points} helth points and ca do an damge of {zombi.attack_dammage}" )

# print(f"{oger.get_type_of_enemy()} has {oger.helth_points} helth points and ca do an damge of {oger.attack_dammage}" )

# zombi.talk()
# oger.talk()

# battle(zombi)
# battle(oger)

# def battle(e1: Enemy, e2: Enemy):
#     e1.talk()
#     e2.talk()
#     # e1.helth_points -=e2.attack_damage()
#     # print(e1.helth_points)
#     while e1.helth_points > 0 and e2.helth_points > 0 :
#         print("----------------------")
#         e1.special_attack()
#         e2.special_attack()
#         print(f"{e1.get_type_of_enemy()}: {e1.helth_points} HP left.")
#         print(f"{e2.get_type_of_enemy()}: {e2.helth_points} HP left.")
#         e2.attack()
#         e1.helth_points -=  e2.attack_damage()
#         e1.attack()
#         e2.helth_points -=  e1.attack_damage()
#     print("----------------------")
#     if e1.helth_points > 0:
#         print(f"{e1.get_type_of_enemy()} wins!")
#     else:
#         print(f"{e2.get_type_of_enemy()} wins!")
#
#
# zombie = Zombi(10, 1)
# oger = Oger(20, 3)
# battle(zombie, oger)


def hero_battle(hero: Hero, enemy: Enemy):
    # e1.helth_points -=e2.attack_damage()
    # print(e1.helth_points)
    while hero.health_point > 0 and enemy.helth_points > 0 :
        print("----------------------")
        enemy.special_attack()
        print(f"Hero: {hero.health_point} HP left.")
        print(f"{enemy.get_type_of_enemy()}: {enemy.helth_points} HP left.")
        enemy.attack()
        hero.health_point -=  enemy.attack_damage()
        hero.attack()
        enemy.helth_points -=  hero.attack_damage
    print("----------------------")
    if hero.health_point > 0:
        print("Hero wins!")
    else:
        print(f"{enemy.get_type_of_enemy()} wins!")


zombi = Zombi(10,1)
oger = Oger(20,3)
hero = Hero(10,1)
weapon = Weapen("Sward", 15)
hero.weapon = weapon
hero.equip_weapon()

hero_battle(hero,oger)
