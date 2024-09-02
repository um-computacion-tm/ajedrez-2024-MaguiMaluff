from game.queen import Queen
from game.king import King
from game.rook import Rook
from game.bishop import Bishop
from game.knight import Knight
from game.pawn import Pawn
from game.cell import Cell
from game.exceptions import InvalidMove, GoingThroughAPiece, SameColor, OutOfBoard

class Board():
    def __init__(self):         ### Declaracion de cada pieza, con nombre, color y posicion al inicio del juego
            self.__pieces__ = [ Queen(piece="Queen",  color="w", initial_position=[0, 3]),   Queen(piece="Queen",   color="b", initial_position=[7, 3]),King(piece="King",   color="w", initial_position=[0, 4]),    King(piece="King",    color="b", initial_position=[7, 4]),
                                Rook(piece="Rook" ,  color="w", initial_position=[0, 0]),    Rook(piece="Rook",    color="b", initial_position=[7, 0]), Rook(piece="Rook" ,  color="w", initial_position=[0, 7]),    Rook(piece="Rook",    color="b", initial_position=[7, 7]),
                                Bishop(piece="Bishop", color="w", initial_position=[0, 2]),  Bishop(piece="Bishop",  color="b", initial_position=[7, 2]), Bishop(piece="Bishop", color="w", initial_position=[0, 5]),  Bishop(piece="Bishop",  color="b", initial_position=[7, 5]),
                                Knight(piece="Knight", color="w", initial_position=[0, 1]),  Knight(piece="Knight",  color="b", initial_position=[7, 1]), Knight(piece="Knight", color="w", initial_position=[0, 6]),  Knight(piece="Knight",  color="b", initial_position=[7, 6]),
                                Pawn(piece="Pawn" ,  color="w", initial_position=[1, 0]),    Pawn(piece="Pawn" ,   color="b", initial_position=[6, 0]), Pawn(piece="Pawn" ,  color="w", initial_position=[1, 1]),    Pawn(piece="Pawn" ,   color="b", initial_position=[6, 1]),
                                Pawn(piece="Pawn" ,  color="w", initial_position=[1, 2]),    Pawn(piece="Pawn" ,   color="b", initial_position=[6, 2]), Pawn(piece="Pawn" ,  color="w", initial_position=[1, 3]),    Pawn(piece="Pawn" ,   color="b", initial_position=[6, 3]),
                                Pawn(piece="Pawn" ,  color="w", initial_position=[1, 4]),    Pawn(piece="Pawn" ,   color="b", initial_position=[6, 4]), Pawn(piece="Pawn" ,  color="w", initial_position=[1, 5]),    Pawn(piece="Pawn" ,   color="b", initial_position=[6, 5]),
                                Pawn(piece="Pawn" ,  color="w", initial_position=[1, 6]),    Pawn(piece="Pawn" ,   color="b", initial_position=[6, 6]), Pawn(piece="Pawn" ,  color="w", initial_position=[1, 7]),    Pawn(piece="Pawn" ,   color="b", initial_position=[6, 7]),]
            
            """On the grid, each square is a cell, with state True(meaning is empty), and piece None"""
            self.__grid__ = ([[Cell(True, None) for _ in range(8)] for _ in range (8)])    

    def print_board(self):
        """Prints the header, then calls print_pieces"""
        print(' '+'-'*64)
        print('   {:^5}|{:^6}|{:^6}|{:^6}|{:^6}|{:^6}|{:^6}|{:^6}|{:^6}|'.format("", "A", "B" , "C", "D" , "E" , "F" , "G" ,"H"), '\n','-'*64)
        self.print_pieces()
        
    def print_pieces(self):
        """Calls print_row 8 times"""
        for i in range(8):
            self.print_rows(i)
            
    def print_rows(self, i):
        """ Row is a list where an image is added if the cell is occupied or 
            spaces if is not. The row is then format. 

            Parameter
            ---------
            i : int
                The first position in row is i, which is the number of row on the board."""
        row = [i] 
        for x in range(8):
                cell = self.get_cell([i,x])
                if cell.__state__ == False:
                    piece = self.get_piece([i,x])
                    row.append('  ' + str(piece.__image__) + '  |')
                else:
                    row.append('      |')
        print('  {:^6}|{:^6}{:^6}{:^6}{:^6}{:^6}{:^6}{:^6}{:^6}'.format(*row), '\n', '-'*64)

                
    def set_piece_cell_begining(self):
        """Goes through the pieces in board, sets its image, looks for the cell that represents that position
            calls cell.new_piece, changing the cell state and piece"""
        for piece in self.__pieces__:
            piece.set_images()
            position = piece.__position__
            cell = self.get_cell([position[0],position[1]])
            cell.new_piece(piece)


    def check_squares_multiple(self, piece, squares, cell):
        """Checks each square the piece intents to go through for pieces.
            A cell could be occupied only if the piece there is a different 
            color and the cell is the last position. If the cell is ocuppied and
            the square is the last, calls fot check_square_one() to check if the
            piece could be capturing another one. If none of the squares its occupied, 
            it just returns "move".

            Parameters
            ----------
            piece : Piece object 
                Piece intended to move.
            squares : list
                Positions that the piece goes through before the new position.
            cell : Cell object
                Last square

            Raises
            ------
            GoingThroughAPiece
                If one of the squares its occupied and the square its not the last
                on the list.
            """
        for square in squares:
            x = square[0]
            y = square[1]
            old_cell = self.get_cell([x,y])
            cell_state = old_cell.__state__
            if cell_state == False and [x , y] != squares[-1]:
                raise GoingThroughAPiece("Oops! You`re trying to go through a piece")
            elif cell_state == False and [x , y] == squares[-1]:
                try:
                    eat = self.check_squares_one(piece, squares[-1], cell)
                    return eat
                except Exception as e:
                    raise
            elif cell_state == True and [x , y] == squares[-1]:
                return 'move'
    

    def check_squares_one(self, piece, squares, cell):
        """Checks the square to see if its occupied by another piece,
            if it is, checks if the colors are different. If they are different,
            then it returns eat, if they are the same it raises an exception.
            If the square its free, it returns move.
            

            Parameters
            ----------
    
            piece : Piece object 
                Piece intended to move.
            squares : list
                Positions that the piece goes through before the new position.
            cell : Cell object
                Last square
            
            Raises
            ------
            SameColor
                If the cell its occupied and the piece intended to move
                has the same color as the piece on the cell.
            """
        new_piece = self.get_piece([squares[0], squares[1]])
        if cell.__state__ == False and new_piece.__color__ == piece.__color__:
            raise SameColor("Oops! You`re trying to eat your own piece")
        elif cell.__state__ == True:
            return 'move'
        else: 
            return "eat"

    def eat_piece(self, piece, new_position, cell):
        """ Calls to new_piece() to change the piece belonging to the cell.
            Calls to change_position() to change the position of the piece.

            Parameters
            ----------
            piece : Piece object 
                Piece intended to move.
            new_position : list
                Position that the piece moves to.
            cell : Cell object
                Last square
            """
        cell.new_piece(piece)
        piece.change_position(new_position)

              
    def on_board(self, new_position):
        """ Checks if the new_position is on the board, meaning the row 
            and column are between 0 and 7. 

            Parameters
            ----------
            piece : Piece object 
                Piece intended to move.
            new_position : list
                Position that the piece moves to.

            Raises
            ------
            OutOfBoard
                If either row or column are greater than 7 or smaller than 0.
            """
        row = new_position[0]
        column = new_position[1]
        if row < 0 or row > 7 or column < 0 or column > 7:
            raise OutOfBoard("Please choose a valid position")
        
    def move_piece(self, piece, new_position):
        """ In charge of verification for the piece movement. First checks
            if the new position is on board calling on_board(). Then checks 
            for exceptions of movement, if the piece is a Pawn, it calls
            for the piece movement() and then for pawn() for an exclusive 
            verification of movement.

            If the piece is other than Pawn, calls for movement(), which returns
            a list of squares. If this list is longer than 1, calls for check_squares_multiple(),
            if its not, calls for check_squares_one(). Then checks if the result of either one 
            is move or eat, if it is it calls for change_cell() which changes the old cell to free,
            and eat_piece().

            Parameters
            ----------
            piece : Piece object 
                Piece intended to move.
            new_position : list
                Position that the piece moves to.
            """
        eat = None
        cell = self.get_cell(new_position)
        try:
            self.on_board(new_position) 
            if piece.__name__ == "Pawn":
                piece.movement(new_position)
                eat = self.pawn(piece, new_position, cell)
            else:
                squares = piece.movement(new_position)
                if len(squares) > 1:
                    eat = self.check_squares_multiple(piece, squares, cell)
                else:
                    eat = self.check_squares_one(piece, new_position, cell)
            if eat == 'eat' or eat == 'move':
                self.change_cell(piece)
                self.eat_piece(piece, new_position, cell)
        except Exception as e:
            raise
    
    def change_cell(self, piece):
        """Changes the old cell, the position in which the piece was
            before movement. 

            Parameters
            ----------
            piece : Piece object
                Piece that has already moved
        """
        cell = self.get_cell([piece.__position__[0], piece.__position__[1]])
        cell.moved()


    def pawn(self, piece, new_position, cell):
        """Compares the new_position and looks for it in list of valid positions also 
            it calls for check_square_one() and saves the ressult in the variable eat.
            If new_position is in eating, it means that the movement is diagonal, 
            that means it must be capturing a piece. If eat is not 'eat', then is an
            Invalid Move. Otherwise, if its 'eat', then it returns the variable eat. 
            Now if the new_position is not in eating, and the variable eat is 'eat',
            it means that the movemnt is diagonal and is not capturing anything, therefore
            its invalid.

            Parameters
            ----------
            piece : Pawn object 
                Piece intended to move.
            new_position : list
                Position that the piece moves to.
            cell : Cell object
                Cell that represents that position.

            Raises
            ------
            InvalidMove
                If the movement is diagonal and the piece is not capturing anything.
                If the movement is straight and the piece is capturing something.
            """
        row = piece.__position__[0]
        column = piece.__position__[1]
        eating = [[row + 1, column + 1], [row + 1, column - 1], [row - 1, column + 1],[row - 1, column - 1]]
        eat = self.check_squares_one(piece, new_position, cell)
        if new_position in eating:
            if eat != 'eat':
                raise InvalidMove("This is not a valid move")
        else:
            if eat == 'eat':
                raise InvalidMove("This is not a valid move")
        return eat
    
    def get_cell(self, position):
        """Gets a cell from the grid, row is the first value of
            position and col the second. Looks fot that position
            on the grid and returns the cell.

            Parameters
            ----------
            position : list
                Coordinates of the cell required
        """
        row = position[0]
        col = position[1]
        cell = self.__grid__[row][col]
        return cell

    def get_piece(self, position):
        """Gets a piece from a cell from the grid. Calls get_cell()
            to get the cell, then gets the piece that belongs on that
            cell and returns it. 

            Parameters
            ----------
            position : list
                Coordinates of the cell required
        """
        cell = self.get_cell(position)
        piece = cell.__piece__
        return piece

    
