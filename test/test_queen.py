import unittest
from game.queen import Queen
from game.exceptions import InvalidMove

class TestQueen(unittest.TestCase):
    def test_queen_straight_right(self):
        queen = Queen('Queen', 'w', [0,3])
        list = queen.movement([0,7])
        self.assertEqual(list, [[0,4], [0,5], [0,6], [0,7]])

    def test_queen_straight_up(self):
        queen = Queen('Queen', 'b', [7,3])
        list = queen.movement([0,3])
        self.assertEqual(list, [[6,3], [5,3], [4,3], [3,3], [2,3], [1,3], [0,3]])
    
    def test_queen_diagonal_left_b(self):
        queen = Queen('Queen', 'b', [7,3])
        list = queen.movement([5,1])
        self.assertEqual(list, [[6,2], [5,1]])
    
    def test_queen_diagonal_right_b(self):
        queen = Queen('Queen', 'b', [7,3])
        list = queen.movement([5,5])
        self.assertEqual(list, [[6,4], [5,5]])
    
    def test_queen_diagonal_left_w(self):
        queen = Queen('Queen', 'w', [0,3])
        list = queen.movement([3,0])
        self.assertEqual(list, [[1,2], [2,1], [3,0]])
    
    def test_queen_diagonal_right_w(self):
        queen = Queen('Queen', 'w', [0,3])
        list = queen.movement([4,7])
        self.assertEqual(list, [[1,4], [2,5], [3,6], [4,7]])
    
    def test_queen_invalid(self):
        queen = Queen('Queen', 'w', [0,3])
        with self.assertRaises(InvalidMove):
         queen.movement([3,5])