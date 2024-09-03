import unittest
from game.pieces import Pieces 
from game.queen import Queen
from game.rook import Rook
from game.board import Board
from game.exceptions import InvalidMove

class TestPieces(unittest.TestCase):
        def test_set_images(self):
            queen_1 = Pieces("Queen", "w", (0,3))
            queen_2 = Pieces("Queen", "b", (0,0))
            queen_1.set_images()
            queen_2.set_images()
            self.assertEqual(queen_1.__image__, '👑')
            self.assertEqual(queen_2.__image__, '🌼')

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
        
        def test_move(self):
            piece = Pieces('Queen', 'b', [0, 4])
            piece.movement([0, 8])
        
        def test_get_positition(self):
            piece = Pieces('Queen', 'b', [0, 4])
            self.assertEqual(piece.get_position(), [0,4])


        







