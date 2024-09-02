from game.pieces import Pieces
from game.exceptions import LimitedMove

class Knight(Pieces):
    """Represents a Knight chess piece, inheriting from the Pieces class."""

    def limit(self, new_position):
        """ Checks if the Knight's move is valid according to its movement rules.
            The Knight moves in an L-shape: two squares in one direction and 
            one square perpendicular. If the move is not valid, an exception 
            is raised.
        
        Parameters
        ----------
        new_position : list
            The new position [row, column] the Knight is moving to.
        
        Raises
        ------
        LimitedMove
            If the move does not follow the Knight's L-shaped movement rule.
        """
        row = self.__position__[0]
        column = self.__position__[1]
        list = [[row - 2, column - 1],
                       [row - 2, column + 1],
                       [row - 1, column - 2],
                       [row - 1, column + 2],
                       [row + 1, column - 2],
                       [row + 1, column + 2],
                       [row + 2, column - 1],
                       [row + 2, column + 1]]
        
        if new_position not in list:
            raise LimitedMove("You can only move in an L shape")
    
    def movement(self, new_position):
        """ Determines if the Knight's move is valid and returns the move. 
            If valid, it returns the new position.
        
        Parameters
        ----------
        new_position : list
            The new position [row, column] the Knight is moving to.
        
        Returns
        -------
        list
            A list containing the new position if the move is valid.
        
        Raises
        ------
        LimitedMove
            If th move does not follow the Knight's L-shaped movement rule.
        """
        try:
            self.limit(new_position)
            return([new_position])
        except Exception as e:
            raise