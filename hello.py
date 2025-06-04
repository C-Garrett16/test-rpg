#!/usr/bin/env python3

from player import Player
from enemy import Goblin
import quest
import json
import ref



goblin1 = Goblin(3)
p1 = Player()

p1.set_health()

print(goblin1.health)
print(goblin1.xp)
print(p1.health)
