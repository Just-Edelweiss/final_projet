import Player
import Enemies
class Object:
    def __init__(self, sword, shield, slurp, damage, block):
        self.sword = sword
        self.shield = shield
        self.slurp = slurp
        self.damage = damage
        self.block = block

    def slurp(self):
        hp += 2
        print(f'you have {hp}hp')

    def sword(self):
        damage = 2
        print(f'your ennemy took {damage}damage')

    def shield(self):
        block = 1
        print('you have bocked the attack')
