#!/usr/bin/env python3

health_mod = 5

class Goblin:
    def __init__(self, level):
        self.strength = 10
        self.health = self.strength * health_mod
        self.inv = ["Sword", "Armor"]
        self.xp = self.health / self.strength
        self.level = level

    def attack(self, player):
        print("The Goblin attacks!")
        player.health -= self.strength



class Dragon:
    def __init__(self, level):
        self.strength = 50
        self.health = self.strength * health_mod
        self.xp = self.health / self.strength * self.level
        self.level = self.level

    def attack(self, player):
        print("The Dragon attacks!")
        player.health -= self.strength
