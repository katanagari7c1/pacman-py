from pacman.model.items import *
from pacman.model.pacman import Pacman


def _create_space(item_string):
    return Space()


def _create_pacman(item_string):
    return Pacman()


class GameState(object):

    def __init__(self, string_state):
        self._state = []
        # TODO: Later on this logic should be moved to a Builder
        # Then, this object will be completely decoupled of the string
        # representation
        for row in string_state:
            items_string = list(row)
            items = []
            for i in items_string:
                if i == '#':
                    items.append(Wall())
                elif i in [' ', '.']:
                    items.append(_create_space(i))
                elif i in ['v', '^', '<', '>']:
                    items.append(_create_pacman(i))
            self._state.append(items)

    def get_item_at(self, x, y):
        return self._state[x][y]

    def set_item_at(self, item, x, y):
        self._state[x][y] = item
