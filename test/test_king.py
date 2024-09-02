import unittest
from game.king import King
from game.exceptions import LimitedMove

class TestKing(unittest.TestCase):
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