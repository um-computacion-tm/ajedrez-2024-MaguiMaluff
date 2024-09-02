import unittest
from game.knight import Knight
from game.exceptions import LimitedMove

class TestKnight(unittest.TestCase):
    
    def test_knight_2(self):
        knight = Knight('Knight', 'b', [0,0])
        knight.movement([2,1])
    
    def test_knight_3(self):
        knight = Knight('Knight', 'b', [0,0])
        with self.assertRaises(LimitedMove):
            knight.movement([3,3])