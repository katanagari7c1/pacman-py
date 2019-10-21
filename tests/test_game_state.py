import unittest
from pacman.model.items import *
from pacman.model.pacman import Pacman
from pacman.model.game_state import build_game_state_from_string_tuple, board_width, board_height


class TestGameState(unittest.TestCase):
    def setUp(self):
        string_state = ('#....#', '#..v.#')
        self.state = build_game_state_from_string_tuple(string_state)

    def test_get_wall_from_board(self):
        self.assertIsInstance(self.state[0][0], Wall)

    def test_get_space_with_dot(self):
        item = self.state[0][1]
        self.assertIsInstance(item, Space)
        # TODO Beware of that, here I attempted to test a method of Space
        # TODO this is not the correct place, create a test for this class instead
        # TODO If not, a change in game object will break this test
        # self.assertTrue(item.contains_dot())

    def test_get_pacman(self):
        item = self.state[1][3]
        self.assertIsInstance(item, Pacman)
        # TODO: Corner case: does this pacman reflects the actual board state?

    # First I though of adding a move_pacman operation. After all, we're
    # only interested in moving pacman/ghosts and devour dots. But this leads
    # to moving all game logic to the board, which is undesired. Board should
    # only have getters/setters and other entity should handle the business logic
    def test_board_items_can_be_set(self):
        self.state[0][1] = Wall()
        self.assertIsInstance(self.state[0][1], Wall)

    def test_invalid_coordinates_throws_exception(self):
        with self.assertRaises(IndexError):
            self.state[6][6]

    def test_write_to_invalid_coordinates_throws_exception(self):
        with self.assertRaises(IndexError):
            self.state[6][6] = Wall()

    def test_board_dimensions_are_available(self):
        self.assertEqual(6, board_width(self.state))
        self.assertEqual(2, board_height(self.state))