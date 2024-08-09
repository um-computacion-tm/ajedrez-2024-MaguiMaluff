from game.pieces import Pieces
from game.cell import Cell

class Board():
    def __init__(self):         ### Declaracion de cada pieza, con nombre, color y posicion al inicio del juego
            self.__pieces__ = [ Pieces(piece="Queen",  color="w", initial_position=[0, 3]),  Pieces(piece="Queen",   color="b", initial_position=[7, 3]),
                                Pieces(piece="King",   color="w", initial_position=[0, 4]),  Pieces(piece="King",    color="b", initial_position=[7, 4]),
                                Pieces(piece="Rook" ,  color="w", initial_position=[0, 0]),  Pieces(piece="Rook",    color="b", initial_position=[7, 0]),
                                Pieces(piece="Rook" ,  color="w", initial_position=[0, 7]),  Pieces(piece="Rook",    color="b", initial_position=[7, 7]),
                                Pieces(piece="Bishop", color="w", initial_position=[0, 2]),  Pieces(piece="Bishop",  color="b", initial_position=[7, 2]),
                                Pieces(piece="Bishop", color="w", initial_position=[0, 5]),  Pieces(piece="Bishop",  color="b", initial_position=[7, 5]),
                                Pieces(piece="Knight", color="w", initial_position=[0, 1]),  Pieces(piece="Knight",  color="b", initial_position=[7, 1]),
                                Pieces(piece="Knight", color="w", initial_position=[0, 6]),  Pieces(piece="Knight",  color="b", initial_position=[7, 6]),
                                Pieces(piece="Pawn" ,  color="w", initial_position=[1, 0]),  Pieces(piece="Pawn" ,   color="b", initial_position=[6, 0]),
                                Pieces(piece="Pawn" ,  color="w", initial_position=[1, 1]),  Pieces(piece="Pawn" ,   color="b", initial_position=[6, 1]),
                                Pieces(piece="Pawn" ,  color="w", initial_position=[1, 2]),  Pieces(piece="Pawn" ,   color="b", initial_position=[6, 2]),
                                Pieces(piece="Pawn" ,  color="w", initial_position=[1, 3]),  Pieces(piece="Pawn" ,   color="b", initial_position=[6, 3]),
                                Pieces(piece="Pawn" ,  color="w", initial_position=[1, 4]),  Pieces(piece="Pawn" ,   color="b", initial_position=[6, 4]),
                                Pieces(piece="Pawn" ,  color="w", initial_position=[1, 5]),  Pieces(piece="Pawn" ,   color="b", initial_position=[6, 5]),
                                Pieces(piece="Pawn" ,  color="w", initial_position=[1, 6]),  Pieces(piece="Pawn" ,   color="b", initial_position=[6, 6]),
                                Pieces(piece="Pawn" ,  color="w", initial_position=[1, 7]),  Pieces(piece="Pawn" ,   color="b", initial_position=[6, 7]),]
            ### Lista de listas de 8x8
            self.__grid__ = ([[Cell(True, None) for _ in range(8)] for _ in range (8)])
            self.set_piece_cell_begining()
    

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
            position = i.__position__
            x = position[0]
            y = position[1]
            self.__grid__[x][y].__state__ = False
            self.__grid__[x][y].__piece__ = i
        
"""        ### Llama a la funcion en piece que verifica si la forma de movimiento es valida.
        ### Llamar a la funcion check_around, para saber si se puede mover a traves
    def move_piece(self, piece):
        piece_name = piece.__name__
        piece_position = piece.__position__
        piece_color = piece.__color__
        if not piece.lower(piece_name)():
            print("in")"""

