import unittest
from game.rook import Rook
from game.exceptions import InvalidMove

class TestRook(unittest.TestCase):
    def test_rook_2(self):
        rook = Rook('Rook', 'b', [0,0])
        with self.assertRaises(InvalidMove):
            rook.movement([1,1])
        
    
    def test_rook_3(self):
        rook = Rook('Rook', 'b', [0,0])
        result = rook.diagonal([0,4])
        self.assertEqual(result, False)
