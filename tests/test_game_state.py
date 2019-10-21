import unittest
from pacman.model.items import *
from pacman.model.pacman import Pacman
from pacman.model.game_state import GameState


class TestGameState(unittest.TestCase):
    def setUp(self):
        string_state = ('#....#', '#..v.#')
        self.state = GameState(string_state)

    def test_get_wall_from_board(self):
        self.assertIsInstance(self.state.get_item_at(0, 0), Wall)

    def test_get_space_with_dot(self):
        item = self.state.get_item_at(0, 1)
        self.assertIsInstance(item, Space)
        # TODO Beware of that, here I attempted to test a method of Space
        # TODO this is not the correct place, create a test for this class instead
        # TODO If not, a change in game object will break this test
        # self.assertTrue(item.contains_dot())

    def test_get_pacman(self):
        item = self.state.get_item_at(1, 3)
        self.assertIsInstance(item, Pacman)
        # TODO: Corner case: does this pacman reflects the actual board state?

    # First I though of adding a move_pacman operation. After all, we're
    # only interested in moving pacman/ghosts and devour dots. But this leads
    # to moving all game logic to the board, which is undesired. Board should
    # only have getters/setters and other entity should handle the business logic
    def test_board_items_can_be_set(self):
        self.state.set_item_at(Wall(), 0, 1)
        self.assertIsInstance(self.state.get_item_at(0, 1), Wall)
