#!/usr/bin/env python3


class Player:
    def __init__(self):
        self.name = input("Please state your name: ")
        self.age = int(input("Please input your age: "))
        if self.age < 18:
            raise ValueError("You must be over 18 to use this software.")
        self.wealth = int(input("How much money do you have? "))
        self.inv = ["Sword", "Leather Armor", "Canteen", "Map"]
        self.strength = int(input("What would you rate for your strength? 1-10: "))
        self.dexterity = int(input("What would you rate for your dexterity? 1-10: "))
        self.intelligence = int(input("What would you rate for your Intelligence? 1-10: "))
        self.stealth = int(input("What would you rate for your stealth? 1-10: "))


    def set_health(self):
        if self.strength <= 5:
            self.health = self.strength * 5
        else:
            self.health = self.strength * 10

    def add_to_inv(self, item):
        self.inv.append(item)

    def rem_from_inv(self, item):
        self.inv.pop(item)

    def display_inv(self):
        j = 1
        for i in self.inv:
            print(f"{j}. {i}")
            j = j + 1

    def manage_inv(self):

        while (p1.health != 0):
            print("What would you like to do?\n")
            print("""
            1. View your inventory\n
            2. Add an item to your inventory\n
            3. Remove an item from your inventory\n
            4. Exit this menu\n
            """)
            choice = input(">>> ")
            match choice:
                case "1":
                    p1.display_inv()
                case "2":
                    item = input("What would you like to add? ")
                    p1.add_to_inv(item)
                case "3":
                    p1.display_inv()
                    item = int(input("What would you like to remove? "))
                    item -= 1
                    p1.rem_from_inv(item)
                case "4":
                    break
