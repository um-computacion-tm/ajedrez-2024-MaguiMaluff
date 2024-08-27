from game.pieces import Pieces, Queen, King, Rook, Bishop, Knight, Pawn
from game.cell import Cell
from game.exceptions import InvalidMove, GoingThroughAPiece, SameColor, OutOfBoard

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
        print(' '+'-'*64)
        print('   {:^5}|{:^6}|{:^6}|{:^6}|{:^6}|{:^6}|{:^6}|{:^6}|{:^6}|'.format("", "A", "B" , "C", "D" , "E" , "F" , "G" ,"H" ))
        print(' '+'-'*64)
    
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
                cell = self.get_cell([i,x])
                if self.__grid__[i][x].__state__ == False:
                    piece = self.get_piece([i,x])
                    row.append('  ' + str(piece.__image__) + '  |')
                else:
                    row.append('      |')
        print('  {:^6}|{:^6}{:^6}{:^6}{:^6}{:^6}{:^6}{:^6}{:^6}'.format(*row))
        print(' '+'-'*64)

                

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
    def check_squares_multiple(self, piece, squares, cell):
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
    
    ### If the piece only moves one square, this function
    ### checks if the new cell is occupied, and if it is,
    ### it checks the color.
    def check_squares_one(self, piece, squares, cell):
            x = squares[0]
            y = squares[1]
            new_piece = self.get_piece([x, y])
            if cell.__state__ == False and new_piece.__color__ == piece.__color__:
                raise SameColor("Oops! You`re trying to eat your own piece")
            elif cell.__state__ == True:
                return 'move'
            else: 
                return "eat"

    def eat_piece(self, piece, new_position, cell):
        cell.new_piece(piece)
        piece.change_position(new_position)

              
    def on_board(self, new_position):
        x = new_position[0]
        y = new_position[1]
        if x < 0 or x > 7:
            raise OutOfBoard("Please choose a valid position")
        elif y < 0 or y > 7:
            raise OutOfBoard("Please choose a valid position")

    def move_piece(self, piece, new_position):
        eat = None
        cell = self.get_cell(new_position)
        try:
            self.on_board(new_position)
            if piece.__name__ == "Knight":
                piece.movement(new_position)
                eat = self.knight(piece, new_position, cell)
            elif piece.__name__ == "Pawn":
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
        row = piece.__position__[0]
        column = piece.__position__[1]
        cell = self.__grid__[row][column]
        cell.moved()

    def knight(self, piece, new_position, cell):
        squares = piece.movement(new_position)
        eat = self.check_squares_one(piece, squares, cell)
        return eat
    
    def pawn(self, piece, new_position, cell):
        row = piece.__position__[0]
        column = piece.__position__[1]
        # This positions are diagonal, pawn should be
        # eating in order to move there
        eating = [[row + 1, column + 1],
                  [row + 1, column - 1], 
                  [row - 1, column + 1],
                  [row - 1, column - 1]]
        if new_position in eating:
            eat = self.check_squares_one(piece, new_position, cell)
            if eat != 'eat':
                raise InvalidMove("This is not a valid move")
        else:
            eat = self.check_squares_one(piece, new_position, cell)
            if eat == 'eat':
                raise InvalidMove("This is not a valid move")
        return eat
    
    def get_cell(self, position):
        row = position[0]
        col = position[1]
        cell = self.__grid__[row][col]
        return cell

    def get_piece(self, position):
        cell = self.get_cell(position)
        piece = cell.__piece__
        return piece

    
