import unittest
from game.player import Player

class TestPlayer(unittest.TestCase):
    def test_player_1(self):
        player_1 = Player('w', 1)
        self.assertEqual(player_1.__color__, 'w')
        self.assertEqual(player_1.__points__, 0)
        self.assertEqual(player_1.__id__, 1)
    
    def test_player_2(self):
        player_1 = Player('b', 4)
        self.assertEqual(player_1.__color__, 'b')
        self.assertEqual(player_1.__points__, 0)
        self.assertEqual(player_1.__id__, 4)
    
    def test_get_id(self):
        player = Player('b', 34)
        self.assertEqual(player.get_id(), 34)

    def test_get_color(self):
        player = Player('w', 4)
        self.assertEqual(player.get_color(), 'w')