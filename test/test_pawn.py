import unittest
from game.pawn import Pawn
from game.exceptions import LimitedMove

class TestPawn(unittest.TestCase):
    def test_pawn_2(self):
        pawn = Pawn('Pawn', 'w', [0,0])
        self.assertTrue(pawn.movement([1,1]))
    
    def test_pawn_3(self):
        pawn = Pawn('Pawn', 'b', [0,0])
        with self.assertRaises(LimitedMove):
            pawn.movement([0,3])
    
    def test_change_pawn(self):
        pawn = Pawn('Pawn', 'b', [0,0])
        self.assertTrue(pawn.change_pawn())

    def test_change_pawn_2(self):
        pawn = Pawn('Pawn', 'w', [7,4])
        self.assertTrue(pawn.change_pawn())
    
    def test_change_pawn_3(self):
        pawn = Pawn('Pawn', 'b', [7,0])
        self.assertFalse(pawn.change_pawn())

    def test_change_pawn_4(self):
        pawn = Pawn('Pawn', 'w', [4,5])
        self.assertFalse(pawn.change_pawn())