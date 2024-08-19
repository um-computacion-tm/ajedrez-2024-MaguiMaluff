from game.pieces import Pieces, Queen, King, Rook, Bishop, Knight, Pawn
from game.cell import Cell
from game.exceptions import InvalidMove, GoingThroughAPiece, SameColor

class Board():
    def __init__(self):         ### Declaracion de cada pieza, con nombre, color y posicion al inicio del juego
            self.__pieces__ = [ Queen(piece="Queen",  color="w", initial_position=[0, 3]),   Queen(piece="Queen",   color="b", initial_position=[7, 3]),
                                King(piece="King",   color="w", initial_position=[0, 4]),    King(piece="King",    color="b", initial_position=[7, 4]),
                                Rook(piece="Rook" ,  color="w", initial_position=[0, 0]),    Rook(piece="Rook",    color="b", initial_position=[7, 0]),
                                Rook(piece="Rook" ,  color="w", initial_position=[0, 7]),    Rook(piece="Rook",    color="b", initial_position=[7, 7]),
                                Bishop(piece="Bishop", color="w", initial_position=[0, 2]),  Bishop(piece="Bishop",  color="b", initial_position=[7, 2]),
                                Bishop(piece="Bishop", color="w", initial_position=[0, 5]),  Bishop(piece="Bishop",  color="b", initial_position=[7, 5]),
                                Knight(piece="Knight", color="w", initial_position=[0, 1]),  Knight(piece="Knight",  color="b", initial_position=[7, 1]),
                                Knight(piece="Knight", color="w", initial_position=[0, 6]),  Knight(piece="Knight",  color="b", initial_position=[7, 6]),
                                Pawn(piece="Pawn" ,  color="w", initial_position=[1, 0]),    Pawn(piece="Pawn" ,   color="b", initial_position=[6, 0]),
                                Pawn(piece="Pawn" ,  color="w", initial_position=[1, 1]),    Pawn(piece="Pawn" ,   color="b", initial_position=[6, 1]),
                                Pawn(piece="Pawn" ,  color="w", initial_position=[1, 2]),    Pawn(piece="Pawn" ,   color="b", initial_position=[6, 2]),
                                Pawn(piece="Pawn" ,  color="w", initial_position=[1, 3]),    Pawn(piece="Pawn" ,   color="b", initial_position=[6, 3]),
                                Pawn(piece="Pawn" ,  color="w", initial_position=[1, 4]),    Pawn(piece="Pawn" ,   color="b", initial_position=[6, 4]),
                                Pawn(piece="Pawn" ,  color="w", initial_position=[1, 5]),    Pawn(piece="Pawn" ,   color="b", initial_position=[6, 5]),
                                Pawn(piece="Pawn" ,  color="w", initial_position=[1, 6]),    Pawn(piece="Pawn" ,   color="b", initial_position=[6, 6]),
                                Pawn(piece="Pawn" ,  color="w", initial_position=[1, 7]),    Pawn(piece="Pawn" ,   color="b", initial_position=[6, 7]),]
            ### Lista de listas de 8x8
            self.__grid__ = ([[Cell(True, None) for _ in range(8)] for _ in range (8)])    

    ### Impresion del board, con las piezas en posicion actual
    def print_board(self):
        self.print_header()
        self.print_pieces()

    ### Imprime las letras de cada columna
    def print_header(self):
        print(' '+'-'*56)
        print('   {:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|'.format("", "A", "B" , "C", "D" , "E" , "F" , "G" ,"H" ))
        print(' '+'-'*56)
    
    ### Llama a print_row 8 veces
    def print_pieces(self):
        for i in range(8):
            self.print_rows(i)
            
    ### Row es una lista, a la que voy agrgando de a uno la imagen de la pieza que esta
    ### en esa posicion, si no hay pieza, no imprime nada alli.
    ### Imprime todo formateado para que se vea ordenado
    ### self.__grid__[i][x].__piece__.__image__, grid[][] me selecciona una fila y una columna
    ### donde hay una celda, .piece me llama a la pieza que esta en la celda, -image, se
    ### se refiere a la imagen de la pieza.
    def print_rows(self, i):
        row = [i] 
        for x in range(8):
                if self.__grid__[i][x].__state__ == False:
                    row.append(str(self.__grid__[i][x].__piece__.__image__))
                else:
                    row += ' '
        print('   {:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|'.format(*row))
        print(' '+'-'*56)

                

    ### Order by pieces, check the piece position, asign the 
    ### piece to the cell that belongs to the position on the grid
    ### and changes the state
    def set_piece_cell_begining(self):
        for i in self.__pieces__:
            i.set_images()
            position = i.__position__
            x = position[0]
            y = position[1]
            self.__grid__[x][y].__state__ = False
            self.__grid__[x][y].__piece__ = i

    ### If the movement is valid, this function checks each
    ### square the piece intents to go through for pieces.
    ### A cell could be occupied only if the piece there 
    ### is a different color and the cell is the last position
    def check_squares_multiple(self, piece, squares):
        for square in squares:
            x = square[0]
            y = square[1]
            cell_state = self.__grid__[x][y].__state__
            if cell_state == False and [x , y] != squares[-1]:
                raise GoingThroughAPiece()
            elif cell_state == False and [x , y] == squares[-1]:
                try:
                    eat = self.check_squares_one(piece, squares[-1])
                    return eat
                except Exception as e:
                    raise
            elif cell_state == True and [x , y] == squares[-1]:
                return 'move'
    
    ### If the piece only moves one square, this function
    ### checks if the new cell is occupied, and if it is,
    ### it checks the color.
    def check_squares_one(self, piece, squares):
            x = squares[0]
            y = squares[1]
            cell = self.__grid__[x][y]
            if cell.__state__ == False and cell.__piece__.__color__ == piece.__color__:
                raise SameColor()
            elif cell.__state__ == True:
                return 'move'
            else: 
                return "eat"

    def eat_piece(self, piece, new_position):
        row = new_position[0]
        column = new_position[1]
        self.__grid__[row][column].__piece__ = piece
        piece.__position__ = new_position

    def move_piece(self, piece, new_position):
        eat = None
        try:
            if piece.__name__ == "Knight":
                eat = self.knight(piece, new_position)
            elif piece.__name__ == "Pawn":
                eat = self.pawn(piece, new_position)
            else:
                squares = piece.movement(new_position)
                if len(squares) > 1:
                    eat = self.check_squares_multiple(piece, squares)
                else:
                    eat = self.check_squares_one(piece, new_position)
            if eat == 'eat' or eat == 'move':
                self.eat_piece(piece, new_position)
        except Exception as e:
            raise
    
    def knight(self, piece, new_position):
        squares = piece.movement(new_position)
        eat = self.check_squares_one(piece, squares)
        return eat
    
    def pawn(self, piece, new_position):
        row = piece.__position__[0]
        column = piece.__position__[1]
        # This positions are diagonal, pawn should be
        # eating in order to move there
        eating = [[row + 1, column + 1],
                  [row + 1, column - 1], 
                  [row - 1, column + 1],
                  [row - 1, column - 1]]
        if new_position in eating:
            eat = self.check_squares_one(piece, new_position)
            if eat != 'eat':
                raise InvalidMove
        else:
            eat = self.check_squares_one(piece, new_position)
            if eat == 'eat':
                raise InvalidMove()
        return eat

    
