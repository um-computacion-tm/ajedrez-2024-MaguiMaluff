import unittest
from game.bishop import Bishop
from game.exceptions import InvalidMove

class TestBishop(unittest.TestCase):
    def test_bishop_2(self):
        bishop = Bishop('Bishop', 'b', [0,0])
        result = bishop.movement([1,1])
        self.assertEqual(result, [[1,1]])
    
    def test_bishop_3(self):
        bishop = Bishop('Bishop', 'b', [0,0])
        with self.assertRaises(InvalidMove):
            bishop.movement([0,4])
    
    def test_bishop_2(self):
        bishop = Bishop('Bishop', 'b', [5,7])
        result = bishop.movement([0,2])
        self.assertEqual(result, [[4, 6], [3, 5], [2, 4], [1, 3], [0, 2]])