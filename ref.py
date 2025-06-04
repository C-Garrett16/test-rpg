#!/usr/bin/env python3


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
