import player

class Action(object):
    def __init__(self, method, name, hotkey, **kwargs):
        self.method = method
        self.hotkey = hotkey
        self.name = name
        self.kwargs = kwargs

    def __str__(self):
        return "%s: %s" % (self.hotkey, self.name)

class MoveNorth(Action):
    def __init__(self):
        super(MoveNorth, self).__init__(player.Player.move_north, 'Move north', 'n')


class MoveSouth(Action):
    def __init__(self):
        super(MoveSouth, self).__init__(player.Player.move_south, 'Move south', 's')


class MoveEast(Action):
    def __init__(self):
        super(MoveEast, self).__init__(player.Player.move_east, 'Move east', 'e')


class MoveWest(Action):
    def __init__(self):
        super(MoveWest, self).__init__(player.Player.move_west, 'Move west', 'w')


class ViewInventory(Action):
    """Prints the player's inventory"""
    def __init__(self):
        super(ViewInventory, self).__init__(player.Player.print_inventory, 'View inventory', 'i')

class Attack(Action):
    def __init__(self, enemy):
        super(Attack, self).__init__(player.Player.attack, "Attack", 'a', enemy=enemy)

class Flee(Action):
    def __init__(self, tile):
        super(Flee, self).__init__(player.Player.flee, "Flee", 'f', tile=tile)
