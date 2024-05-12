class Player:
    def __init__(self, name, hp, alive = True):
        self.name = name
        self.hp = hp
    
    def is_dead(self):
        print('you is dead')
        self.alive = False