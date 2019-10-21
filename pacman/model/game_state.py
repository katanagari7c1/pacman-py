from pacman.model.items import *
from pacman.model.pacman import Pacman


def _create_space(item_string):
    return Space()


def _create_pacman(item_string):
    return Pacman()


def build_game_state_from_string_tuple(board_string):
    board = []

    for row in board_string:
        items_string = list(row)
        converted_row = []

        for item in items_string:
            if item == '#':
                converted_row.append(Wall())
            elif item in [' ', '.']:
                converted_row.append(_create_space(item))
            elif item in ['v', '^', '<', '>']:
                converted_row.append(_create_pacman(item))

        board.append(converted_row)

    return board


def board_width(board):
    return len(board[0])


def board_height(board):
    return len(board)
