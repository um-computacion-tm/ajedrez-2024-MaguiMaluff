from game.pieces import Pieces, Queen, King, Bishop, Rook, Pawn, Knight
from game.board import Board
from game.exceptions import OutOfBoard, InvalidMove, LimitedMove
import unittest
from unittest.mock import patch
import builtins

class TestPieces(unittest.TestCase):
        def test_set_images(self):
            queen_1 = Pieces("Queen", "w", (0,3))
            queen_2 = Pieces("Queen", "b", (0,0))
            queen_1.set_images()
            queen_2.set_images()
            self.assertEqual(queen_1.__image__, 'q')
            self.assertEqual(queen_2.__image__, 'Q')
        

        def test_rook_1(self):
            board = Board()
            rook = Rook('Rook', 'w', [0,0])
            board.__pieces__ = [rook]
            board.set_piece_cell_begining()
            result = rook.straight_line([0, 3])
            self.assertEqual(result, [[0, 1], [0, 2], [0, 3]])

        def test_rook_2(self):
            board = Board()
            rook = Rook('Rook', 'w', [0,0])
            board.__pieces__ = [rook]
            board.set_piece_cell_begining()
            result = rook.straight_line([4, 0])
            self.assertEqual(result, [[1, 0], [2, 0], [3, 0], [4, 0]])
        
        def test_rook_wrong(self):
            board = Board()
            rook = Rook('Rook', 'w', [0,0])
            board.__pieces__ = [rook]
            board.set_piece_cell_begining()
            result = rook.straight_line([1, 1])
            self.assertEqual(result, False)

        def test_bishop_1(self):
            board = Board()
            bishop = Rook('Bishop', 'w', [0 ,0])
            board.__pieces__ = [bishop]
            board.set_piece_cell_begining()
            result = bishop.diagonal([1, 1])
            self.assertEqual(result, [[1, 1]])

        def test_bishop_2(self):
            board = Board()
            bishop = Pieces('Bishop', 'w', [0 ,0])
            board.__pieces__ = [bishop]
            board.set_piece_cell_begining()
            result = bishop.diagonal([1, 4])
            self.assertEqual(result, False)
        
        def test_bishop_3(self):
            board = Board()
            bishop = Pieces('Bishop', 'w', [0 ,0])
            board.__pieces__ = [bishop]
            board.set_piece_cell_begining()
            result = bishop.diagonal([1, 0])
            self.assertEqual(result, False)
        
        def test_bishop_4(self):
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
    def test_queen_1(self):
        queen = Queen('Queen', 'w', [0,0])
        with self.assertRaises(OutOfBoard):
            queen.movement([0,8])
    
    def test_queen_2(self):
        queen = Queen('Queen', 'w', [0,0])
        with self.assertRaises(OutOfBoard):
            queen.movement([-3,0])
    
    def test_queen_3(self):
        queen = Queen('Queen', 'w', [0,0])
        list = queen.movement([0,4])
        self.assertEqual(list, [[0,1], [0,2], [0,3], [0,4]])

    def test_queen_4(self):
        queen = Queen('Queen', 'b', [7,3])
        list = queen.movement([0,3])
        self.assertEqual(list, [[6,3], [5,3], [4,3], [3,3], [2,3], [1,3], [0,3]])

class TestKing(unittest.TestCase):

    def test_king_1(self):
        king = King('King', 'b', [0,0])
        with self.assertRaises(OutOfBoard):
            king.movement([0,1212])

    def test_king_2(self):
        king = King('King', 'b', [0,0])
        with self.assertRaises(LimitedMove):
            king.movement([0,0])

    def test_king_3(self):
        king = King('King', 'b', [0,0])
        with self.assertRaises(LimitedMove):
            king.movement([4,0])
    
    def test_king_4(self):
        king = King('King', 'b', [1,3])
        with self.assertRaises(LimitedMove):
            king.movement([1,0])
    
    def test_king_5(self):
        king = King('King', 'b', [0,3])
        with self.assertRaises(LimitedMove):
            king.limit([1,5])
    
    def test_king_6(self):
        king = King('King', 'b', [7,3])
        list = king.movement([7,2])
        self.assertEqual(list, [[7,2]])


class TestBishop(unittest.TestCase):
    def test_bishop_1(self):
        bishop = Bishop('Bishop', 'b', [0,0])
        with self.assertRaises(OutOfBoard):
            bishop.movement([0,1212])
    
    def test_bishop_2(self):
        bishop = Bishop('Bishop', 'b', [0,0])
        result = bishop.movement([1,1])
        self.assertEqual(result, [[1,1]])
    
    def test_bishop_3(self):
        bishop = Bishop('Bishop', 'b', [0,0])
        result = bishop.diagonal([0,4])
        self.assertEqual(result, False)
    
    def test_bishop_2(self):
        print("bishop")
        bishop = Bishop('Bishop', 'b', [5,7])
        result = bishop.movement([0,2])
        self.assertEqual(result, [[4, 6], [3, 5], [2, 4], [1, 3], [0, 2]])

class TestRook(unittest.TestCase):
    def test_rook_1(self):
        rook = Rook('Rook', 'b', [0,0])
        with self.assertRaises(OutOfBoard):
            rook.movement([0,1212])
    
    def test_rook_2(self):
        rook = Rook('Rook', 'b', [0,0])
        result = rook.movement([1,1])
        
    
    def test_rook_3(self):
        rook = Rook('Rook', 'b', [0,0])
        result = rook.diagonal([0,4])
        self.assertEqual(result, False)

class TestPawn(unittest.TestCase):
    def test_pawn_1(self):
        pawn = Pawn('Pawn', 'b', [0,0])
        with self.assertRaises(OutOfBoard):
            pawn.movement([0,1212])
    
    def test_pawn_2(self):
        pawn = Pawn('Pawn', 'w', [0,0])
        result = pawn.movement([1,1])
    
    def test_pawn_3(self):
        pawn = Pawn('Pawn', 'b', [0,0])
        with self.assertRaises(LimitedMove):
            pawn.movement([0,3])

class TestKnight(unittest.TestCase):
    def test_knight_1(self):
        knight = Knight('Knight', 'b', [0,0])
        with self.assertRaises(OutOfBoard):
            knight.movement([0,-4])
    
    def test_knight_2(self):
        knight = Knight('Knight', 'b', [0,0])
        knight.movement([2,1])
    
    def test_knight_3(self):
        knight = Knight('Knight', 'b', [0,0])
        with self.assertRaises(LimitedMove):
            knight.movement([3,3])