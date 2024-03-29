from enum import Enum


class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


class Pacman(object):
    direction = Direction.UP

    def setDirection(self, direction):
        for d in Direction:
            if direction == d:
                self.direction = d
