import unittest
from utils import board_reader


class TestBoardReader(unittest.TestCase):
    def test_reads_board_from_file(self):
        expected = ('######',
                    '#....#',
                    ' .#v. ',
                    '######')
        board = board_reader.read('resources/small_board.txt')
        self.assertEqual(expected, board)
