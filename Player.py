from random import randint
from Object import *

class Player:
    def __init__(self, name, hp, alive = True):
        self.name = name
        self.hp = hp
        self.alive = alive

    def afficher(self):
        print(self.name, 'a', self.hp, 'hp')

    def is_dead(self):
        print(self.name, 'is dead')
        self.alive = False

    def attaquer(self, enemie):
        print(self.name, 'attack', enemie.name)
        if randint(1, 6) < 6:
            enemie.hp -= 3
        else:
            print('critical hit !')
            enemie.hp -= 5
        enemie.afficher()
        if enemie.hp <= 0:
            enemie.is_dead()

    def heal(self):
        if heal.count > 0:
            self.pv += 5
            self.afficher()
            heal.count -= 1
        else:
            print("You don't have any heal on you.")