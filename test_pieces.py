import unittest
from game.pieces import Pieces, Board

class TestBoard(unittest.TestCase):
    def test_init(self):
        board = Board()
        self.assertEqual(len(board.__grid__),8,)
        self.assertEqual(len(board.__grid__[0]),8,)
    
    def print_board(self):
        board = Board()
        self.board.print_board()

if __name__ == '__main__':
    board = Board()
    board.print_board()
    unittest.main()
