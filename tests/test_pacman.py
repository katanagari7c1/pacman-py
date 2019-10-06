import unittest
from pacman.pacman import Pacman, Direction


# TODO Tests can be more robust if we avoid exposing the Direction enum
# TODO and check all valid directions
class TestPacman(unittest.TestCase):
    def setUp(self):
        self.pacman = Pacman()

    def test_starts_facing_up(self):
        self.assertEqual(self.pacman.direction, Direction.UP)

    def test_position_can_be_changed(self):
        self.pacman.setDirection(Direction.LEFT)
        self.assertEqual(self.pacman.direction, Direction.LEFT)

    def test_invalid_direction_does_not_change_pacmans_direction(self):
        self.pacman.setDirection('1234')
        self.assertEqual(self.pacman.direction, Direction.UP)
