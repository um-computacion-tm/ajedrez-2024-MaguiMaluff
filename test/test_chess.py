import unittest
from game.board import Board
from game.player import Player
from game.chess import Chess
from game.exceptions import WrongPiece, OutOfBoard, LimitedMove

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
    
    def test_end_game(self):
        chess = Chess()
        end = chess.end_game('y')
        self.assertEqual(chess.__playing__, False)

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