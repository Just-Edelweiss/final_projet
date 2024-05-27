class Object:
    def __init__(self, name, type = 'weapon' or 'item', count = 0):
        self.name = name
        self.type = type
        self.count = count

sword = Object(name = 'sword', type = 'weapon')
heal = Object(name='health_potion', type='item')