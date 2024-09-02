from game.pieces import Pieces
from game.exceptions import InvalidMove

class Bishop(Pieces):
    def movement(self, new_position):
        try:
            squares = self.diagonal(new_position)
            if not squares:
                raise InvalidMove("This is not a valid move")
            return squares
        except Exception as e:
            raise