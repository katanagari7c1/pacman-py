from pacman.pacman import Direction


# Game tick function. Receives current game state
# and should return the new state
def tick(current_state, direction):
    new_state = list(current_state)
    pacman_index = __find_pacman_position(new_state)

    if direction is not None:
        new_state[pacman_index] = ' '

    (pacman_new_index, pacman) = __calculate_pacman_new_position(new_state, pacman_index, direction)
    new_state[pacman_new_index] = pacman

    return ''.join(new_state)


def __find_pacman_position(state):
    for i, obj in enumerate(state):
        if obj in ['v', '<', '^', '>']:
            return i


def __calculate_pacman_new_position(state, pacman_position, direction):
    new_position = pacman_position
    new_pacman = state[pacman_position]
    board_width = len(state)

    if direction == Direction.RIGHT:
        new_position = (pacman_position + 1) % board_width
        new_pacman = '<'
    elif direction == Direction.LEFT:
        new_position = (pacman_position - 1) % board_width
        new_pacman = '>'

    if state[new_position] == '#':
        new_position = pacman_position

    return new_position, new_pacman
