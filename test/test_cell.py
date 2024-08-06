import unittest
from game.cell import Cell 
from game.pieces import Pieces

class TestCell(unittest.TestCase):
    def test_init(self):
        cell = Cell(True, Pieces("Queen", "b", (1,2)))
        self.assertEqual(cell.__state__, True)
        self.assertEqual(cell.__piece__.__name__, "Queen")