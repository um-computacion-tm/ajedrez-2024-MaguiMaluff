from game.pieces import Pieces, Queen, King, Bishop, Rook
from game.board import Board
from game.exceptions import OutOfBoard, InvalidMove, LimitedMove
import unittest
from unittest.mock import patch
import builtins

class TestPieces(unittest.TestCase):
        @patch.object(builtins, 'print')
        def test_set_images(self, mock_print):
            queen_1 = Pieces("Queen", "w", (0,3))
            queen_2 = Pieces("Queen", "b", (0,0))
            queen_1.set_images()
            queen_2.set_images()
            self.assertEqual(queen_1.__image__, 'q')
            self.assertEqual(queen_2.__image__, 'Q')
        
        @patch.object(builtins, 'print')
        def test_rook_1(self, mock_print):
            board = Board()
            rook = Pieces('Rook', 'w', [0,0])
            board.__pieces__ = [rook]
            board.set_piece_cell_begining()
            result = rook.straight_line([0, 3])
            self.assertEqual(result, True)

        @patch.object(builtins, 'print')
        def test_rook_2(self, mock_print):
            board = Board()
            rook = Pieces('Rook', 'w', [0,0])
            board.__pieces__ = [rook]
            board.set_piece_cell_begining()
            result = rook.straight_line([4, 0])
            self.assertEqual(result, True)
        
        @patch.object(builtins, 'print')
        def test_rook_wrong(self, mock_print):
            board = Board()
            rook = Pieces('Rook', 'w', [0,0])
            board.__pieces__ = [rook]
            board.set_piece_cell_begining()
            result = rook.straight_line([1, 1])
            self.assertEqual(result, False)
        
        @patch.object(builtins, 'print')
        def test_bishop_1(self, mock_print):
            board = Board()
            bishop = Pieces('Bishop', 'w', [0 ,0])
            board.__pieces__ = [bishop]
            board.set_piece_cell_begining()
            result = bishop.diagonal([1, 1])
            self.assertEqual(result, True)
        
        @patch.object(builtins, 'print')
        def test_bishop_2(self, mock_print):
            board = Board()
            bishop = Pieces('Bishop', 'w', [0 ,0])
            board.__pieces__ = [bishop]
            board.set_piece_cell_begining()
            result = bishop.diagonal([1, 4])
            self.assertEqual(result, False)
        
        @patch.object(builtins, 'print')
        def test_bishop_3(self, mock_print):
            board = Board()
            bishop = Pieces('Bishop', 'w', [0 ,0])
            board.__pieces__ = [bishop]
            board.set_piece_cell_begining()
            result = bishop.diagonal([1, 0])
            self.assertEqual(result, False)
        
        @patch.object(builtins, 'print')
        def test_bishop_4(self, mock_print):
            board = Board()
            bishop = Pieces('Bishop', 'w', [0 ,0])
            board.__pieces__ = [bishop]
            board.set_piece_cell_begining()
            result = bishop.diagonal([0, 4])
            self.assertEqual(result, False)
        
        def test_valid_or_invalid(self):
            queen = Queen('Queen', 'w', [0,0])
            with self.assertRaises(InvalidMove):
                queen.valid_or_invalid([3,1])

        
class TestQueen(unittest.TestCase):
    def test_1(self):
        queen = Queen('Queen', 'w', [0,0])
        with self.assertRaises(OutOfBoard):
            queen.movement([0,8])
    
    def test_2(self):
        queen = Queen('Queen', 'w', [0,0])
        with self.assertRaises(OutOfBoard):
            queen.movement([-3,0])
    
    def test_3(self):
        queen = Queen('Queen', 'w', [0,0])
        queen.movement([0,4])

class TestKing(unittest.TestCase):

    def test_1(self):
        king = King('King', 'b', [0,0])
        with self.assertRaises(OutOfBoard):
            king.movement([0,1212])

    def test_2(self):
        king = King('King', 'b', [0,0])
        with self.assertRaises(LimitedMove):
            king.movement([0,0])

    def test_3(self):
        king = King('King', 'b', [0,0])
        with self.assertRaises(LimitedMove):
            king.movement([4,0])
    
    def test_4(self):
        king = King('King', 'b', [1,3])
        with self.assertRaises(LimitedMove):
            king.movement([1,0])
    
    def test_5(self):
        king = King('King', 'b', [0,3])
        with self.assertRaises(LimitedMove):
            king.limit([1,5])
    
    def test_6(self):
        king = King('King', 'b', [0,3])
        king.movement([0,4])

class TestBishop(unittest.TestCase):
    def test_1(self):
        bishop = Bishop('Bishop', 'b', [0,0])
        with self.assertRaises(OutOfBoard):
            bishop.movement([0,1212])
    
    def test_2(self):
        bishop = Bishop('Bishop', 'b', [0,0])
        bishop.movement([1,1])
    
    def test_3(self):
        bishop = Bishop('Bishop', 'b', [0,0])
        result = bishop.diagonal([0,4])
        self.assertEqual(result, False)

class TestRook(unittest.TestCase):
    def test_1(self):
        rook = Rook('Rook', 'b', [0,0])
        with self.assertRaises(OutOfBoard):
            rook.movement([0,1212])
    
    def test_2(self):
        rook = Rook('rRook', 'b', [0,0])
        rook.movement([1,1])
    
    def test_3(self):
        rook = Rook('Rook', 'b', [0,0])
        result = rook.diagonal([0,4])
        self.assertEqual(result, False)



        

             
