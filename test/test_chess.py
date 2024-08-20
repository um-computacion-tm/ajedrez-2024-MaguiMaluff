import unittest
from game.board import Board
from game.player import Player
from game.chess import Chess
from game.exceptions import WrongPiece, OutOfBoard

class TestChess(unittest.TestCase):
    def test_init(self):
        chess = Chess()
        self.assertIsNotNone(chess.__board__)
        self.assertEqual(chess.__turn__.__color__, 'w')
        self.assertEqual(chess.__turn__.__id__, 1)
    
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
        end = chess.end_game()
        self.assertEqual(end, False)