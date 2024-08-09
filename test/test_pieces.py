from game.pieces import Pieces
from game.board import Board
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

             
