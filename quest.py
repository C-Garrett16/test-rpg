#!/usr/bin/env python3

class Quest:
    def __init__(self, description, reward, xp):
        self.description = description
        self.reward = reward
        self.xp = xp
        self.completed = False

    def complete (self, player):
        print(f"You've completed the quest: {self.description}")
        player.gain_xp(self.reward)
        self.completed = True


main_quest = Quest("Defeat the dragon!", "Flame Sword", 100)

side_quest = Quest("Defeat the Goblin!", "Gold Coin", 50)
