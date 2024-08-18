import unittest
from io import StringIO
import sys
from game.pieces import Pieces, Queen, King, Knight, Pawn, Rook, Bishop
from game.board import Board
from game.exceptions import InvalidMove, GoingThroughAPiece, SameColor, LimitedMove

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


    ### Test Check Squares Multiple

    def test_check_squares_1(self):
        board = Board()
        piece = Queen("Queen", 'b', [0,0])      
        board.set_piece_cell_begining()
        with self.assertRaises(GoingThroughAPiece):
            board.check_squares_multiple(piece, [[1,0],[2,0]])
    
    def test_check_squares_2(self):
        board = Board() 
        piece = Queen("Queen", 'b', [0,0])     
        board.set_piece_cell_begining()
        with self.assertRaises(GoingThroughAPiece):
            board.check_squares_multiple(piece, [[1,2],[7,0]])
    
    def test_check_squares_3(self):
        board = Board()
        piece = Queen("Queen", 'w', [0,0])
        board.set_piece_cell_begining()
        eat = board.check_squares_multiple(piece, [[2,0],[2,1],[2,3],[6,6]])
        self.assertEqual(eat, "eat")

    def test_check_squares_4(self):
        board = Board()
        piece = Queen("Queen", 'b', [0,0])
        board.set_piece_cell_begining()
        board.check_squares_multiple(piece, [[3,0], [3,1],[3,3], [3,4]])
    
    def test_check_squares_5(self):
        board = Board()
        piece = Queen("Queen", 'b', [0,0])
        board.set_piece_cell_begining()
        with self.assertRaises(GoingThroughAPiece):
            board.check_squares_multiple(piece, [[5,0],[7,0], [6,0]])
    
    def test_check_squares_6(self):
        board = Board()
        piece = Queen("Queen", 'b', [0,0])
        board.set_piece_cell_begining()
        with self.assertRaises(GoingThroughAPiece):
            board.check_squares_multiple(piece, [[6,6],[7,0]])
    
    def test_check_squares_7(self):
        board = Board()
        piece = Queen("Queen", 'b', [0,0])
        board.set_piece_cell_begining()
        with self.assertRaises(SameColor):
            board.check_squares_multiple(piece, [[2,0],[2,1],[2,3],[6,6]])

    
    ### Test Check Squares One

    def test_check_one_1(self):
        board = Board()
        board.set_piece_cell_begining()
        with self.assertRaises(SameColor):
            board.check_squares_one(board.__grid__[0][0].__piece__, [1,0])

    def test_check_one_2(self):
            board = Board()
            board.set_piece_cell_begining()
            with self.assertRaises(SameColor):
                board.check_squares_one(board.__grid__[7][7].__piece__, [7,6])
    
    def test_check_one_3(self):
        board = Board()
        board.set_piece_cell_begining()
        eat = board.check_squares_one(board.__grid__[0][0].__piece__, [6,6])
        self.assertEqual(eat, "eat")

    def test_check_one_4(self):
        board = Board()
        board.set_piece_cell_begining()
        eat = board.check_squares_one(board.__grid__[7][3].__piece__, [1,6])
        self.assertEqual(eat, "eat")

    ### Test Eat Piece

    def test_eating_1(self):
        board = Board()
        board.set_piece_cell_begining()
        piece = Queen("Queen", 'w', [0,0])
        piece.set_images()
        self.assertEqual(board.__grid__[6][6].__piece__.__image__, 'P')
        board.eat_piece(piece, [6,6])
        self.assertEqual(board.__grid__[6][6].__piece__.__image__, 'q')
    
    def test_eating_2(self):
        board = Board()
        board.set_piece_cell_begining()
        piece = Queen("Queen", 'b', [0,0])
        self.assertEqual(board.__grid__[1][1].__piece__.__image__, 'p')
        board.eat_piece(piece, [1,1])
        self.assertEqual(board.__grid__[1][1].__piece__, piece)

    ### Test Move Piece

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
        with self.assertRaises(SameColor):
            board.move_piece(piece, [0,4])
    
    def test_move_piece_3(self):
        board = Board()
        board.set_piece_cell_begining()
        piece = board.__grid__[0][0].__piece__
        with self.assertRaises(GoingThroughAPiece):
            board.move_piece(piece, [0,4])
    
    def test_move_piece_4(self):
        board = Board()
        board.set_piece_cell_begining()
        piece = board.__grid__[0][0].__piece__
        board.__grid__[1][0].__state__ = True        
        board.move_piece(piece, [4,0])
        self.assertEqual(piece.__position__, [4,0])

    def test_move_piece_5(self):
        board = Board()
        board.set_piece_cell_begining()
        piece = board.__grid__[0][3].__piece__
        board.__grid__[1][3].__state__ = True        
        board.move_piece(piece, [6,3])
        self.assertEqual(piece.__position__, [6,3])

    ### Test Knight

    def test_knight_1(self):
        board = Board()
        board.set_piece_cell_begining()
        knight = board.__grid__[7][1].__piece__
        board.move_piece(knight, [5,2])
        self.assertEqual(knight.__position__, [5,2])
    
    def test_knight_2(self):
        board = Board()
        board.set_piece_cell_begining()
        knight = board.__grid__[7][1].__piece__
        with self.assertRaises(LimitedMove):
            board.move_piece(knight, [5,1])

if __name__ == '__main__':
    unittest.main()
