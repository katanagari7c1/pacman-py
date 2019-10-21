from pacman.model.items import *
from pacman.model.pacman import Pacman, Direction


def _create_space(item_string):
    sp = Space()

    if item_string == '.':
        sp.content = Dot()

    return sp


def _create_pacman(item_string):
    pac = Pacman()
    if item_string == 'v':
        pac.direction = Direction.UP
    elif item_string == '^':
        pac.direction = Direction.DOWN
    elif item_string == '>':
        pac.direction = Direction.LEFT
    elif item_string == '<':
        pac.direction = Direction.RIGHT
    return pac


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


def board_to_string(board):
    rep = []
    for row in board:
        rowstr = ''
        for item in row:
            if isinstance(item, Wall):
                rowstr += '#'
            elif isinstance(item, Space):
                rowstr += '.' if isinstance(item.content, Dot) else ' '
            elif isinstance(item, Pacman):
                if item.direction == Direction.UP:
                    rowstr += 'v'
                elif item.direction == Direction.DOWN:
                    rowstr += '^'
                elif item.direction == Direction.LEFT:
                    rowstr += '>'
                elif item.direction == Direction.RIGHT:
                    rowstr += '<'
                else:
                    rowstr += '?'
            else:
                rowstr += '_'
        rep.append(rowstr)

    return tuple(rep)


def board_width(board):
    return len(board[0])


def board_height(board):
    return len(board)
