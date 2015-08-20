_world = {}
_game_map = {}

def load_tiles():
    """Parses a file that describes the world space into the _world object"""
    with open('resources/map.txt', 'r') as f:
        rows = f.readlines()

    x_max = len(rows[0].split(','))# Assumes all rows contain the same number of tabs

    for y in range(len(rows)):
        cols = rows[y].split(',')
        for x in range(x_max):
            tile_name = cols[x].replace('\n', '') # Windows users may need to replace '\r\n'
            _game_map[(x, y)] = tile_name
            _world[(x, y)] = None if tile_name == '' else getattr(__import__('tiles'), tile_name)(x, y)


def tile_exists(x, y):
    return _world.get((x, y))

def return_start_coordinates():
    pos = [key for key, val in _game_map.items() if val == 'StartingRoom']
    return pos[0][0], pos[0][1]
