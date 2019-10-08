import unittest
from pacman.model.exception import InvalidBoard
from pacman.model.board import Board


class TestBoard(unittest.TestCase):
    def test_board_is_created_from_string_representation(self):
        board_repr = ('#.<.#', '#...#')
        board = Board(board_repr)

        self.assertEqual(5, board.width)
        self.assertEqual(2, board.height)

    def test_board_fails_if_no_pacman_is_present(self):
        board_repr = ('##', '##')
        with self.assertRaises(InvalidBoard):
            Board(board_repr)

    def test_board_fails_if_more_than_one_pacman_is_present(self):
        board_repr = ('#.<.#', '#.^.#')
        with self.assertRaises(InvalidBoard):
            Board(board_repr)
