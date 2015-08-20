class Item(object):
    """The base class for all items"""
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return "%s\n=====\nDescription:\n%s\n\nValue: %s\n" % (self.name, self.description, self.value)

class Gold(Item):
    def __init__(self, amt):
        self.amt = amt
        super(Gold, self).__init__("Gold",
                                   "A round coin made from a shiny precious metal.",
                                   self.amt)

class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.name = name
        self.description = description
        self.value = value
        self.damage = damage

    def __str__(self):
        return "%s\n=====\nDescription:\n%s\n\nValue: %s\n\nDamage: %s\n" % (
            self.name, self.description, self.value, self.damage)

class Rock(Weapon):
    def __init__(self):
        super(Rock, self).__init__("Rock",
                                   "A fist-sized rock,good for breaking heads.",
                                   0,
                                   5)

class Dagger(Weapon):
    def __init__(self):
        super(Dagger, self).__init__("Dagger",
                                     "Pointy, rusty and potentially deadly.",
                                     10,
                                     10)
