import unittest
from unittest.mock import patch
from game.chess import Chess
from cli_folder.cli import play, main


class TestCli(unittest.TestCase):
    @patch('builtins.input', side_effect=['1', 'A', '2', 'A', 'y', 'y'],)
    @patch('builtins.print')
    @patch.object(Chess, 'move_piece_board')
    def test_play_works(self, mock_chess_move, mock_print, mock_input,):
        chess = Chess()
        play(chess)
        self.assertEqual(mock_input.call_count, 5)
        self.assertEqual(mock_print.call_count, 21)
        self.assertEqual(mock_chess_move.call_count, 1)

    @patch('builtins.input', side_effect=['hola', '1', '2', '2', '1', 'A', '2', 'A' ])
    @patch('builtins.print')
    @patch.object(Chess, 'move_piece_board')
    def test_play_dont_work(self, mock_chess_move, mock_print, mock_input):
        chess = Chess()
        play(chess)
        self.assertEqual(mock_input.call_count, 1)
        self.assertEqual(mock_print.call_count, 14)
        self.assertEqual(mock_chess_move.call_count, 0)

    @patch('builtins.input', side_effect=['1', 'A', '2', 'hola', '1', 'A', '2', 'A', 'y', 'y'])
    @patch('builtins.print')
    @patch.object(Chess, 'move_piece_board')
    def test_play_dont_work_worse(self, mock_chess_move, mock_print, mock_input,):
        chess = Chess()
        play(chess)
        self.assertEqual(mock_input.call_count, 4)
        self.assertEqual(mock_print.call_count, 14)
        self.assertEqual(mock_chess_move.call_count, 0)
    
    
    @patch('builtins.input', side_effect=['1', 'A', '2', 'A', 'y', 'y'],)
    @patch('builtins.print')
    @patch.object(Chess, 'move_piece_board')
    def test_play_works(self, mock_chess_move, mock_print, mock_input):
        main()
        self.assertEqual(mock_input.call_count, 6)
        self.assertEqual(mock_print.call_count, 15)
        self.assertEqual(mock_chess_move.call_count, 1)
    
if __name__ == '__main__':
    unittest.main()