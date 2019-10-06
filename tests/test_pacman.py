import unittest
from pacman.pacman import Pacman


class TestPacman(unittest.TestCase):
    def test_starts_facing_up(self):
        pacman = Pacman()
        self.assertEquals(pacman.position, 'u')
