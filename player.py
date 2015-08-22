import items
import world
import random

class Player(object):
    inventory = [items.Gold(15), items.Rock()]
    hp = 100
    location_x, location_y = world.pos  # Change to starting room coordinates
    victory = False

    def is_alive(self):
        return self.hp > 0

    def print_inventory(self):
        for item in self.inventory:
            print item, '\n'

    def print_hp(self):
        print "You currently have %s HP." % self.hp

    def move(self, dx, dy):
        self.location_x += dx
        self.location_y += dy
        print(world.tile_exists(self.location_x, self.location_y).intro_text())

    def move_north(self):
        self.move(0, -1)

    def move_south(self):
        self.move(0, 1)

    def move_east(self):
        self.move(1, 0)

    def move_west(self):
        self.move(-1, 0)

    def attack(self, enemy):
        best_weapon = None
        max_dmg = 0
        for i in self.inventory:
            if isinstance(i, items.Weapon):
                if i.damage > max_dmg:
                    max_dmg = i.damage
                    best_weapon = i

        print"You use %s against %s!" % (best_weapon.name, enemy.name)

        enemy.hp -= best_weapon.damage

        if not enemy.is_alive():
            print "You killed %s!" % enemy.name
        else:
            print "%s HP is %s." % (enemy.name, enemy.hp)

    def do_action(self, action, **kwargs):
        action_method = getattr(self, action.method.__name__)
        if action_method:
            action_method(**kwargs)

    def flee(self, tile):
        """Moves the player randomly to an adjacent tile"""
        available_moves = tile.adjacent_moves()
        r = random.randint(0, len(available_moves) - 1)
        self.do_action(available_moves[r])