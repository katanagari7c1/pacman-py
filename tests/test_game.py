import unittest
from pacman.pacman import Direction
import pacman.game as game


# TODO It would be better if I create an abstraction of the board?
# TODO even though I have to rewrite all tests :-(
class TestGame(unittest.TestCase):
    def test_pacman_dont_move_at_beginning(self):
        board = ('.v.',
                 '...')
        new_board = game.tick(board, None)
        self.assertEqual(board, new_board)

    def test_pacman_moves_right_when_input_given(self):
        board = ('.v.', '...')
        expected = ('. <', '...')
        new_board = game.tick(board, Direction.RIGHT)
        self.assertEqual(expected, new_board)

    def test_pacman_moves_left_when_input_given(self):
        board = ('.v.', '...')
        expected = ('> .', '...')
        new_board = game.tick(board, Direction.LEFT)
        self.assertEqual(expected, new_board)

    def test_pacman_passes_through_empty_borders(self):
        board = ('.v.', '...')
        expected = ('  >', '...')
        step1 = game.tick(board, Direction.LEFT)
        new_board = game.tick(step1, Direction.LEFT)

        self.assertEqual(expected, new_board)

    def test_pacman_stops_at_wall(self):
        board = ('#..v..#', '#.....#')
        expected = ('#..  <#', '#.....#')
        step1 = game.tick(board, Direction.RIGHT)
        step2 = game.tick(step1, Direction.RIGHT)
        new_board = game.tick(step2, Direction.RIGHT)

        self.assertEqual(expected, new_board)

    def test_pacman_can_move_up(self):
        board = ('#.....#',
                 '#..v..#')
        expected = ('#..v..#',
                    '#.. ..#')
        new_board = game.tick(board, Direction.UP)
        self.assertEqual(expected, new_board)

    def test_pacman_can_wrap_vertically(self):
        board = ('#.....#',
                 '#..v..#')
        expected = ('#.. ..#',
                    '#..v..#')

        step1 = game.tick(board, Direction.UP)
        new_board = game.tick(step1, Direction.UP)
        self.assertEqual(expected, new_board)

    def test_pacman_cannot_pass_through_a_wall(self):
        board = ('#..#..#',
                 '#..v..#')
        expected = ('#..#..#',
                    '#..^..#')

        new_board = game.tick(board, Direction.DOWN)
        self.assertEqual(expected, new_board)
