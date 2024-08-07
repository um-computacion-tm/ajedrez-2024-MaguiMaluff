import unittest
from io import StringIO
import sys
from game.pieces import Pieces
from game.board import Board
import emoji

class TestBoard(unittest.TestCase):
    def test_init(self):
        board = Board()
        self.assertEqual(len(board.__grid__),8,)
        self.assertEqual(len(board.__grid__[0]),8,)
   
    def test_print_board(self):
            board = Board()           
            captured_output = StringIO()
            sys.stdout = captured_output
            board.print_board()
            sys.stdout = sys.__stdout__
            self.maxDiff = None
            
            expected_output = (
                " --------------------------------------------------\n"
                "  |  A  |  B  |  C  |  D  |  E  |  F  |  G  |  H  |\n"
                " --------------------------------------------------\n"
            )
            for i in range(8):
                expected_output += (
                    f'{i} |     |     |     |     |     |     |     |     |\n'
                    '  |     |     |     |     |     |     |     |     |\n'
                    " --------------------------------------------------\n"
                )
            
            self.assertEqual(captured_output.getvalue(), expected_output)

    def test_set_piece_begining(self):
        board = Board()
        piece_1 = Pieces("Queen", "w", (0,0))
        piece_2 = Pieces("Pawn", "b", (3,4))
        board.__pieces__ = (piece_1, piece_2)
        board.set_piece_cell_begining()
        self.assertEqual(piece_1, board.__grid__[0][0].__piece__)
        self.assertEqual(piece_2, board.__grid__[3][4].__piece__)

if __name__ == '__main__':
    unittest.main()
