from pacman.pacman import Direction


# Game tick function. Receives current game state
# and should return the new state
def tick(current_state, direction):
    new_state = __copy_state(current_state)
    pacman_x, pacman_y = __find_pacman_position(new_state)

    if direction is not None:
        new_state[pacman_x][pacman_y] = ' '

    (pacman_new_x, pacman_new_y, pacman) = __calculate_pacman_new_position(new_state, (pacman_x, pacman_y), direction)
    new_state[pacman_new_x][pacman_new_y] = pacman

    return __convert_to_output_state(new_state)


def __copy_state(current_state):
    new_state = []
    for row in current_state:
        new_state.append(list(row))

    return new_state


def __convert_to_output_state(state):
    output_state = []
    for row in state:
        output_state.append(''.join(row))

    return tuple(output_state)


def __find_pacman_position(state):
    for i, row in enumerate(state):
        for j, item in enumerate(row):
            if item in ['v', '<', '^', '>']:
                return i, j


def __calculate_pacman_new_position(state, pacman_position, direction):
    new_position = list(pacman_position)
    new_pacman = state[pacman_position[0]][pacman_position[1]]
    board_width = len(state[0])
    board_height = len(state)

    if direction == Direction.RIGHT:
        new_position[1] = (pacman_position[1] + 1) % board_width
        new_pacman = '<'
    elif direction == Direction.LEFT:
        new_position[1] = (pacman_position[1] - 1) % board_width
        new_pacman = '>'
    elif direction == Direction.UP:
        new_position[0] = (pacman_position[0] - 1) % board_height
        new_pacman = 'v'
    elif direction == Direction.DOWN:
        new_position[0] = (pacman_position[0] + 1) % board_height
        new_pacman = '^'

    if state[new_position[0]][new_position[1]] == '#':
        new_position = pacman_position

    return new_position[0], new_position[1], new_pacman
