from game.pieces import Pieces

class Queen(Pieces):
    def movement(self, new_position):
        try:
            squares = self.valid_or_invalid(new_position)
            return squares
        except Exception as e:
            raise