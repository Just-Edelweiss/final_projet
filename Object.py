class Object:
    def __init__(self, name, type = 'weapon' or 'item', count = 0):
        self.name = name
        self.type = type
        self.count = count

heal = Object('health_potion', 'item', 1)