from pacman.model.exception import InvalidBoard


class Board(object):
    width = 0
    height = 0
    _board = []

    def __init__(self, board_string_array):
        self.width = len(board_string_array[0])
        self.height = len(board_string_array)

        pacman_found = 0
        for row in board_string_array:
            found = [s for s in list(row) if any(xs in s for xs in ['v', '<', '>', '^'])]
            pacman_found += len(found)

        if pacman_found != 1:
            raise InvalidBoard()
