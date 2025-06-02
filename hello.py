#!/usr/bin/env python3

from player import Player
from enemy import Enemy
import quest
import json


def combat(enemy, player):
    while player.health != 0 or enemy.is_alive():
        action = input("What would you like to do? Attack/Run: ")
        if action == "Attack":
            damage = enemy.health - player.strength
            print(f"{player.name} attacks {enemy.name} for {damage} damage!")
            enemy.health -= damage
        elif action == "Run":
            print("You ran away!")
            break


goblin1 = Enemy("Goblin", 3)
p1 = Player()

p1.set_health()
