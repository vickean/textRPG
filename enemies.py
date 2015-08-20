class Enemy(object):
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def __str__(self):
        return "ENEMY\nName: %s\n=====\nHP: %s\nDamage: %s\n" % (
            self.name, self.hp, self.damage)

    def is_alive(self):
        return self.hp > 0

class GiantSpider(Enemy):
    def __init__(self):
        super(GiantSpider, self).__init__("Giant Spider", 10, 2)

class Ogre(Enemy):
    def __init__(self):
        super(Ogre, self).__init__("Ogre", 30, 15)
