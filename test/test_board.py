import unittest
from io import StringIO
import sys
from game.pieces import Pieces, Queen, King, Knight, Pawn, Rook, Bishop
from game.board import Board
from game.exceptions import InvalidMove, GoingThroughAPiece, SameColor, LimitedMove, OutOfBoard

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
                " ----------------------------------------------------------------\n"
                "        |  A   |  B   |  C   |  D   |  E   |  F   |  G   |  H   | \n"
                " ----------------------------------------------------------------\n"
                "    0   |  🗿  |  🦄  |  🔱  |  👑  |  🧝  |  🔱  |  🦄  |  🗿  | \n"
                " ----------------------------------------------------------------\n"
                "    1   |  👃  |  👃  |  👃  |  👃  |  👃  |  👃  |  👃  |  👃  | \n"
                " ----------------------------------------------------------------\n"
                "    2   |      |      |      |      |      |      |      |      | \n"
                " ----------------------------------------------------------------\n"
                "    3   |      |      |      |      |      |      |      |      | \n"
                " ----------------------------------------------------------------\n"
                "    4   |      |      |      |      |      |      |      |      | \n"
                " ----------------------------------------------------------------\n"
                "    5   |      |      |      |      |      |      |      |      | \n"
                " ----------------------------------------------------------------\n"
                "    6   |  👤  |  👤  |  👤  |  👤  |  👤  |  👤  |  👤  |  👤  | \n"
                " ----------------------------------------------------------------\n"
                "    7   |  🏢  |  🐴  |  🍁  |  🌼  |  🤴  |  🍁  |  🐴  |  🏢  | \n"
                " ----------------------------------------------------------------\n"

            )
            
            self.assertEqual(captured_output.getvalue(), expected_output)

    def test_print_board_moved(self):
            board = Board()
            board.set_piece_cell_begining()
            piece = board.__grid__[1][0].__piece__
            board.move_piece(piece, [2,0])
            captured_output = StringIO()
            sys.stdout = captured_output
            board.print_board()
            sys.stdout = sys.__stdout__
            self.maxDiff = None
            
            expected_output = (
                " ----------------------------------------------------------------\n"
                "        |  A   |  B   |  C   |  D   |  E   |  F   |  G   |  H   | \n"
                " ----------------------------------------------------------------\n"
                "    0   |  🗿  |  🦄  |  🔱  |  👑  |  🧝  |  🔱  |  🦄  |  🗿  | \n"
                " ----------------------------------------------------------------\n"
                "    1   |      |  👃  |  👃  |  👃  |  👃  |  👃  |  👃  |  👃  | \n"
                " ----------------------------------------------------------------\n"
                "    2   |  👃  |      |      |      |      |      |      |      | \n"
                " ----------------------------------------------------------------\n"
                "    3   |      |      |      |      |      |      |      |      | \n"
                " ----------------------------------------------------------------\n"
                "    4   |      |      |      |      |      |      |      |      | \n"
                " ----------------------------------------------------------------\n"
                "    5   |      |      |      |      |      |      |      |      | \n"
                " ----------------------------------------------------------------\n"
                "    6   |  👤  |  👤  |  👤  |  👤  |  👤  |  👤  |  👤  |  👤  | \n"
                " ----------------------------------------------------------------\n"
                "    7   |  🏢  |  🐴  |  🍁  |  🌼  |  🤴  |  🍁  |  🐴  |  🏢  | \n"
                " ----------------------------------------------------------------\n"

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
        position = [2,0]
        cell = board.__grid__[position[0]][position[1]]
        with self.assertRaises(GoingThroughAPiece):
            board.check_squares_multiple(piece, [[1,0],[2,0]], cell)
    
    def test_check_squares_2(self):
        board = Board() 
        piece = Queen("Queen", 'b', [0,0]) 
        position = [7,0]
        cell = board.__grid__[position[0]][position[1]]    
        board.set_piece_cell_begining()
        with self.assertRaises(GoingThroughAPiece):
            board.check_squares_multiple(piece, [[1,2],[7,0]], cell)
    
    def test_check_squares_3(self):
        board = Board()
        piece = Queen("Queen", 'w', [0,0])
        position = [6,6]
        cell = board.__grid__[position[0]][position[1]]
        board.set_piece_cell_begining()
        eat = board.check_squares_multiple(piece, [[2,0],[2,1],[2,3],[6,6]], cell)
        self.assertEqual(eat, "eat")

    def test_check_squares_4(self):
        board = Board()
        piece = Queen("Queen", 'b', [0,0])
        position = [3,4]
        cell = board.__grid__[position[0]][position[1]]
        board.set_piece_cell_begining()
        board.check_squares_multiple(piece, [[3,0], [3,1],[3,3], [3,4]], cell)
    
    def test_check_squares_5(self):
        board = Board()
        piece = Queen("Queen", 'b', [0,0])
        position = [6,0]
        cell = board.__grid__[position[0]][position[1]]
        board.set_piece_cell_begining()
        with self.assertRaises(GoingThroughAPiece):
            board.check_squares_multiple(piece, [[5,0],[7,0], [6,0]], cell)
    
    def test_check_squares_6(self):
        board = Board()
        piece = Queen("Queen", 'b', [0,0])
        position = [7,0]
        cell = board.__grid__[position[0]][position[1]]
        board.set_piece_cell_begining()
        with self.assertRaises(GoingThroughAPiece):
            board.check_squares_multiple(piece, [[6,6],[7,0]], cell)
    
    def test_check_squares_7(self):
        board = Board()
        piece = Queen("Queen", 'b', [0,0])
        board.set_piece_cell_begining()
        position = [6,6]
        cell = board.__grid__[position[0]][position[1]]
        with self.assertRaises(SameColor):
            board.check_squares_multiple(piece, [[2,0],[2,1],[2,3],[6,6]], cell)

    
    ### Test Check Squares One

    def test_check_one_1(self):
        board = Board()
        board.set_piece_cell_begining()
        position = [1,0]
        cell = board.__grid__[position[0]][position[1]]
        with self.assertRaises(SameColor):
            board.check_squares_one(board.__grid__[0][0].__piece__, [1,0], cell)

    def test_check_one_2(self):
        board = Board()
        board.set_piece_cell_begining()
        position = [7,6]
        cell = board.__grid__[position[0]][position[1]]
        with self.assertRaises(SameColor):
            board.check_squares_one(board.__grid__[7][7].__piece__, [7,6], cell)
    
    def test_check_one_3(self):
        board = Board()
        board.set_piece_cell_begining()
        position = [6,6]
        cell = board.__grid__[position[0]][position[1]]
        eat = board.check_squares_one(board.__grid__[0][0].__piece__, [6,6], cell)
        self.assertEqual(eat, "eat")

    def test_check_one_4(self):
        board = Board()
        board.set_piece_cell_begining()
        position = [1,6]
        cell = board.__grid__[position[0]][position[1]]
        eat = board.check_squares_one(board.__grid__[7][3].__piece__, [1,6], cell)
        self.assertEqual(eat, "eat")

    ### Test Eat Piece

    def test_eating_1(self):
        board = Board()
        board.set_piece_cell_begining()
        piece = Queen("Queen", 'w', [0,0])
        piece.set_images()
        position = [6,6]
        cell = board.__grid__[position[0]][position[1]]
        self.assertEqual(board.__grid__[6][6].__piece__.__image__, '👤')
        board.eat_piece(piece, [6,6], cell)
        self.assertEqual(board.__grid__[6][6].__piece__.__image__, '👑')
    
    def test_eating_2(self):
        board = Board()
        board.set_piece_cell_begining()
        piece = Queen("Queen", 'b', [0,0])
        position = [1,1]
        cell = board.__grid__[position[0]][position[1]]
        self.assertEqual(board.__grid__[1][1].__piece__.__image__, '👃')
        board.eat_piece(piece, position, cell)
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
        board.__grid__[1][3].moved()
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

    ### Test Pawn

    def test_pawn_1(self):
        board = Board()
        board.set_piece_cell_begining()
        pawn = board.__grid__[6][7].__piece__
        position = [5,6]
        cell = board.__grid__[position[0]][position[1]]
        with self.assertRaises(InvalidMove):
            board.pawn(pawn, [5,6], cell)
    
    def test_pawn_2(self):
        board = Board()
        board.set_piece_cell_begining()
        pawn = board.__grid__[1][1].__piece__
        cell = board.__grid__[2][2]
        piece = Pawn('Pawn', 'b' ,[2,2])
        cell.__piece__ = piece
        cell.__state__ = False
        eat = board.pawn(pawn, [2,2], cell)
        self.assertEqual(eat, 'eat')
    
    def test_pawn_3(self):
        board = Board()
        board.set_piece_cell_begining()
        pawn = board.__grid__[1][1].__piece__
        cell = board.__grid__[2][1]
        piece = Pawn('Pawn', 'b' ,[2,1])
        cell.__piece__ = piece
        cell.__state__ = False
        with self.assertRaises(InvalidMove):
            board.pawn(pawn, [2,1], cell)

    def test_pawn_4(self):
        board = Board()
        board.set_piece_cell_begining()
        pawn = board.__grid__[6][7].__piece__
        with self.assertRaises(InvalidMove):
            board.move_piece(pawn, [5,6])
    
    def test_pawn_5(self):
        board = Board()
        board.set_piece_cell_begining()
        pawn = board.__grid__[6][6].__piece__
        cell = board.__grid__[5][5]
        piece = Pawn('Pawn', 'w' ,[5,5])
        cell.__piece__ = piece
        cell.__state__ = False
        eat = board.pawn(pawn, [5,5], cell)
        self.assertEqual(eat, 'eat')
    
    def test_pawn_6(self):
        board = Board()
        board.set_piece_cell_begining()
        pawn = board.__grid__[6][1].__piece__
        cell = board.__grid__[5][1]
        piece = Pawn('Pawn', 'w' ,[5,1])
        cell.__piece__ = piece
        cell.__state__ = False
        with self.assertRaises(InvalidMove):
            board.pawn(pawn, [5,1], cell)
    
    def test_pawn_7(self):
        board = Board()
        board.set_piece_cell_begining()
        pawn = board.__grid__[6][1].__piece__
        board.move_piece(pawn, [5,1])
        self.assertEqual(pawn.__position__, [5,1])
        self.assertEqual(board.__grid__[6][1].__piece__, None)
        self.assertEqual(board.__grid__[6][1].__state__, True)

    # Test Out Of Board
    def test_out_up(self):
        board = Board()
        with self.assertRaises(OutOfBoard):
            board.on_board([-1, 3])

    def test_out_down(self):
        board = Board()
        with self.assertRaises(OutOfBoard):
            board.on_board([122, 1])

    def test_out_right(self):
        board = Board()
        with self.assertRaises(OutOfBoard):
            board.on_board([1, 34])

    def test_out_left(self):
        board = Board()
        with self.assertRaises(OutOfBoard):
            board.on_board([1, -2])





if __name__ == '__main__':
    unittest.main()
