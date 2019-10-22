import unittest
from unittest.mock import Mock
from pacman.model.pacman import Direction
from pacman.model.game_board import build_game_state_from_string_tuple as create_board, board_to_string
import engine.game as game


class TestGame(unittest.TestCase):
    def test_pacman_dont_move_at_beginning(self):
        board = create_board(('.v.',
                              '...'))
        new_board = game.tick(board, None)
        self._compare_boards(board, new_board)

    def test_pacman_moves_right_when_input_given(self):
        board = create_board(('.v.', '...'))
        expected = create_board(('. <', '...'))
        new_board = game.tick(board, Direction.RIGHT)
        self._compare_boards(expected, new_board)

    def test_pacman_moves_left_when_input_given(self):
        board = create_board(('.v.', '...'))
        expected = create_board(('> .', '...'))
        new_board = game.tick(board, Direction.LEFT)
        self._compare_boards(expected, new_board)

    def test_pacman_passes_through_empty_borders(self):
        board = create_board(('.v.', '...'))
        expected = create_board(('  >', '...'))
        step1 = game.tick(board, Direction.LEFT)
        new_board = game.tick(step1, Direction.LEFT)

        self._compare_boards(expected, new_board)

    def test_pacman_stops_at_wall(self):
        board = create_board(('#..v..#', '#.....#'))
        expected = create_board(('#..  <#', '#.....#'))
        step1 = game.tick(board, Direction.RIGHT)
        step2 = game.tick(step1, Direction.RIGHT)
        new_board = game.tick(step2, Direction.RIGHT)

        self._compare_boards(expected, new_board)

    def test_pacman_can_move_up(self):
        board = create_board(('#.....#',
                              '#..v..#'))
        expected = create_board(('#..v..#',
                                 '#.. ..#'))
        new_board = game.tick(board, Direction.UP)
        self._compare_boards(expected, new_board)

    def test_pacman_can_wrap_vertically(self):
        board = create_board(('#.....#',
                              '#..v..#'))
        expected = create_board(('#.. ..#',
                                 '#..v..#'))

        step1 = game.tick(board, Direction.UP)
        new_board = game.tick(step1, Direction.UP)
        self._compare_boards(expected, new_board)

    def test_pacman_cannot_pass_through_a_wall(self):
        board = create_board(('#..#..#',
                              '#..v..#'))
        expected = create_board(('#..#..#',
                                 '#..^..#'))

        new_board = game.tick(board, Direction.DOWN)
        self._compare_boards(expected, new_board)

    def _compare_boards(self, expected, actual):
        self.assertEqual(board_to_string(expected), board_to_string(actual))
