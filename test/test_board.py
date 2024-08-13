import unittest
from io import StringIO
import sys
from game.pieces import Pieces, Queen, King, Knight, Pawn, Rook, Bishop
from game.board import Board
from game.exceptions import InvalidMove

class TestBoard(unittest.TestCase):
    def test_init(self):
        board = Board()
        self.assertEqual(len(board.__grid__),8,)
        self.assertEqual(len(board.__grid__[0]),8,)
   
    def test_print_board(self):
            board = Board()
            board.set_piece_cell_begining()
            captured_output = StringIO()
            sys.stdout = captured_output
            board.print_board()
            sys.stdout = sys.__stdout__
            self.maxDiff = None
            
            expected_output = (
                " --------------------------------------------------------\n"
                "        |  A  |  B  |  C  |  D  |  E  |  F  |  G  |  H  |\n"
                " --------------------------------------------------------\n"
                "     0  |  r  |  n  |  b  |  q  |  k  |  b  |  n  |  r  |\n"
                " --------------------------------------------------------\n"
                "     1  |  p  |  p  |  p  |  p  |  p  |  p  |  p  |  p  |\n"
                " --------------------------------------------------------\n"
                "     2  |     |     |     |     |     |     |     |     |\n"
                " --------------------------------------------------------\n"
                "     3  |     |     |     |     |     |     |     |     |\n"
                " --------------------------------------------------------\n"
                "     4  |     |     |     |     |     |     |     |     |\n"
                " --------------------------------------------------------\n"
                "     5  |     |     |     |     |     |     |     |     |\n"
                " --------------------------------------------------------\n"
                "     6  |  P  |  P  |  P  |  P  |  P  |  P  |  P  |  P  |\n"
                " --------------------------------------------------------\n"
                "     7  |  R  |  N  |  B  |  Q  |  K  |  B  |  N  |  R  |\n"
                " --------------------------------------------------------\n"

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

    def test_check_squares_1(self):
        board = Board()      
        board.set_piece_cell_begining()
        with self.assertRaises(InvalidMove):
            board.check_squares([[1,0],[2,0]])
    
    def test_check_squares_2(self):
        board = Board()      
        board.set_piece_cell_begining()
        with self.assertRaises(InvalidMove):
            board.check_squares([[1,0],[2,0]])
    
    def test_move_piece_1(self):
        board = Board()
        board.set_piece_cell_begining()
        piece = board.__pieces__[-1]
        board.move_piece(piece, [5,7])
        self.assertEqual(piece.__position__, [5,7])
    
    def test_move_piece_2(self):
        board = Board()
        board.set_piece_cell_begining()
        piece = board.__pieces__[0]
        with self.assertRaises(InvalidMove):
            board.move_piece(piece, [0,4])

if __name__ == '__main__':
    unittest.main()
