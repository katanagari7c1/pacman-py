import unittest
from pacman.model.items import Space, Dot


class TestSpace(unittest.TestCase):
    def test_space_is_created_empty(self):
        self.assertIsNone(Space().content)

    def test_space_can_be_created_with_content(self):
        dot = Dot()
        self.assertEqual(Space(dot).content, dot)
