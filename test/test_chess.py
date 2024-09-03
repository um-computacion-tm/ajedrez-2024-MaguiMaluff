import unittest
from unittest.mock import patch
from game.board import Board
from game.pieces import Pieces
from game.king import King
from game.pawn import Pawn
from game.player import Player
from game.chess import Chess
from game.exceptions import WrongPiece, OutOfBoard, LimitedMove, NotAnOption, InvalidPiece

class TestChess(unittest.TestCase):
    def test_init(self):
        chess = Chess()
        self.assertIsNotNone(chess.__board__)
        self.assertEqual(chess.__player__.__color__, 'w')
        self.assertEqual(chess.__turn__, 1)
    
    def test_next_turn_1(self):
        chess = Chess()
        chess.next_turn()
        chess.next_turn()
        self.assertEqual(chess.__player__.__color__, 'w')
        self.assertEqual(chess.__turn__, 1)
        self.assertEqual(chess.__number__, 2)
    
    def test_next_turn_2(self):
        chess = Chess()
        chess.next_turn()
        self.assertEqual(chess.__player__.__color__, 'b')
        self.assertEqual(chess.__turn__, 2)
    
    def test_move_1(self):
        chess = Chess()
        piece = chess.__board__.__grid__[1][1].__piece__
        chess.move_piece_board(piece, [2,1])
        self.assertEqual(piece.__position__, [2,1])
    
    def test_move_2(self):
        chess = Chess()
        piece = chess.__board__.__grid__[6][6].__piece__
        with self.assertRaises(WrongPiece):
            chess.move_piece_board(piece, [6,5])
    
    def test_move_3(self):
        chess = Chess()
        chess.next_turn()
        piece = chess.__board__.__grid__[6][6].__piece__
        with self.assertRaises(LimitedMove):
            chess.move_piece_board(piece, [3,6])

    def test_move_4(self):
        chess = Chess()
        chess.next_turn()
        piece = chess.__board__.__grid__[6][6].__piece__
        chess.move_piece_board(piece, [4,6])
        self.assertEqual(piece.__position__, [4, 6])

    def test_get_piece_1(self):
        chess = Chess()
        piece = chess.get_piece(7,4)
        self.assertEqual(piece, chess.__board__.__grid__[7][4].__piece__)

    def test_get_piece_2(self):
        chess = Chess() 
        with self.assertRaises(OutOfBoard):
            chess.get_piece(8,4)
    
    @patch('builtins.input', side_effect=['y'])
    @patch('builtins.print')
    def test_end_game_y(self, mock_print, mock_input):
        chess = Chess()
        chess.check_end('y')
        self.assertEqual(chess.__playing__, False)

    @patch('builtins.input', side_effect=['Y'])
    @patch('builtins.print')
    def test_end_game_y_upp(self, mock_print, mock_input):
        chess = Chess()
        chess.check_end('y')
        self.assertEqual(chess.__playing__, False)

    @patch('builtins.input', side_effect=['n'])
    @patch('builtins.print')
    def test_end_game_n(self,  mock_print, mock_input):
        chess = Chess()
        end = chess.check_end('y')
        self.assertEqual(chess.__playing__, True)

    @patch('builtins.input', side_effect=['m'])
    @patch('builtins.print')
    def test_end_game_m(self, mock_print, mock_input):
        chess = Chess()
        with self.assertRaises(NotAnOption):
            chess.check_end('y')
    
    @patch('builtins.print')
    def test_end_game_h(self, mock_print):
        chess = Chess()
        with self.assertRaises(NotAnOption):
            chess.check_end('h')

    def test_playin(self):
        chess = Chess()
        self.assertEqual(chess.is_playing(), True)

    def test_change_cell(self):
        board = Board()
        board.set_piece_cell_begining()
        cell = board.__grid__[1][0]
        piece = cell.__piece__
        board.change_cell(piece)
        self.assertEqual(cell.__state__, True)
        self.assertEqual(cell.__piece__, None)

    def test_get_column(self):
        chess = Chess()
        self.assertEqual(chess.get_column('A'), 0)
        self.assertEqual(chess.get_column('B'), 1)
        self.assertEqual(chess.get_column('H'), 7)

        with self.assertRaises(ValueError):
            chess.get_column('I')
        
        with self.assertRaises(ValueError):
            chess.get_column('9') 
    
    @patch('builtins.print')
    def test_move_piece_end_king(self, mock_print):
        chess = Chess()
        king = King('King', 'b', [5,6])
        pawn = Pawn('Pawn', 'w', [4,5])
        chess.__board__.__pieces__ = [king ,pawn]
        chess.__board__.set_piece_cell_begining()
        chess.move_piece_board(pawn, [5,6])
        self.assertEqual(chess.__playing__, False)

    @patch('builtins.print')
    def test_check_ending(self, mock_print):
        chess = Chess()
        chess.__number__ = 33
        for lista in  chess.__board__.__grid__:
            for cell in lista:
                cell.__state__ = True
        king = King('King', 'b', [5,6])
        chess.__board__.__pieces__ = [king]
        chess.__board__.set_piece_cell_begining()
        chess.no_pieces()
        self.assertEqual(chess.__playing__, False)
    
    def test_end_king_false(self):
        chess = Chess()
        end = chess.end_king([6,6])
        self.assertFalse(end)
    
    @patch('builtins.input', side_effect=['Rook'])
    @patch('builtins.print')
    def test_change_pawn(self, mock_input, mock_print):
        chess = Chess()
        board = chess.__board__
        for lista in  board.__grid__:
            for cell in lista:
                cell.__state__ = True
                cell.__piece__ = None
        pawn = Pawn('Pawn', 'w', [6,3])
        board.__pieces__ = [pawn]
        board.set_piece_cell_begining()
        chess.move_piece_board(pawn, [7,3])
        self.assertEqual(board.get_piece([7,3]).__name__, 'Rook')
    
    def test_get_piece_out(self):
        chess = Chess()
        with self.assertRaises(OutOfBoard):
            chess.get_piece(8,8)

    def test_get_piece_none(self):
        chess = Chess()
        with self.assertRaises(WrongPiece):
            chess.get_piece(2,2)

    @patch('builtins.input', side_effect=['roook'])
    @patch('builtins.print')
    def test_change_pawn_invalid(self, mock_input, mock_print):
        chess = Chess()
        board = chess.__board__
        for lista in  board.__grid__:
            for cell in lista:
                cell.__state__ = True
                cell.__piece__ = None
        pawn = Pawn('Pawn', 'w', [6,3])
        board.__pieces__ = [pawn]
        board.set_piece_cell_begining()
        with self.assertRaises(InvalidPiece):
            chess.move_piece_board(pawn, [7,3])