#!/usr/bin/env python3


class Enemy:
    def __init__(self, name, strength):
        self.name = name
        self.strength = strength
        self.health = self.strength * 5
        self.inv = ["Sword", "Armor"]

    def attack(self, player):
        print(f"{self.name} attacks!")
        player.health -= self.strength
