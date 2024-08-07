from game.pieces import Pieces
import unittest

class TestPieces(unittest.TestCase):
        def test_set_images(self):
            queen_1 = Pieces("Queen", "w", (0,3))
            queen_2 = Pieces("Queen", "b", (0,0))
            queen_1.set_images()
            queen_2.set_images()
            self.assertEqual(queen_1.__image__, '♛')
            self.assertEqual(queen_2.__image__, '♕')