from pacman.model.pacman import Pacman, Direction
from pacman.model.items import *


# Game tick function. Receives current game state
# and should return the new state
def tick(current_state, direction):
    new_state = __copy_state(current_state)
    pacman_x, pacman_y = __find_pacman_position(new_state)

    if direction is not None:
        new_state[pacman_x][pacman_y] = Space()

    (pacman_new_x, pacman_new_y, pacman) = __calculate_pacman_new_position(new_state, (pacman_x, pacman_y), direction)
    new_state[pacman_new_x][pacman_new_y] = pacman

    return new_state


def __copy_state(current_state):
    new_state = []
    for row in current_state:
        new_state.append(row.copy())

    return new_state


def __find_pacman_position(state):
    for i, row in enumerate(state):
        for j, item in enumerate(row):
            if isinstance(item, Pacman):
                return i, j


def __calculate_pacman_new_position(state, pacman_position, direction):
    new_position = list(pacman_position)
    new_pacman = Pacman()
    if direction is not None:
        new_pacman.direction = direction
    else:
        new_pacman.direction = state[pacman_position[0]][pacman_position[1]].direction

    board_width = len(state[0])
    board_height = len(state)

    if direction == Direction.RIGHT:
        new_position[1] = (pacman_position[1] + 1) % board_width
    elif direction == Direction.LEFT:
        new_position[1] = (pacman_position[1] - 1) % board_width
    elif direction == Direction.UP:
        new_position[0] = (pacman_position[0] - 1) % board_height
    elif direction == Direction.DOWN:
        new_position[0] = (pacman_position[0] + 1) % board_height

    if isinstance(state[new_position[0]][new_position[1]], Wall):
        new_position = pacman_position

    return new_position[0], new_position[1], new_pacman
